import logging
from flow_control import FlowControl

class Connection:
    def __init__(self, dcid, scid, address):
        self.dcid = dcid  # Destination Connection ID
        self.scid = scid  # Source Connection ID
        self.address = address  # Client address
        self.state = "INITIAL"  # Possible states: INITIAL, HANDSHAKE, ESTABLISHED, CLOSING
        self.keys = None  # Placeholder for encryption keys
        self.flow_control = FlowControl()  # Flow control for managing send/receive windows
        
        logging.info(f"New connection initialized: DCID={dcid}, SCID={scid}, Address={address}")

    def transition_state(self, new_state):
        logging.info(f"Connection {self.dcid} transitioning from {self.state} to {new_state}")
        self.state = new_state

    def set_encryption_keys(self, keys):
        self.keys = keys
        logging.info(f"Encryption keys set for connection {self.dcid}")
    
    def close(self):
        logging.info(f"Closing connection {self.dcid}")
        self.state = "CLOSING"
    
    def update_flow_control(self, bytes_sent=None, bytes_received=None, bytes_acked=None, bytes_processed=None):
        if bytes_sent:
            self.flow_control.update_send_window(bytes_sent)
        if bytes_received:
            self.flow_control.update_recv_window(bytes_received)
        if bytes_acked:
            self.flow_control.restore_send_window(bytes_acked)
        if bytes_processed:
            self.flow_control.restore_recv_window(bytes_processed)
