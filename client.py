# Client file for FLARE Server. Use this as a testing file

import socket

from src import logger

log = logger.setup_logger("Client")


def test_flare_connection(server_ip: str, server_port: int):
    """Test FLARE connection with a server."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(2)
    client_socket.sendto(b'Client Hello', (server_ip, server_port))

    response, _ = client_socket.recvfrom(1024)
    log.info(f"Response received : {response}")


if __name__ == "__main__":
    SERVER_IP = "127.0.0.1"  # Change to your server's IP
    SERVER_PORT = 4433  # Change to your server's FLARE port

    log.info("Starting FLARE client test...")
    test_flare_connection(SERVER_IP, SERVER_PORT)
    log.info("Test completed.")
