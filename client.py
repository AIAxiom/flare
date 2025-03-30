import socket
import logging
from src import logger
from src.packet import *

log = logger.setup_logger("Client", level=logging.INFO)


def test_control_packet(server_ip: str, server_port: int):
    """Test sending a control packet to the FLARE server."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(2)

    control_packet = ControlPacket(control_type=0x01, payload=b"Client Control Message")
    flare_packet = FlarePacket(version=1, packet_type=ControlPacket.CONTROL_PACKET, conn_id=123, packet_id=1,
                               packet_obj=control_packet)
    client_socket.sendto(flare_packet.encode(), (server_ip, server_port))

    try:
        response, _ = client_socket.recvfrom(1024)
        log.info(f"Response received for Control Packet: {response}")
    except socket.timeout:
        log.warning("No response received for Control Packet")


def test_large_data_transfer(server_ip: str, server_port: int):
    """Test sending a large amount of data using fragmentation."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(2)

    large_payload = b"X" * 5000  # Large binary data
    chunk_size = 1024
    fragments = []

    for i in range(0, len(large_payload), chunk_size):
        chunk = large_payload[i:i + chunk_size]
        data_packet = DataPacket(total_length=len(large_payload), chunk_offset=i, payload=chunk)
        flare_packet = FlarePacket(version=1, packet_type=DataPacket.DATA_PACKET, conn_id=123,
                                   packet_id=i // chunk_size, packet_obj=data_packet)
        fragments.append(flare_packet.encode())

    for fragment in fragments:
        client_socket.sendto(fragment, (server_ip, server_port))

    try:
        response, _ = client_socket.recvfrom(1024)
        log.info(f"Response received for Data Packet: {response}")
    except socket.timeout:
        log.warning("No response received for Data Packet")


if __name__ == "__main__":
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 4433

    log.info("Starting FLARE client test...")

    # Test control packet
    test_control_packet(SERVER_IP, SERVER_PORT)

    # Test large data transfer
    test_large_data_transfer(SERVER_IP, SERVER_PORT)

    log.info("Tests completed.")
