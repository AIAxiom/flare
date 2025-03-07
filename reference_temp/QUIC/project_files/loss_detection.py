import logging
import time

class LossDetection:
    def __init__(self, reordering_threshold=3, pto_multiplier=1.25):
        self.sent_packets = {}  # Stores packet timestamps
        self.acknowledged_packets = set()
        self.reordering_threshold = reordering_threshold  # Threshold for detecting reordering
        self.pto_multiplier = pto_multiplier  # Probe timeout multiplier
        logging.info("Loss Detection initialized")
    
    def track_packet(self, packet_number, timestamp=None):
        """Tracks a sent packet for loss detection."""
        if timestamp is None:
            timestamp = time.time()
        self.sent_packets[packet_number] = timestamp
        logging.info(f"Packet {packet_number} tracked for loss detection")
    
    def detect_lost_packets(self, largest_acked, current_time=None):
        """Detects lost packets based on reordering threshold and timeouts."""
        if current_time is None:
            current_time = time.time()
        
        lost_packets = []
        for packet_number, sent_time in list(self.sent_packets.items()):
            if packet_number < largest_acked - self.reordering_threshold:
                lost_packets.append(packet_number)
                del self.sent_packets[packet_number]
                logging.warning(f"Packet {packet_number} detected as lost (reordering threshold)")
            elif current_time - sent_time > self.pto_multiplier * (current_time - min(self.sent_packets.values(), default=current_time)):
                lost_packets.append(packet_number)
                del self.sent_packets[packet_number]
                logging.warning(f"Packet {packet_number} detected as lost (timeout)")
        
        return lost_packets
    
    def acknowledge_packet(self, packet_number):
        """Marks a packet as acknowledged."""
        if packet_number in self.sent_packets:
            del self.sent_packets[packet_number]
            self.acknowledged_packets.add(packet_number)
            logging.info(f"Packet {packet_number} acknowledged and removed from tracking")
