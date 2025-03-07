import logging
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class KeyManagement:
    def __init__(self):
        self.keys = {}
        logging.info("Key Management initialized")

    def generate_initial_keys(self, connection_id):
        """Generates initial encryption keys based on connection ID."""
        secret = os.urandom(32)  # Placeholder for proper key derivation
        self.keys[connection_id] = {
            "encryption_key": AESGCM(secret),
            "decryption_key": AESGCM(secret)
        }
        logging.info(f"Generated keys for connection {connection_id}")
    
    def encrypt_packet(self, connection_id, plaintext, nonce):
        """Encrypts a packet using the stored encryption key."""
        if connection_id in self.keys:
            return self.keys[connection_id]["encryption_key"].encrypt(nonce, plaintext, None)
        logging.error("Encryption failed: No key found")
        return None
    
    def decrypt_packet(self, connection_id, ciphertext, nonce):
        """Decrypts a packet using the stored decryption key."""
        if connection_id in self.keys:
            try:
                return self.keys[connection_id]["decryption_key"].decrypt(nonce, ciphertext, None)
            except Exception as e:
                logging.error(f"Decryption failed: {e}")
        return None


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