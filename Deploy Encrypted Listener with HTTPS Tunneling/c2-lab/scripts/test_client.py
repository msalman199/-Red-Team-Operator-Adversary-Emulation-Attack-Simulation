#!/usr/bin/env python3
"""
Test Client - Student Implementation
Complete the TODO sections to test the listener
"""

import socket
import base64
import time
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class TestClient:
    def __init__(self, host='localhost', port=8080, password='RedTeamTraining2024'):
        self.host = host
        self.port = port
        self.password = password.encode()
        self.setup_encryption()
        
    def setup_encryption(self):
        """Initialize encryption matching server configuration"""
        # TODO: Use same salt as server (b'salt_for_lab_demo')
        # TODO: Initialize PBKDF2HMAC with matching parameters
        # TODO: Derive key and create Fernet cipher
        pass
        
    def encrypt_data(self, data):
        """Encrypt data for transmission"""
        # TODO: Implement encryption
        pass
        
    def decrypt_data(self, encrypted_data):
        """Decrypt received data"""
        # TODO: Implement decryption with error handling
        pass
        
    def connect_and_test(self):
        """Connect to listener and test communication"""
        # TODO: Create socket and connect to server
        # TODO: Loop for 60 seconds
        # TODO: Receive heartbeat, decrypt, and print
        # TODO: Send encrypted response "CLIENT_ALIVE"
        # TODO: Handle exceptions and close socket
        pass

if __name__ == "__main__":
    # TODO: Create TestClient instance and run test
    pass
