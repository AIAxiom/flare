# QUIC-Like Packet Structure for UDP Transport

## Packet Types

1. **Control Packet**: Used for session management, acknowledgments, and signaling.
2. **Data Packet**: Used for transmitting user payloads.

## Packet Header Structure

### Common Header (8 bytes)

| Field     | Size (bytes) | Description                                           |
| --------- | ------------ | ----------------------------------------------------- |
| Version   | 1            | Protocol version                                      |
| Type      | 1            | Packet type: `0x01` for Control, `0x02` for Data      |
| Conn ID   | 2            | Connection identifier (randomly assigned per session) |
| Packet ID | 4            | Unique packet identifier (incremental)                |

### Control Packet Structure (Variable Length)

| Field        | Size (bytes) | Description                                                |
| ------------ | ------------ | ---------------------------------------------------------- |
| Control Type | 1            | Subtype of the control packet (e.g., ACK, Handshake, etc.) |
| Total Length | 4            | Total length of the full control payload                   |
| Chunk Offset | 4            | Offset of this fragment within the total payload           |
| Payload      | Variable     | Control message payload                                    |

### Data Packet Structure

| Field        | Size (bytes) | Description                                            |
| ------------ | ------------ | ------------------------------------------------------ |
| Total Length | 2            | Total size of the original data (before fragmentation) |
| Chunk Offset | 4            | Offset of this chunk within the total data             |
| Chunk Data   | Variable     | Fragmented payload data                                |

## Fragmentation and Reassembly

- Large binary data is split into multiple packets, each containing a chunk.
- The **Total Length** field allows the receiver to determine when the full payload has been received.
- The **Chunk Offset** field ensures proper reassembly.

## Error Handling

- Each packet should be verified for integrity using its **Packet ID**.
- If a packet is missing, the receiver requests retransmission using a **Control Packet (ACK with NACK info)**.

## Notes:
- Retransmission not implemented. 
- Connection id and packet id needs to be implemented. 
- Clearing buffer after successful transmission pending. 
- More control packet types needs to be implemented. 