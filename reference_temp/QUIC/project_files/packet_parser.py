import struct
import logging
from constants import QUIC_LONG_HEADER, QUIC_SHORT_HEADER

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QUICPacketParser:
    @staticmethod
    def parse_packet(data):
        if len(data) < 1:
            logging.warning("Received empty packet")
            return None
        
        first_byte = data[0]
        header_form = (first_byte & 0x80) >> 7  # 1 = Long Header, 0 = Short Header
        packet_type = (first_byte & 0x30) >> 4  # Extracting packet type (if long header)
        
        logging.info(f"Header Form: {'Long' if header_form else 'Short'} Header")
        
        if header_form:  # Long header processing
            if len(data) < 6:
                logging.warning("Insufficient data for a valid QUIC long header packet")
                return None
            version = struct.unpack("!I", data[1:5])[0]
            dcid_length = data[5]
            if len(data) < 6 + dcid_length:
                logging.warning("Insufficient data for connection ID")
                return None
            dcid = data[6:6 + dcid_length].hex()
            logging.info(f"QUIC Version: {version}, DCID: {dcid}")
            return {
                "header_form": QUIC_LONG_HEADER,
                "packet_type": packet_type,
                "version": version,
                "dcid": dcid
            }
        else:  # Short header processing
            dcid = data[1:].hex()
            logging.info(f"Short header packet received, DCID: {dcid}")
            return {
                "header_form": QUIC_SHORT_HEADER,
                "dcid": dcid
            }

if __name__ == "__main__":
    sample_data = b'\xc3\x00\x00\x00\x01\x08abcdefgh'  # Example long header packet
    parsed_packet = QUICPacketParser.parse_packet(sample_data)
    logging.info(f"Parsed Packet: {parsed_packet}")
