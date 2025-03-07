import socket
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_quic_packet(packet_type: str, payload: bytes) -> bytes:
    """Create a basic QUIC packet with a simple structure."""
    if packet_type == "initial":
        packet_header = b'\xC3'  # Example Initial Packet Header
    elif packet_type == "handshake":
        packet_header = b'\xE1'  # Example Handshake Packet Header
    elif packet_type == "short":
        packet_header = b'\x43'  # Example Short Header Packet
    else:
        raise ValueError("Unknown packet type")
    
    return packet_header + payload

def test_quic_connection(server_ip: str, server_port: int):
    """Test QUIC connection with a server."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(2)
    
    try:
        logging.info("Sending Initial QUIC packet...")
        initial_packet = create_quic_packet("initial", b'Client Hello')
        client_socket.sendto(initial_packet, (server_ip, server_port))
        
        response, _ = client_socket.recvfrom(1024)
        logging.info(f"Received Response: {response}")
        
        logging.info("Sending Handshake QUIC packet...")
        handshake_packet = create_quic_packet("handshake", b'TLS Handshake Data')
        client_socket.sendto(handshake_packet, (server_ip, server_port))
        
        response, _ = client_socket.recvfrom(1024)
        logging.info(f"Received Response: {response}")
        
        logging.info("Sending Short Header QUIC packet...")
        short_packet = create_quic_packet("short", b'QUIC Data Exchange')
        client_socket.sendto(short_packet, (server_ip, server_port))
        
        response, _ = client_socket.recvfrom(1024)
        logging.info(f"Received Response: {response}")
        
    except socket.timeout:
        logging.error("Timeout: No response from the server")
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        client_socket.close()
        logging.info("Client socket closed.")

if __name__ == "__main__":
    SERVER_IP = "127.0.0.1"  # Change to your server's IP
    SERVER_PORT = 4433  # Change to your server's QUIC port
    
    logging.info("Starting QUIC client test...")
    test_quic_connection(SERVER_IP, SERVER_PORT)
    logging.info("Test completed.")
