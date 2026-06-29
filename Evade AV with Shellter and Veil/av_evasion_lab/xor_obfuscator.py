#!/usr/bin/env python3

import os
import sys
import subprocess
import time
from pathlib import Path

class PayloadObfuscator:
    def __init__(self, payload_file):
        self.payload_file = payload_file
        self.output_dir = "obfuscated_payloads"
        self.create_output_directory()
    
    def create_output_directory(self):
        """Create output directory for obfuscated payloads"""
        Path(self.output_dir).mkdir(exist_ok=True)
        print(f"Output directory: {self.output_dir}")
    
    def run_base64_obfuscation(self):
        """Run Base64 obfuscation"""
        output_file = f"{self.output_dir}/base64_payload.py"
        cmd = ["python3", "obfuscator.py", self.payload_file, output_file]
        
        try:
            subprocess.run(cmd, check=True)
            print("✓ Base64 obfuscation completed")
            return True
        except subprocess.CalledProcessError:
            print("✗ Base64 obfuscation failed")
            return False
    
    def run_xor_obfuscation(self):
        """Run XOR obfuscation"""
        output_file = f"{self.output_dir}/xor_payload.py"
        cmd = ["python3", "xor_obfuscator.py", self.payload_file, output_file]
        
        try:
            subprocess.run(cmd, check=True)
            print("✓ XOR obfuscation completed")
            return True
        except subprocess.CalledProcessError:
            print("✗ XOR obfuscation failed")
            return False
    
    def generate_veil_payloads(self):
        """Generate multiple Veil payloads"""
        veil_configs = [
            ("python/meterpreter/rev_tcp", "veil_python"),
            ("powershell/meterpreter/rev_tcp", "veil_powershell"),
            ("c/meterpreter/rev_tcp", "veil_c")
        ]
        
        for payload_type, name in veil_configs:
            print(f"Generating Veil payload: {payload_type}")
            # Note: This would require Veil automation
            # For demonstration, we'll create placeholder files
            placeholder_file = f"{self.output_dir}/{name}.py"
            with open(placeholder_file, 'w') as f:
                f.write(f"# Veil payload: {payload_type}\n")
                f.write(f"# Generated at: {time.ctime()}\n")
            print(f"✓ Veil payload placeholder created: {name}")
    
    def create_summary_report(self):
        """Create summary report of generated payloads"""
        report_file = f"{self.output_dir}/obfuscation_report.txt"
        
        with open(report_file, 'w') as f:
            f.write("Payload Obfuscation Report\n")
            f.write("=" * 30 + "\n\n")
            f.write(f"Original payload: {self.payload_file}\n")
            f.write(f"Generation time: {time.ctime()}\n\n")
            
            f.write("Generated payloads:\n")
            for file in os.listdir(self.output_dir):
                if file.endswith(('.py', '.exe', '.bat')):
                    file_path = os.path.join(self.output_dir, file)
                    file_size = os.path.getsize(file_path)
                    f.write(f"- {file} ({file_size} bytes)\n")
        
        print(f"✓ Summary report created: {report_file}")
    
    def run_all_obfuscations(self):
        """Run all obfuscation techniques"""
        print("Starting automated payload obfuscation...")
        print("-" * 40)
        
        # Run Base64 obfuscation
        self.run_base64_obfuscation()
        
        # Run XOR obfuscation
        self.run_xor_obfuscation()
        
        # Generate Veil payloads
        self.generate_veil_payloads()
        
        # Create summary report
        self.create_summary_report()
        
        print("-" * 40)
        print("Automated obfuscation completed!")
        print(f"Check the '{self.output_dir}' directory for results")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 batch_obfuscator.py <payload_file>")
        sys.exit(1)
    
    payload_file = sys.argv[1]
    
    if not os.path.exists(payload_file):
        print(f"Error: Payload file '{payload_file}' not found")
        sys.exit(1)
    
    obfuscator = PayloadObfuscator(payload_file)
    obfuscator.run_all_obfuscations()

if __name__ == "__main__":
    main()
