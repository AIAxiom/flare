# Protocol Specification: FLARE (Fast Local App Relay & Exchange)

> Version : 0.0.0-ALPHA

## 1. Introduction

FLARE is a custom UDP-based protocol designed for efficient local inter-application communication. It aims to provide a lightweight, low-latency, and reliable mechanism for data exchange between applications running on the same machine or local network.

## 2. Terminology & Definitions

- **Connection**: A bidirectional communication channel between two endpoints.
- **Stream**: An independent, ordered sequence of bytes within a connection.
- **Packet**: A unit of data transmitted over UDP, containing FLARE frames.
- **Frame**: The smallest unit of data in FLARE, carrying control or application data.
- **Handshake**: The initial exchange of packets to establish security and session parameters.
- **Congestion Control**: Mechanism to prevent network congestion by regulating data flow.

## 3. Protocol Overview

FLARE provides the following key features:

- **Connection Establishment**: Faster than TCP using a combined transport and cryptographic handshake.
- **Multiplexed Streams**: Multiple independent streams in a single connection without head-of-line blocking.
- **Reliable Delivery**: Built-in acknowledgments and retransmission for reliability.
- **Security**: Uses encryption and authentication mechanisms.
- **Congestion & Flow Control**: Dynamic adaptation to network conditions.

## 4. Packet Structure

Refer [here](/src/constants/packet.md)

## 5. State Machine

### 5.1 Connection Establishment

1. **ClientHello** → Client sends an Initial packet with handshake data.
2. **ServerHello** → Server responds with handshake messages and cryptographic parameters.
3. **Handshake Completion** → Both parties finalize keys and start encrypted communication.

### 5.2 Data Transfer

1. **STREAM Frame** → Application data sent within streams.
2. **ACK Frame** → Acknowledgments sent for received packets.
3. **Retransmission** (if packet loss detected).

### 5.3 Connection Termination

1. **CONNECTION_CLOSE Frame** → Initiates graceful shutdown.
2. **Final ACK** → Confirms connection closure.

## 6. Error Handling

- **Packet Loss Detection & Retransmission**
- **Flow & Congestion Control**
- **Stateless Reset for Unexpected Termination**

## 7. Security Considerations

- **End-to-End Encryption**
- **Protection Against Replay & Man-in-the-Middle Attacks**
- **Forward Secrecy & Authentication**

## 8. Implementation Considerations

- Optimize packet scheduling for low latency.
- Implement adaptive congestion control.
- Efficient memory management for stream multiplexing.


Note : Project still in design state. 