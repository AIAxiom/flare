# import logging
# from connection_manager import ConnectionManager
# from handshake import QUICHandshake
# from flow_control import FlowControl

# class PacketHandler:
#     def __init__(self, connection_manager):
#         self.connection_manager = connection_manager
#         self.handshake = QUICHandshake(connection_manager)
#         logging.info("Packet Handler initialized")

#     def process_packet(self, data, address):
#         logging.info(f"Processing packet from {address}: {data.hex()}")
#         packet_type = data[0]
#         dcid = data[1:9].hex() if len(data) > 8 else None
        
#         if packet_type == 0xC3:  # Initial Packet
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Existing connection found for DCID {dcid}")
#             else:
#                 logging.info(f"No existing connection, creating new one")
#                 connection = self.connection_manager.create_connection(dcid, "generated_scid", address)
#                 connection.flow_control = FlowControl()
#                 logging.info("Flow control initialized for new connection")
        
#         elif packet_type == 0xC1:  # Handshake Packet
#             logging.info("Received Handshake Packet")
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Processing handshake for connection {dcid}")
#                 self.handshake.process_client_hello(dcid, "generated_scid", address, data[9:])
        
#         elif packet_type & 0x40 == 0x40:  # Short Header Packet
#             logging.info(f"Received Short Header Packet for DCID {dcid}")
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Processing Short Header Packet for {dcid}")
#                 # Simulate flow control updates
#                 connection.update_flow_control(bytes_received=len(data))
#                 logging.info(f"Flow control updated for {dcid}")
                
#         else:
#             logging.warning("Unknown packet type received")


# import logging
# from connection_manager import ConnectionManager
# from handshake import QUICHandshake
# from flow_control import FlowControl
# from retransmission import RetransmissionHandler
# from loss_detection import LossDetection
# from congestion_control import CongestionControl

# class PacketHandler:
#     def __init__(self, connection_manager):
#         self.connection_manager = connection_manager
#         self.handshake = QUICHandshake(connection_manager)
#         self.retransmission_handler = RetransmissionHandler()
#         self.loss_detection = LossDetection()
#         self.congestion_control = CongestionControl()
#         logging.info("Packet Handler initialized")

#     def process_packet(self, data, address):
#         logging.info(f"Processing packet from {address}: {data.hex()}")
#         packet_type = data[0]
#         dcid = data[1:9].hex() if len(data) > 8 else None
        
#         if packet_type == 0xC3:  # Initial Packet
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Existing connection found for DCID {dcid}")
#             else:
#                 logging.info(f"No existing connection, creating new one")
#                 connection = self.connection_manager.create_connection(dcid, "generated_scid", address)
#                 connection.flow_control = FlowControl()
#                 logging.info("Flow control initialized for new connection")
        
#         elif packet_type == 0xC1:  # Handshake Packet
#             logging.info("Received Handshake Packet")
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Processing handshake for connection {dcid}")
#                 self.handshake.process_client_hello(dcid, "generated_scid", address, data[9:])
        
#         elif packet_type & 0x40 == 0x40:  # Short Header Packet
#             logging.info(f"Received Short Header Packet for DCID {dcid}")
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Processing Short Header Packet for {dcid}")
#                 connection.update_flow_control(bytes_received=len(data))
#                 self.retransmission_handler.track_packet(len(data), data)
#                 lost_packets = self.loss_detection.detect_lost_packets(len(data))
#                 for pkt in lost_packets:
#                     self.retransmission_handler.track_packet(pkt, data)
#                     logging.warning(f"Retransmitting lost packet {pkt}")
#                 logging.info(f"Flow control updated for {dcid}")
                
#                 if self.congestion_control.can_send():
#                     logging.info("Congestion control allows sending more packets")
#                 else:
#                     logging.warning("Congestion window is full, delaying transmission")
        
#         else:
#             logging.warning("Unknown packet type received")


# import logging
# from connection_manager import ConnectionManager
# from handshake import QUICHandshake
# from flow_control import FlowControl
# from retransmission import RetransmissionHandler
# from loss_detection import LossDetection
# from congestion_control import CongestionControl
# from stream_manager import StreamManager
# from stream_prioritization import StreamPriorityQueue

