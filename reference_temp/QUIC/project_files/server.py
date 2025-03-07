import socket
import logging
from connection_manager import ConnectionManager
from handshake import QUICHandshake
from packet_builder import PacketBuilder

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QUICServer:
    def __init__(self, host='0.0.0.0', port=4433):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.host, self.port))
        logging.info(f"QUIC Server listening on {self.host}:{self.port}")
        
        self.connection_manager = ConnectionManager()
        self.handshake = QUICHandshake(self.connection_manager)
    
    def start(self):
        while True:
            data, addr = self.socket.recvfrom(65535)
            logging.info(f"Received packet from {addr}: {data.hex()}")
            
            # Assume first byte indicates packet type (simplified for now)
            packet_type = data[0]
            dcid = data[1:9].hex() if len(data) > 8 else None  # Extract DCID assuming fixed length
            packet = {"dcid": dcid} if dcid else {}
            
            if packet_type == 0xC3:  # Initial Packet
                response = self.handshake.process_initial_packet(packet, addr)
            elif packet_type == 0xC1:  # Handshake Packet
                response = PacketBuilder.build_handshake_response(dcid)
            elif packet_type & 0x40 == 0x40:  # Short Header Packet
                logging.info("Received Short Header Packet - Responding with basic ACK")
                response = PacketBuilder.build_short_header_ack(dcid)
            else:
                logging.warning("Unknown packet type received")
                response = None
            
            if response:
                self.socket.sendto(response, addr)
                logging.info(f"Sent response to {addr}: {response.hex()}")

if __name__ == "__main__":
    server = QUICServer()
    server.start()
