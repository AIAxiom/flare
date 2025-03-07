import logging

class ConnectionMigration:
    def __init__(self, connection_manager):
        self.connection_manager = connection_manager
        logging.info("Connection Migration handler initialized")

    def detect_migration(self, connection, new_address):
        """Detects if the client's address has changed."""
        if connection.peer_address != new_address:
            logging.info(f"Connection {connection.dcid} migrating from {connection.peer_address} to {new_address}")
            connection.peer_address = new_address
            return True
        return False