# class PacketHandler:
#     def __init__(self, connection_manager):
#         self.connection_manager = connection_manager
#         self.handshake = QUICHandshake(connection_manager)
#         self.retransmission_handler = RetransmissionHandler()
#         self.loss_detection = LossDetection()
#         self.congestion_control = CongestionControl()
#         self.stream_manager = StreamManager()
#         self.stream_priority_queue = StreamPriorityQueue()
#         logging.info("Packet Handler initialized")

#     def process_packet(self, data, address):
#         logging.info(f"Processing packet from {address}: {data.hex()}")
#         packet_type = data[0]
#         dcid = data[1:9].hex() if len(data) > 8 else None
        
#         if packet_type == 0xC3:  # Initial Packet
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Existing connection found for DCID {dcid}")
#             else:
#                 logging.info(f"No existing connection, creating new one")
#                 connection = self.connection_manager.create_connection(dcid, "generated_scid", address)
#                 connection.flow_control = FlowControl()
#                 logging.info("Flow control initialized for new connection")
        
#         elif packet_type == 0xC1:  # Handshake Packet
#             logging.info("Received Handshake Packet")
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Processing handshake for connection {dcid}")
#                 self.handshake.process_client_hello(dcid, "generated_scid", address, data[9:])
        
#         elif packet_type & 0x40 == 0x40:  # Short Header Packet
#             logging.info(f"Received Short Header Packet for DCID {dcid}")
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Processing Short Header Packet for {dcid}")
#                 connection.update_flow_control(bytes_received=len(data))
#                 self.retransmission_handler.track_packet(len(data), data)
#                 lost_packets = self.loss_detection.detect_lost_packets(len(data))
#                 for pkt in lost_packets:
#                     self.retransmission_handler.track_packet(pkt, data)
#                     logging.warning(f"Retransmitting lost packet {pkt}")
#                 logging.info(f"Flow control updated for {dcid}")
                
#                 if self.congestion_control.can_send():
#                     logging.info("Congestion control allows sending more packets")
#                 else:
#                     logging.warning("Congestion window is full, delaying transmission")
                
#                 # Stream Handling
#                 stream_id = int.from_bytes(data[9:13], 'big') if len(data) > 12 else None
#                 if stream_id is not None:
#                     stream = self.stream_manager.create_stream(stream_id, connection)
#                     stream.write(data[13:])
#                     self.stream_priority_queue.add_stream(stream_id, priority=0)  # Default priority
#                     logging.info(f"Stream {stream_id} processed and added to priority queue")
                
#         else:
#             logging.warning("Unknown packet type received")

# import logging
# from connection_manager import ConnectionManager
# from handshake import QUICHandshake
# from flow_control import FlowControl
# from retransmission import RetransmissionHandler
# from loss_detection import LossDetection
# from congestion_control import CongestionControl
# from stream_manager import StreamManager
# from stream_prioritization import StreamPriorityQueue
# from connection_migration import ConnectionMigration
# from stateless_reset import StatelessReset

# class PacketHandler:
#     def __init__(self, connection_manager):
#         self.connection_manager = connection_manager
#         self.handshake = QUICHandshake(connection_manager)
#         self.retransmission_handler = RetransmissionHandler()
#         self.loss_detection = LossDetection()
#         self.congestion_control = CongestionControl()
#         self.stream_manager = StreamManager()
#         self.stream_priority_queue = StreamPriorityQueue()
#         self.connection_migration = ConnectionMigration(connection_manager)
#         self.stateless_reset = StatelessReset(connection_manager)
#         logging.info("Packet Handler initialized")

#     def process_packet(self, data, address):
#         logging.info(f"Processing packet from {address}: {data.hex()}")
#         packet_type = data[0]
#         dcid = data[1:9].hex() if len(data) > 8 else None
        
#         if packet_type == 0xC3:  # Initial Packet
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Existing connection found for DCID {dcid}")
#             else:
#                 logging.info(f"No existing connection, creating new one")
#                 connection = self.connection_manager.create_connection(dcid, "generated_scid", address)
#                 connection.flow_control = FlowControl()
#                 logging.info("Flow control initialized for new connection")
        
#         elif packet_type == 0xC1:  # Handshake Packet
#             logging.info("Received Handshake Packet")
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Processing handshake for connection {dcid}")
#                 self.handshake.process_client_hello(dcid, "generated_scid", address, data[9:])
        
