#!/usr/bin/env python3
import re
import sys

def extract_ntlm_hashes(filename):
    """
    Extract NTLM hashes from LSA dump file.
    
    Args:
        filename: Path to LSA dump file
    
    Returns:
        Number of hashes extracted
    """
    # TODO: Open and read the file
    # TODO: Use regex to find User and Hash NTLM patterns
    # TODO: Extract username and NTLM hash (second part after colon)
    # TODO: Write to extracted_ntlm.txt in format: username:hash
    # TODO: Return count of extracted hashes
    pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 extract_ntlm.py <lsa_dump_file>")
        sys.exit(1)
    
    # TODO: Call extract_ntlm_hashes function
    # TODO: Print summary of extraction
    pass
