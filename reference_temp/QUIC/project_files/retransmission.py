import logging
import time

class RetransmissionHandler:
    def __init__(self, timeout=3.0):
        self.sent_packets = {}  # Stores sent packets with timestamps
        self.timeout = timeout  # Retransmission timeout in seconds
        logging.info("Retransmission Handler initialized")

    def track_packet(self, packet_number, packet_data, timestamp=None):
        """Tracks a sent packet for potential retransmission."""
        if timestamp is None:
            timestamp = time.time()
        self.sent_packets[packet_number] = (packet_data, timestamp)
        logging.info(f"Packet {packet_number} tracked for retransmission")

    def check_for_retransmission(self, current_time=None):
        """Checks for packets that need retransmission."""
        if current_time is None:
            current_time = time.time()
        
        retransmit_list = []
        for packet_number, (packet_data, timestamp) in list(self.sent_packets.items()):
            if current_time - timestamp >= self.timeout:
                retransmit_list.append((packet_number, packet_data))
                logging.warning(f"Retransmitting packet {packet_number}")
                del self.sent_packets[packet_number]
        
        return retransmit_list

    def acknowledge_packet(self, packet_number):
        """Removes acknowledged packets from tracking."""
        if packet_number in self.sent_packets:
            del self.sent_packets[packet_number]
            logging.info(f"Packet {packet_number} acknowledged and removed from tracking")
