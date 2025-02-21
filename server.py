import socket
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FLAREServer:
    def __init__(self, host='0.0.0.0', port=4433):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.host, self.port))
        logging.info(f"QUIC Server listening on {self.host}:{self.port}")
    
    def start(self):
        while True:
            data, addr = self.socket.recvfrom(65535)
            logging.info(f"Received packet from {addr}: {data.hex()}")            
            
if __name__ == "__main__":
    server = FLAREServer()
    server.start()
