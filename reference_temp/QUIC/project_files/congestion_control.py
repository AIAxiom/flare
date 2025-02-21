import logging

class CongestionControl:
    def __init__(self, initial_window=10, min_window=2, loss_reduction_factor=0.5):
        self.cwnd = initial_window  # Congestion window size (packets)
        self.ssthresh = float('inf')  # Slow start threshold
        self.min_window = min_window  # Minimum congestion window size
        self.loss_reduction_factor = loss_reduction_factor  # Factor to reduce window on loss
        logging.info("Congestion Control initialized")
    
    def on_packet_acked(self, acked_packets):
        """Adjusts congestion window on successful packet acknowledgments."""
        for _ in acked_packets:
            if self.cwnd < self.ssthresh:
                self.cwnd += 1  # Slow start phase
            else:
                self.cwnd += 1 / self.cwnd  # Congestion avoidance phase
        logging.info(f"Congestion window updated: {self.cwnd}")
    
    def on_packet_lost(self):
        """Handles congestion window reduction on packet loss."""
        self.ssthresh = max(self.cwnd * self.loss_reduction_factor, self.min_window)
        self.cwnd = max(self.min_window, self.ssthresh)
        logging.warning(f"Packet loss detected! New cwnd: {self.cwnd}, ssthresh: {self.ssthresh}")
    
    def can_send(self):
        """Checks if congestion window allows sending more packets."""
        return self.cwnd > 0
