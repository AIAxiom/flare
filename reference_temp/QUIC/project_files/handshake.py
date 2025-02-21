import logging
import os
from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from connection_manager import ConnectionManager

class QUICHandshake:
    def __init__(self, connection_manager):
        self.connection_manager = connection_manager
        logging.info("QUIC Handshake Handler initialized")

    def generate_keys(self):
        private_key = x25519.X25519PrivateKey.generate()
        public_key = private_key.public_key()
        return private_key, public_key

    def process_client_hello(self, dcid, scid, address, client_public_key_bytes):
        connection = self.connection_manager.create_connection(dcid, scid, address)
        server_private_key, server_public_key = self.generate_keys()
        
        shared_key = server_private_key.exchange(x25519.X25519PublicKey.from_public_bytes(client_public_key_bytes))
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'quic handshake',
        ).derive(shared_key)
        
        connection.set_encryption_keys(derived_key)
        logging.info(f"Handshake successful for connection {dcid}")
        return server_public_key.public_bytes_raw()
