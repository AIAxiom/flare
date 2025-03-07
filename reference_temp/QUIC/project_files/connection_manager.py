import logging
import os
from connection import Connection

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConnectionManager:
    def __init__(self):
        self.connections = {}  # Stores active connections {dcid: client_address}
    
    def generate_connection_id(self):
        return os.urandom(8).hex()
    
    def add_connection(self, dcid, client_address):
        if dcid not in self.connections:
            self.connections[dcid] = client_address
            logging.info(f"New QUIC connection established: {dcid} -> {client_address}")
    
    def get_client_address(self, dcid):
        return self.connections.get(dcid)
    
    def create_connection(self, dcid, scid, address):
        if dcid in self.connections:
            logging.warning(f"Connection with DCID {dcid} already exists")
            return self.connections[dcid]
        
        connection = Connection(dcid, scid, address)
        self.connections[dcid] = connection
        return connection
    
    def get_connection(self, dcid):
        return self.connections.get(dcid)
    
    def remove_connection(self, dcid):
        if dcid in self.connections:
            logging.info(f"Removing connection {dcid}")
            del self.connections[dcid]
    
    def cleanup_closed_connections(self):
        closed_dcids = [dcid for dcid, conn in self.connections.items() if conn.state == "CLOSING"]
        for dcid in closed_dcids:
            self.remove_connection(dcid)

if __name__ == "__main__":
    manager = ConnectionManager()
    sample_dcid = manager.generate_connection_id()
    manager.add_connection(sample_dcid, ('127.0.0.1', 4433))
    print(manager.get_client_address(sample_dcid))
