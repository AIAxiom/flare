import logging
import os

class StatelessReset:
    def __init__(self, connection_manager):
        self.connection_manager = connection_manager
        logging.info("Stateless Reset handler initialized")
    
    def generate_reset_token(self, dcid):
        """Generates a stateless reset token for a given DCID."""
        return os.urandom(16)  # Placeholder for a proper token derivation
    
    def handle_reset(self, received_token, address):
        """Checks if a received token matches an active connection, and resets if needed."""
        for dcid, connection in self.connection_manager.connections.items():
            expected_token = self.generate_reset_token(dcid)
            if received_token == expected_token:
                logging.info(f"Stateless reset triggered for {dcid} from {address}")
                self.connection_manager.remove_connection(dcid)
                return True
        logging.warning("Received unknown reset token, ignoring.")
        return False
