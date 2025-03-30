import struct
from .control_packet import ControlPacket
from .data_packet import DataPacket

class FlarePacket:
    HEADER_FORMAT = "!BBHI"
    HEADER_SIZE = struct.calcsize(HEADER_FORMAT)

    def __init__(self, version, packet_type, conn_id, packet_id, packet_obj):
        self.version = version
        self.packet_type = packet_type
        self.conn_id = conn_id
        self.packet_id = packet_id
        self.packet_obj = packet_obj

    def encode(self):
        header = struct.pack(self.HEADER_FORMAT, self.version, self.packet_type, self.conn_id, self.packet_id)
        return header + self.packet_obj.encode()

    @classmethod
    def decode(cls, data):
        header = data[:cls.HEADER_SIZE]
        version, packet_type, conn_id, packet_id = struct.unpack(cls.HEADER_FORMAT, header)
        payload = data[cls.HEADER_SIZE:]

        if packet_type == ControlPacket.CONTROL_PACKET:
            packet_obj = ControlPacket.decode(payload)
        elif packet_type == DataPacket.DATA_PACKET:
            packet_obj = DataPacket.decode(payload)
        else:
            raise ValueError("Unknown packet type")

        return cls(version, packet_type, conn_id, packet_id, packet_obj)

# Example Usage
if __name__ == "__main__":
    # Example: Creating and encoding a control packet
    control_packet = ControlPacket(control_type=0x01, payload=b"ACK")
    flare_control = FlarePacket(version=1, packet_type=ControlPacket.CONTROL_PACKET, conn_id=100, packet_id=1, packet_obj=control_packet)
    encoded_control = flare_control.encode()
    print("Decoded Control Packet:", encoded_control.hex())
    decoded_control = FlarePacket.decode(encoded_control)
    print("Decoded Control Packet:", decoded_control.packet_obj.control_type, decoded_control.packet_obj.payload)

    # Example: Creating and encoding a fragmented large data packet
    large_payload = b"X" * 5000  # Simulating large binary data
    chunk_size = 1024
    fragments = []

    for i in range(0, len(large_payload), chunk_size):
        chunk = large_payload[i:i + chunk_size]
        data_packet = DataPacket(total_length=len(large_payload), chunk_offset=i, payload=chunk)
        flare_data = FlarePacket(version=1, packet_type=DataPacket.DATA_PACKET, conn_id=200, packet_id=i // chunk_size, packet_obj=data_packet)
        fragments.append(flare_data.encode())

    # Example: Decoding and reassembling data packets
    reassembled_data = bytearray()
    for fragment in fragments:
        print("Before decoding : ", fragment.hex())
        decoded_fragment = FlarePacket.decode(fragment)
        reassembled_data[decoded_fragment.packet_obj.chunk_offset:decoded_fragment.packet_obj.chunk_offset + len(decoded_fragment.packet_obj.payload)] = decoded_fragment.packet_obj.payload

    print("Reassembled Data Size:", len(reassembled_data))
