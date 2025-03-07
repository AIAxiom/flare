# Packet Documentation

Packet Composition:
- Header
- Data

## Header 

> 1 Byte : ABCDEFGH

- `A` : Packet Type
  - `CONTROL` : `0`
  - `DATA` : `1`

### For control packets
- `B` : `ACK`
- `C` : `HANDSHAKE`
- `D` : 

### For Data packets

- `BC` : Stream Id
- `DEFGH` : Packet Sequence Numbers