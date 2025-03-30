from ..constants import *


class ControlPacket:

    def __init__(self, control_type, total_length=0, chunk_offset=0, payload=b""):
        self.control_type = control_type
        self.total_length = total_length  # Total length of the full control payload
        self.chunk_offset = chunk_offset  # Offset of this fragment
        self.payload = payload  # Actual payload fragment

    def encode(self):
        header = struct.pack(CONTROL_HEADER_FORMAT, self.control_type, self.total_length, self.chunk_offset)
        return header + self.payload

    @classmethod
    def decode(cls, data):
        control_type, total_length, chunk_offset = struct.unpack(CONTROL_HEADER_FORMAT,
                                                                 data[:CONTROL_HEADER_SIZE])
        payload = data[CONTROL_HEADER_SIZE:]
        return cls(control_type, total_length, chunk_offset, payload)


# Example Usage
if __name__ == "__main__":
    # Example: Creating and encoding a control packet
    control_packet = ControlPacket(control_type=0x01, total_length=5000, chunk_offset=0, payload=b"ACK")
    encoded_control = control_packet.encode()
    decoded_control = ControlPacket.decode(encoded_control)
    print("Decoded Control Packet:", decoded_control.control_type, decoded_control.total_length,
          decoded_control.chunk_offset, decoded_control.payload)

    # Example: Creating and encoding a fragmented large control packet
    large_control_payload = b"C" * 5000  # Simulating large control binary data
    chunk_size = 1024
    fragments = []

    for i in range(0, len(large_control_payload), chunk_size):
        chunk = large_control_payload[i:i + chunk_size]
        control_fragment = ControlPacket(control_type=0x01, total_length=len(large_control_payload), chunk_offset=i,
                                         payload=chunk)
        fragments.append(control_fragment.encode())

    # Example: Decoding and reassembling control packets
    reassembled_control_data = bytearray(len(large_control_payload))
    for fragment in fragments:
        decoded_fragment = ControlPacket.decode(fragment)
        reassembled_control_data[decoded_fragment.chunk_offset:decoded_fragment.chunk_offset + len(
            decoded_fragment.payload)] = decoded_fragment.payload

    print("Reassembled Control Data Size:", len(reassembled_control_data))
