import socket
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SocketHandler:
    def __init__(self, host='0.0.0.0', port=4433):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.host, self.port))
        logging.info(f"Socket bound to {self.host}:{self.port}")

    def receive_packet(self):
        data, addr = self.socket.recvfrom(65535)
        logging.info(f"Received {len(data)} bytes from {addr}")
        return data, addr

    def send_packet(self, data, addr):
        self.socket.sendto(data, addr)
        logging.info(f"Sent {len(data)} bytes to {addr}")

if __name__ == "__main__":
    handler = SocketHandler()
    while True:
        packet, address = handler.receive_packet()
        handler.send_packet(b'QUIC Response', address)
