import logging

class ErrorHandler:
    def __init__(self):
        logging.info("Error Handler initialized")
    
    def log_error(self, message, address):
        logging.error(f"Error at {address}: {message}")
    
    def handle_connection_error(self, dcid, error_code):
        logging.error(f"Connection {dcid} encountered error: {error_code}")
    
    def handle_packet_error(self, packet_data):
        logging.error(f"Malformed packet received: {packet_data.hex()}")
