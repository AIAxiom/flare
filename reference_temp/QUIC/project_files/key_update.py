import logging
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class KeyUpdate:
    def __init__(self):
        self.key_store = {}
        logging.info("Key Update Manager initialized")

    def generate_new_key(self, connection_id):
        """Generates a new encryption key for a connection."""
        new_key = os.urandom(32)
        self.key_store[connection_id] = new_key
        logging.info(f"New key generated for connection {connection_id}")
        return new_key

    def encrypt_data(self, connection_id, plaintext):
        """Encrypts data using the updated key."""
        key = self.key_store.get(connection_id)
        if not key:
            logging.error("No key available for encryption")
            return None

        nonce = os.urandom(12)
        aesgcm = AESGCM(key)
        ciphertext = aesgcm.encrypt(nonce, plaintext, None)
        logging.info(f"Data encrypted for connection {connection_id}")
        return nonce + ciphertext

    def decrypt_data(self, connection_id, encrypted_data):
        """Decrypts received data with the updated key."""
        key = self.key_store.get(connection_id)
        if not key:
            logging.error("No key available for decryption")
            return None

        nonce, ciphertext = encrypted_data[:12], encrypted_data[12:]
        aesgcm = AESGCM(key)
        try:
            plaintext = aesgcm.decrypt(nonce, ciphertext, None)
            logging.info(f"Data decrypted for connection {connection_id}")
            return plaintext
        except Exception as e:
            logging.error(f"Decryption failed: {e}")
            return None