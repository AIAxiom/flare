import logging
import socket

from src import logger

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
        log.info(f"FLARE Server listening on {self.host}:{self.port}")

    def start(self):
        while True:
            data, addr = self.socket.recvfrom(65535)
            log.info(f"Received packet from {addr}: {data.hex()}")

            if data:
                self.socket.sendto(b'Server Hello', addr)
                # TODO: Remove the following
                break


if __name__ == "__main__":
    log.info("Starting Server ...... ")
    server = FLARE()
    server.start()
