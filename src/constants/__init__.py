import struct

# Flare packet constants
HEADER_FORMAT = "!BBHI"
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)

# Control packet constants
CONTROL_PACKET = 0x01
CONTROL_HEADER_FORMAT = "!B I I"  # Merged control_type, total_length, chunk_offset
CONTROL_HEADER_SIZE = struct.calcsize(CONTROL_HEADER_FORMAT)

# Data packet constants
DATA_HEADER_FORMAT = "!HI"
DATA_HEADER_SIZE = struct.calcsize(DATA_HEADER_FORMAT)
DATA_PACKET = 0x02