#         elif packet_type & 0x40 == 0x40:  # Short Header Packet
#             logging.info(f"Received Short Header Packet for DCID {dcid}")
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Processing Short Header Packet for {dcid}")
#                 connection.update_flow_control(bytes_received=len(data))
#                 self.retransmission_handler.track_packet(len(data), data)
#                 lost_packets = self.loss_detection.detect_lost_packets(len(data))
#                 for pkt in lost_packets:
#                     self.retransmission_handler.track_packet(pkt, data)
#                     logging.warning(f"Retransmitting lost packet {pkt}")
#                 logging.info(f"Flow control updated for {dcid}")
                
#                 if self.congestion_control.can_send():
#                     logging.info("Congestion control allows sending more packets")
#                 else:
#                     logging.warning("Congestion window is full, delaying transmission")
                
#                 # Stream Handling
#                 stream_id = int.from_bytes(data[9:13], 'big') if len(data) > 12 else None
#                 if stream_id is not None:
#                     stream = self.stream_manager.create_stream(stream_id, connection)
#                     stream.write(data[13:])
#                     self.stream_priority_queue.add_stream(stream_id, priority=0)  # Default priority
#                     logging.info(f"Stream {stream_id} processed and added to priority queue")
                
#                 # Detect Connection Migration
#                 if self.connection_migration.detect_migration(connection, address):
#                     logging.info(f"Connection {dcid} migrated to new address {address}")
                
#         elif packet_type == 0xC0:  # Stateless Reset Packet
#             received_token = data[1:17] if len(data) > 16 else None
#             if received_token:
#                 if self.stateless_reset.handle_reset(received_token, address):
#                     logging.info(f"Stateless reset handled for {address}")
        
#         else:
#             logging.warning("Unknown packet type received")


# import logging
# from connection_manager import ConnectionManager
# from handshake import QUICHandshake
# from flow_control import FlowControl
# from retransmission import RetransmissionHandler
# from loss_detection import LossDetection
# from congestion_control import CongestionControl
# from stream_manager import StreamManager
# from stream_prioritization import StreamPriorityQueue
# from connection_migration import ConnectionMigration
# from stateless_reset import StatelessReset
# from key_management import KeyManagement
# from connection_close import ConnectionClose

# class PacketHandler:
#     def __init__(self, connection_manager):
#         self.connection_manager = connection_manager
#         self.handshake = QUICHandshake(connection_manager)
#         self.retransmission_handler = RetransmissionHandler()
#         self.loss_detection = LossDetection()
#         self.congestion_control = CongestionControl()
#         self.stream_manager = StreamManager()
#         self.stream_priority_queue = StreamPriorityQueue()
#         self.connection_migration = ConnectionMigration(connection_manager)
#         self.stateless_reset = StatelessReset(connection_manager)
#         self.key_management = KeyManagement()
#         self.connection_close = ConnectionClose(connection_manager)
#         logging.info("Packet Handler initialized")

#     def process_packet(self, data, address):
#         logging.info(f"Processing packet from {address}: {data.hex()}")
#         packet_type = data[0]
#         dcid = data[1:9].hex() if len(data) > 8 else None
        
#         if packet_type == 0xC3:  # Initial Packet
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Existing connection found for DCID {dcid}")
#             else:
#                 logging.info(f"No existing connection, creating new one")
#                 connection = self.connection_manager.create_connection(dcid, "generated_scid", address)
#                 connection.flow_control = FlowControl()
#                 self.key_management.generate_initial_keys(dcid)
#                 logging.info("Flow control and key management initialized for new connection")
        
#         elif packet_type == 0xC1:  # Handshake Packet
#             logging.info("Received Handshake Packet")
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Processing handshake for connection {dcid}")
#                 self.handshake.process_client_hello(dcid, "generated_scid", address, data[9:])
        
#         elif packet_type & 0x40 == 0x40:  # Short Header Packet
#             logging.info(f"Received Short Header Packet for DCID {dcid}")
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Processing Short Header Packet for {dcid}")
#                 connection.update_flow_control(bytes_received=len(data))
#                 self.retransmission_handler.track_packet(len(data), data)
#                 lost_packets = self.loss_detection.detect_lost_packets(len(data))
#                 for pkt in lost_packets:
#                     self.retransmission_handler.track_packet(pkt, data)
#                     logging.warning(f"Retransmitting lost packet {pkt}")
#                 logging.info(f"Flow control updated for {dcid}")
                
