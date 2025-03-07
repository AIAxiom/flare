import logging

class ConnectionClose:
    def __init__(self, connection_manager):
        self.connection_manager = connection_manager
        logging.info("Connection Close handler initialized")
    
    def send_close_frame(self, connection_id, error_code, reason):
        """Sends a CONNECTION_CLOSE frame."""
        frame = {
            "type": "CONNECTION_CLOSE",
            "error_code": error_code,
            "reason": reason
        }
        logging.info(f"Sending CONNECTION_CLOSE frame for {connection_id}: {frame}")
        return frame  # Placeholder, should be serialized and sent as per QUIC format
    
    def handle_close_frame(self, connection_id, frame):
        """Handles an incoming CONNECTION_CLOSE frame."""
        if frame.get("type") == "CONNECTION_CLOSE":
            logging.info(f"Received CONNECTION_CLOSE frame for {connection_id}: {frame}")
            self.connection_manager.remove_connection(connection_id)
            logging.info(f"Connection {connection_id} closed successfully.")
