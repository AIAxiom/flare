import logging
import os
import time
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class SessionResumption:
    def __init__(self):
        self.session_tickets = {}
        logging.info("Session Resumption initialized")
    
    def generate_session_ticket(self, connection_id):
        """Generates a session ticket for resumption."""
        ticket_key = os.urandom(32)
        ticket_nonce = os.urandom(12)
        expiry = time.time() + 3600  # 1-hour expiry
        self.session_tickets[connection_id] = {
            "ticket_key": ticket_key,
            "ticket_nonce": ticket_nonce,
            "expiry": expiry
        }
        logging.info(f"Session ticket generated for connection {connection_id}")
        return ticket_key, ticket_nonce
    
    def validate_session_ticket(self, connection_id, ticket_key, ticket_nonce):
        """Validates a received session ticket."""
        stored_ticket = self.session_tickets.get(connection_id)
        if stored_ticket and stored_ticket["expiry"] > time.time():
            if stored_ticket["ticket_key"] == ticket_key and stored_ticket["ticket_nonce"] == ticket_nonce:
                logging.info(f"Valid session ticket for connection {connection_id}")
                return True
        logging.warning(f"Invalid or expired session ticket for connection {connection_id}")
        return False