#                 if self.congestion_control.can_send():
#                     logging.info("Congestion control allows sending more packets")
#                 else:
#                     logging.warning("Congestion window is full, delaying transmission")
                
#                 # Stream Handling
#                 stream_id = int.from_bytes(data[9:13], 'big') if len(data) > 12 else None
#                 if stream_id is not None:
#                     stream = self.stream_manager.create_stream(stream_id, connection)
#                     stream.write(data[13:])
#                     self.stream_priority_queue.add_stream(stream_id, priority=0)  # Default priority
#                     logging.info(f"Stream {stream_id} processed and added to priority queue")
                
#                 # Detect Connection Migration
#                 if self.connection_migration.detect_migration(connection, address):
#                     logging.info(f"Connection {dcid} migrated to new address {address}")
                
#         elif packet_type == 0xC0:  # Stateless Reset Packet
#             received_token = data[1:17] if len(data) > 16 else None
#             if received_token:
#                 if self.stateless_reset.handle_reset(received_token, address):
#                     logging.info(f"Stateless reset handled for {address}")
        
#         elif packet_type == 0xC2:  # Connection Close Packet
#             logging.info(f"Received CONNECTION_CLOSE frame for DCID {dcid}")
#             frame = {"type": "CONNECTION_CLOSE", "error_code": 0, "reason": "Normal closure"}  # Placeholder
#             self.connection_close.handle_close_frame(dcid, frame)
        
#         else:
#             logging.warning("Unknown packet type received")


# import logging
# from connection_manager import ConnectionManager
# from handshake import QUICHandshake
# from flow_control import FlowControl
# from retransmission import RetransmissionHandler
# from loss_detection import LossDetection
# from congestion_control import CongestionControl
# from stream_manager import StreamManager
# from stream_prioritization import StreamPriorityQueue
# from connection_migration import ConnectionMigration
# from stateless_reset import StatelessReset
# from key_management import KeyManagement
# from connection_close import ConnectionClose
# from session_resumption import SessionResumption
# from zero_rtt import ZeroRTT

# class PacketHandler:
#     def __init__(self, connection_manager):
#         self.connection_manager = connection_manager
#         self.handshake = QUICHandshake(connection_manager)
#         self.retransmission_handler = RetransmissionHandler()
#         self.loss_detection = LossDetection()
#         self.congestion_control = CongestionControl()
#         self.stream_manager = StreamManager()
#         self.stream_priority_queue = StreamPriorityQueue()
#         self.connection_migration = ConnectionMigration(connection_manager)
#         self.stateless_reset = StatelessReset(connection_manager)
#         self.key_management = KeyManagement()
#         self.connection_close = ConnectionClose(connection_manager)
#         self.session_resumption = SessionResumption()
#         self.zero_rtt = ZeroRTT()
#         logging.info("Packet Handler initialized")

#     def process_packet(self, data, address):
#         logging.info(f"Processing packet from {address}: {data.hex()}")
#         packet_type = data[0]
#         dcid = data[1:9].hex() if len(data) > 8 else None
        
#         if packet_type == 0xC3:  # Initial Packet
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Existing connection found for DCID {dcid}")
#             else:
#                 logging.info(f"No existing connection, creating new one")
#                 connection = self.connection_manager.create_connection(dcid, "generated_scid", address)
#                 connection.flow_control = FlowControl()
#                 self.key_management.generate_initial_keys(dcid)
#                 self.session_resumption.generate_session_ticket(dcid)
#                 logging.info("Flow control, key management, and session resumption initialized for new connection")
        
#         elif packet_type == 0xC1:  # Handshake Packet
#             logging.info("Received Handshake Packet")
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Processing handshake for connection {dcid}")
#                 self.handshake.process_client_hello(dcid, "generated_scid", address, data[9:])
        
#         elif packet_type & 0x40 == 0x40:  # Short Header Packet
#             logging.info(f"Received Short Header Packet for DCID {dcid}")
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Processing Short Header Packet for {dcid}")
#                 connection.update_flow_control(bytes_received=len(data))
#                 self.retransmission_handler.track_packet(len(data), data)
#                 lost_packets = self.loss_detection.detect_lost_packets(len(data))
#                 for pkt in lost_packets:
#                     self.retransmission_handler.track_packet(pkt, data)
#                     logging.warning(f"Retransmitting lost packet {pkt}")
#                 logging.info(f"Flow control updated for {dcid}")
                
