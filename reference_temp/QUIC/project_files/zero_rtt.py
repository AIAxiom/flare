import logging
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class ZeroRTT:
    def __init__(self):
        self.early_data_keys = {}
        logging.info("0-RTT handler initialized")
    
    def generate_early_data_key(self, connection_id):
        """Generates an encryption key for early data."""
        key = os.urandom(32)
        self.early_data_keys[connection_id] = key
        logging.info(f"Generated 0-RTT key for connection {connection_id}")
        return key
    
    def encrypt_early_data(self, connection_id, plaintext):
        """Encrypts early data using the 0-RTT key."""
        key = self.early_data_keys.get(connection_id)
        if not key:
            logging.error("No 0-RTT key available for encryption")
            return None
        
        nonce = os.urandom(12)
        aesgcm = AESGCM(key)
        ciphertext = aesgcm.encrypt(nonce, plaintext, None)
        logging.info(f"0-RTT data encrypted for connection {connection_id}")
        return nonce + ciphertext
    
    def decrypt_early_data(self, connection_id, encrypted_data):
        """Decrypts received early data."""
        key = self.early_data_keys.get(connection_id)
        if not key:
            logging.error("No 0-RTT key available for decryption")
            return None
        
        nonce, ciphertext = encrypted_data[:12], encrypted_data[12:]
        aesgcm = AESGCM(key)
        try:
            plaintext = aesgcm.decrypt(nonce, ciphertext, None)
            logging.info(f"0-RTT data decrypted for connection {connection_id}")
            return plaintext
        except Exception as e:
            logging.error(f"0-RTT decryption failed: {e}")
            return None
