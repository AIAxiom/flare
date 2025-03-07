import logging

class FlowControl:
    def __init__(self, initial_window=65536, max_window=131072):
        self.send_window = initial_window
        self.recv_window = initial_window
        self.max_window = max_window
        logging.info("Flow Control initialized")

    def update_send_window(self, bytes_sent):
        self.send_window = max(0, self.send_window - bytes_sent)
        logging.info(f"Updated send window: {self.send_window} bytes remaining")

    def update_recv_window(self, bytes_received):
        self.recv_window = max(0, self.recv_window - bytes_received)
        logging.info(f"Updated receive window: {self.recv_window} bytes remaining")

    def can_send(self, bytes_to_send):
        return self.send_window >= bytes_to_send
    
    def can_receive(self, bytes_to_receive):
        return self.recv_window >= bytes_to_receive
    
    def adjust_window(self, new_size):
        self.send_window = min(new_size, self.max_window)
        self.recv_window = min(new_size, self.max_window)
        logging.info(f"Flow control window adjusted to {new_size} bytes")

    def restore_send_window(self, bytes_acked):
        self.send_window = min(self.send_window + bytes_acked, self.max_window)
        logging.info(f"Restored send window: {self.send_window} bytes")
    
    def restore_recv_window(self, bytes_processed):
        self.recv_window = min(self.recv_window + bytes_processed, self.max_window)
        logging.info(f"Restored receive window: {self.recv_window} bytes")