#                 if self.congestion_control.can_send():
#                     logging.info("Congestion control allows sending more packets")
#                 else:
#                     logging.warning("Congestion window is full, delaying transmission")
                
#                 # Stream Handling
#                 stream_id = int.from_bytes(data[9:13], 'big') if len(data) > 12 else None
#                 if stream_id is not None:
#                     stream = self.stream_manager.create_stream(stream_id, connection)
#                     stream.write(data[13:])
#                     self.stream_priority_queue.add_stream(stream_id, priority=0)  # Default priority
#                     logging.info(f"Stream {stream_id} processed and added to priority queue")
                
#                 # Detect Connection Migration
#                 if self.connection_migration.detect_migration(connection, address):
#                     logging.info(f"Connection {dcid} migrated to new address {address}")
                
#                 # Handle 0-RTT Data
#                 if connection.is_early_data_allowed():
#                     decrypted_data = self.zero_rtt.decrypt_early_data(dcid, data[13:])
#                     if decrypted_data:
#                         logging.info(f"Processed 0-RTT data for {dcid}: {decrypted_data}")
        
#         elif packet_type == 0xC0:  # Stateless Reset Packet
#             received_token = data[1:17] if len(data) > 16 else None
#             if received_token:
#                 if self.stateless_reset.handle_reset(received_token, address):
#                     logging.info(f"Stateless reset handled for {address}")
        
#         elif packet_type == 0xC2:  # Connection Close Packet
#             logging.info(f"Received CONNECTION_CLOSE frame for DCID {dcid}")
#             frame = {"type": "CONNECTION_CLOSE", "error_code": 0, "reason": "Normal closure"}  # Placeholder
#             self.connection_close.handle_close_frame(dcid, frame)
        
#         else:
#             logging.warning("Unknown packet type received")


# import logging
# from connection_manager import ConnectionManager
# from handshake import QUICHandshake
# from flow_control import FlowControl
# from retransmission import RetransmissionHandler
# from loss_detection import LossDetection
# from congestion_control import CongestionControl
# from stream_manager import StreamManager
# from stream_prioritization import StreamPriorityQueue
# from connection_migration import ConnectionMigration
# from stateless_reset import StatelessReset
# from key_management import KeyManagement
# from connection_close import ConnectionClose
# from session_resumption import SessionResumption
# from zero_rtt import ZeroRTT
# from key_update import KeyUpdate

# class PacketHandler:
#     def __init__(self, connection_manager):
#         self.connection_manager = connection_manager
#         self.handshake = QUICHandshake(connection_manager)
#         self.retransmission_handler = RetransmissionHandler()
#         self.loss_detection = LossDetection()
#         self.congestion_control = CongestionControl()
#         self.stream_manager = StreamManager()
#         self.stream_priority_queue = StreamPriorityQueue()
#         self.connection_migration = ConnectionMigration(connection_manager)
#         self.stateless_reset = StatelessReset(connection_manager)
#         self.key_management = KeyManagement()
#         self.connection_close = ConnectionClose(connection_manager)
#         self.session_resumption = SessionResumption()
#         self.zero_rtt = ZeroRTT()
#         self.key_update = KeyUpdate()
#         logging.info("Packet Handler initialized")

#     def process_packet(self, data, address):
#         logging.info(f"Processing packet from {address}: {data.hex()}")
#         packet_type = data[0]
#         dcid = data[1:9].hex() if len(data) > 8 else None
        
#         if packet_type == 0xC3:  # Initial Packet
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Existing connection found for DCID {dcid}")
#             else:
#                 logging.info(f"No existing connection, creating new one")
#                 connection = self.connection_manager.create_connection(dcid, "generated_scid", address)
#                 connection.flow_control = FlowControl()
#                 self.key_management.generate_initial_keys(dcid)
#                 self.session_resumption.generate_session_ticket(dcid)
#                 self.key_update.generate_new_key(dcid)
#                 logging.info("Flow control, key management, session resumption, and key update initialized for new connection")
        
#         elif packet_type == 0xC1:  # Handshake Packet
#             logging.info("Received Handshake Packet")
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Processing handshake for connection {dcid}")
#                 self.handshake.process_client_hello(dcid, "generated_scid", address, data[9:])
        
