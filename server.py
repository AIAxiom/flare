import logging
import socket

from src import logger
from src.constants import *
from src.packet import *

log = logger.setup_logger("FLAREServer", level=logging.INFO)


class FLARE:
    def __init__(self, host='127.0.0.1', port=4433):
        """
        FLARE Server
        """
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.host, self.port))
        self.reassembly_buffer = {}  # Dictionary to store fragmented data
        log.info(f"FLARE Server listening on {self.host}:{self.port}")

    def start(self):
        while True:
            data, addr = self.socket.recvfrom(65535)
            log.info(f"Received packet from {addr}: {data.hex()}")

            try:
                packet = FlarePacket.decode(data)
                if packet.packet_type == CONTROL_PACKET:
                    self.handle_control_packet(packet, addr)
                elif packet.packet_type == DATA_PACKET:
                    self.handle_data_packet(packet, addr)
                else:
                    log.warning("Unknown packet type received.")
            except Exception as e:
                log.error(f"Failed to process packet: {e}")

    def handle_control_packet(self, packet, addr):
        """Handles incoming control packets, including fragmented ones."""
        conn_id = packet.conn_id

        if packet.packet_obj.total_length > len(packet.packet_obj.payload):
            if conn_id not in self.reassembly_buffer:
                self.reassembly_buffer[conn_id] = bytearray(packet.packet_obj.total_length)

            self.reassembly_buffer[conn_id][packet.packet_obj.chunk_offset:packet.packet_obj.chunk_offset + len(
                packet.packet_obj.payload)] = packet.packet_obj.payload
            log.info(
                f"Received Control Packet Chunk: Offset {packet.packet_obj.chunk_offset}, Size {len(packet.packet_obj.payload)}")

            # Check if reassembly is complete
            if all(self.reassembly_buffer[conn_id]):
                full_payload = bytes(self.reassembly_buffer[conn_id])
                log.info(f"Full Control Packet Reassembled for Connection {conn_id}, Size: {len(full_payload)}")
                del self.reassembly_buffer[conn_id]  # Clean up buffer
                response_packet = ControlPacket(control_type=0x02, payload=b"Full Control Packet Received")
                response_flare = FlarePacket(version=1, packet_type=CONTROL_PACKET,
                                             conn_id=packet.conn_id, packet_id=packet.packet_id,
                                             packet_obj=response_packet)
                self.socket.sendto(response_flare.encode(), addr)
        else:
            log.info(f"Received Complete Control Packet: {packet.packet_obj.payload}")
            response_packet = ControlPacket(control_type=0x02, payload=b"Server ACK")
            response_flare = FlarePacket(version=1, packet_type=CONTROL_PACKET, conn_id=packet.conn_id,
                                         packet_id=packet.packet_id, packet_obj=response_packet)
            self.socket.sendto(response_flare.encode(), addr)

    def handle_data_packet(self, packet, addr):
        """Handles incoming data packets and reassembles fragmented data."""
        conn_id = packet.conn_id

        if conn_id not in self.reassembly_buffer:
            self.reassembly_buffer[conn_id] = bytearray(packet.packet_obj.total_length)

        self.reassembly_buffer[conn_id][packet.packet_obj.chunk_offset:packet.packet_obj.chunk_offset + len(
            packet.packet_obj.payload)] = packet.packet_obj.payload
        log.info(
            f"Received Data Packet Chunk: Offset {packet.packet_obj.chunk_offset}, Size {len(packet.packet_obj.payload)}")

        # Check if reassembly is complete
        if all(self.reassembly_buffer[conn_id]):
            log.info(f"Full Data Reassembled for Connection {conn_id}, Size: {len(self.reassembly_buffer[conn_id])}")
            del self.reassembly_buffer[conn_id]  # Clean up buffer
            response_packet = ControlPacket(control_type=0x02, payload=b"Full Data Received")
            response_flare = FlarePacket(version=1, packet_type=CONTROL_PACKET, conn_id=packet.conn_id,
                                         packet_id=packet.packet_id, packet_obj=response_packet)
            self.socket.sendto(response_flare.encode(), addr)


if __name__ == "__main__":
    log.info("Starting Server ...... ")
    server = FLARE()
    server.start()
