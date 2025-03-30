from ..constants import *


class DataPacket:

    def __init__(self, total_length, chunk_offset, payload=b""):
        self.total_length = total_length
        self.chunk_offset = chunk_offset
        self.payload = payload

    def encode(self):
        return struct.pack(DATA_HEADER_FORMAT, self.total_length, self.chunk_offset) + self.payload

    @classmethod
    def decode(cls, data):
        total_length, chunk_offset = struct.unpack(DATA_HEADER_FORMAT, data[:DATA_HEADER_SIZE])
        payload = data[DATA_HEADER_SIZE:]
        return cls(total_length, chunk_offset, payload)


# Example Usage
if __name__ == "__main__":
    # Create a data packet
    data_packet = DataPacket(total_length=1024, chunk_offset=0, payload=b"Hello, World!")
    encoded_data = data_packet.encode()

    # Decode the data packet
    decoded_data = DataPacket.decode(encoded_data)
    print("Decoded Data Packet:", decoded_data.total_length, decoded_data.chunk_offset, decoded_data.payload)