#         elif packet_type & 0x40 == 0x40:  # Short Header Packet
#             logging.info(f"Received Short Header Packet for DCID {dcid}")
#             connection = self.connection_manager.get_connection(dcid)
#             if connection:
#                 logging.info(f"Processing Short Header Packet for {dcid}")
#                 connection.update_flow_control(bytes_received=len(data))
#                 self.retransmission_handler.track_packet(len(data), data)
#                 lost_packets = self.loss_detection.detect_lost_packets(len(data))
#                 for pkt in lost_packets:
#                     self.retransmission_handler.track_packet(pkt, data)
#                     logging.warning(f"Retransmitting lost packet {pkt}")
#                 logging.info(f"Flow control updated for {dcid}")
                
#                 if self.congestion_control.can_send():
#                     logging.info("Congestion control allows sending more packets")
#                 else:
#                     logging.warning("Congestion window is full, delaying transmission")
                
#                 # Stream Handling
#                 stream_id = int.from_bytes(data[9:13], 'big') if len(data) > 12 else None
#                 if stream_id is not None:
#                     stream = self.stream_manager.create_stream(stream_id, connection)
#                     stream.write(data[13:])
#                     self.stream_priority_queue.add_stream(stream_id, priority=0)  # Default priority
#                     logging.info(f"Stream {stream_id} processed and added to priority queue")
                
#                 # Detect Connection Migration
#                 if self.connection_migration.detect_migration(connection, address):
#                     logging.info(f"Connection {dcid} migrated to new address {address}")
                
#                 # Handle 0-RTT Data
#                 if connection.is_early_data_allowed():
#                     decrypted_data = self.zero_rtt.decrypt_early_data(dcid, data[13:])
#                     if decrypted_data:
#                         logging.info(f"Processed 0-RTT data for {dcid}: {decrypted_data}")
                
#                 # Handle Key Update
#                 if len(data) > 14 and data[13] == 0x1F:  # Example key update trigger
#                     new_key = self.key_update.generate_new_key(dcid)
#                     logging.info(f"Key update triggered for {dcid}, new key: {new_key.hex()}")
        
#         elif packet_type == 0xC0:  # Stateless Reset Packet
#             received_token = data[1:17] if len(data) > 16 else None
#             if received_token:
#                 if self.stateless_reset.handle_reset(received_token, address):
#                     logging.info(f"Stateless reset handled for {address}")
        
#         elif packet_type == 0xC2:  # Connection Close Packet
#             logging.info(f"Received CONNECTION_CLOSE frame for DCID {dcid}")
#             frame = {"type": "CONNECTION_CLOSE", "error_code": 0, "reason": "Normal closure"}  # Placeholder
#             self.connection_close.handle_close_frame(dcid, frame)
        
#         else:
#             logging.warning("Unknown packet type received")

import logging
from connection_manager import ConnectionManager
from handshake import QUICHandshake
from flow_control import FlowControl
from retransmission import RetransmissionHandler
from loss_detection import LossDetection
from congestion_control import CongestionControl
from stream_manager import StreamManager
from stream_prioritization import StreamPriorityQueue
from connection_migration import ConnectionMigration
from stateless_reset import StatelessReset
from key_management import KeyManagement
from connection_close import ConnectionClose
from session_resumption import SessionResumption
from zero_rtt import ZeroRTT
from key_update import KeyUpdate
from timeout_handler import TimeoutHandler
from error_handling import ErrorHandler

