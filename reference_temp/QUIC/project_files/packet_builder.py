import struct
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PacketBuilder:
    @staticmethod
    def build_initial_response(dcid):
        version = 1  # Example QUIC version
        scid = b'\x01\x02\x03\x04\x05\x06\x07\x08'  # Example Server Connection ID
        payload = b'QUIC Initial Response'
        
        response_packet = struct.pack("!B I", 0xC1, version) + scid + bytes.fromhex(dcid) + payload
        logging.info(f"Built Initial Response Packet: {response_packet.hex()}")
        return response_packet
    
    @staticmethod
    def build_handshake_response(dcid):
        version = 1  # Example QUIC version
        scid = b'\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10'  # Example Server Connection ID for handshake
        payload = b'QUIC Handshake Response'
        
        response_packet = struct.pack("!B I", 0xC2, version) + scid + bytes.fromhex(dcid) + payload
        logging.info(f"Built Handshake Response Packet: {response_packet.hex()}")
        return response_packet
    
    @staticmethod
    def build_short_header_ack(dcid):
        version = 1  # Example QUIC version
        ack_frame = b'ACK'  # Simplified ACK response
        
        response_packet = struct.pack("!B I", 0x43, version) + bytes.fromhex(dcid) + ack_frame
        logging.info(f"Built Short Header ACK Packet: {response_packet.hex()}")
        return response_packet

if __name__ == "__main__":
    builder = PacketBuilder()
    sample_dcid = "abcdef1234567890"
    initial_response = builder.build_initial_response(sample_dcid)
    print("Initial Response:", initial_response.hex())
    handshake_response = builder.build_handshake_response(sample_dcid)
    print("Handshake Response:", handshake_response.hex())
    short_ack = builder.build_short_header_ack(sample_dcid)
    print("Short Header ACK:", short_ack.hex())