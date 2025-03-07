# Packet types

# Header size : 1 Byte
#


from enum import  Enum

class PacketType(Enum):
    CONTROL = 0
    DATA = 1

class ControlPacketFlags(Enum):
    ACK = 0
    HANDSHAKE = 1