class PacketHandler:
    def __init__(self, connection_manager):
        self.connection_manager = connection_manager
        self.handshake = QUICHandshake(connection_manager)
        self.retransmission_handler = RetransmissionHandler()
        self.loss_detection = LossDetection()
        self.congestion_control = CongestionControl()
        self.stream_manager = StreamManager()
        self.stream_priority_queue = StreamPriorityQueue()
        self.connection_migration = ConnectionMigration(connection_manager)
        self.stateless_reset = StatelessReset(connection_manager)
        self.key_management = KeyManagement()
        self.connection_close = ConnectionClose(connection_manager)
        self.session_resumption = SessionResumption()
        self.zero_rtt = ZeroRTT()
        self.key_update = KeyUpdate()
        self.timeout_handler = TimeoutHandler()
        self.error_handler = ErrorHandler()
        logging.info("Packet Handler initialized")

    def process_packet(self, data, address):
        try:
            logging.info(f"Processing packet from {address}: {data.hex()}")
            packet_type = data[0]
            dcid = data[1:9].hex() if len(data) > 8 else None
            
            if packet_type == 0xC3:  # Initial Packet
                connection = self.connection_manager.get_connection(dcid)
                if connection:
                    logging.info(f"Existing connection found for DCID {dcid}")
                else:
                    logging.info(f"No existing connection, creating new one")
                    connection = self.connection_manager.create_connection(dcid, "generated_scid", address)
                    connection.flow_control = FlowControl()
                    self.key_management.generate_initial_keys(dcid)
                    self.session_resumption.generate_session_ticket(dcid)
                    self.key_update.generate_new_key(dcid)
                    logging.info("Flow control, key management, session resumption, and key update initialized for new connection")
                self.timeout_handler.start_timer(dcid)
            
            elif packet_type == 0xC1:  # Handshake Packet
                logging.info("Received Handshake Packet")
                connection = self.connection_manager.get_connection(dcid)
                if connection:
                    logging.info(f"Processing handshake for connection {dcid}")
                    self.handshake.process_client_hello(dcid, "generated_scid", address, data[9:])
                    self.timeout_handler.reset_timer(dcid)
            
            elif packet_type & 0x40 == 0x40:  # Short Header Packet
                logging.info(f"Received Short Header Packet for DCID {dcid}")
                connection = self.connection_manager.get_connection(dcid)
                if connection:
                    logging.info(f"Processing Short Header Packet for {dcid}")
                    connection.update_flow_control(bytes_received=len(data))
                    self.retransmission_handler.track_packet(len(data), data)
                    lost_packets = self.loss_detection.detect_lost_packets(len(data))
                    for pkt in lost_packets:
                        self.retransmission_handler.track_packet(pkt, data)
                        logging.warning(f"Retransmitting lost packet {pkt}")
                    logging.info(f"Flow control updated for {dcid}")
                    self.timeout_handler.reset_timer(dcid)
                    
                    if self.congestion_control.can_send():
                        logging.info("Congestion control allows sending more packets")
                    else:
                        logging.warning("Congestion window is full, delaying transmission")
                    
                    # Stream Handling
                    stream_id = int.from_bytes(data[9:13], 'big') if len(data) > 12 else None
                    if stream_id is not None:
                        stream = self.stream_manager.create_stream(stream_id, connection)
                        stream.write(data[13:])
                        self.stream_priority_queue.add_stream(stream_id, priority=0)  # Default priority
                        logging.info(f"Stream {stream_id} processed and added to priority queue")
                    
                    # Detect Connection Migration
                    if self.connection_migration.detect_migration(connection, address):
                        logging.info(f"Connection {dcid} migrated to new address {address}")
                    
                    # Handle 0-RTT Data
                    if connection.is_early_data_allowed():
                        decrypted_data = self.zero_rtt.decrypt_early_data(dcid, data[13:])
                        if decrypted_data:
                            logging.info(f"Processed 0-RTT data for {dcid}: {decrypted_data}")
                    
                    # Handle Key Update
                    if len(data) > 14 and data[13] == 0x1F:  # Example key update trigger
                        new_key = self.key_update.generate_new_key(dcid)
                        logging.info(f"Key update triggered for {dcid}, new key: {new_key.hex()}")
            
            elif packet_type == 0xC0:  # Stateless Reset Packet
                received_token = data[1:17] if len(data) > 16 else None
                if received_token:
                    if self.stateless_reset.handle_reset(received_token, address):
                        logging.info(f"Stateless reset handled for {address}")
            
            elif packet_type == 0xC2:  # Connection Close Packet
                logging.info(f"Received CONNECTION_CLOSE frame for DCID {dcid}")
                frame = {"type": "CONNECTION_CLOSE", "error_code": 0, "reason": "Normal closure"}  # Placeholder
                self.connection_close.handle_close_frame(dcid, frame)
            
            else:
                logging.warning("Unknown packet type received")
                self.error_handler.log_error("Unknown packet type", address)
        except Exception as e:
            logging.error(f"Error processing packet: {str(e)}")
            self.error_handler.log_error(str(e), address)
