#!/usr/bin/env python3

import re
from collections import Counter
from datetime import datetime

def analyze_decoy_logs(log_file):
    """
    Analyze decoy server logs to identify patterns.
    
    Args:
        log_file: Path to the log file
    
    Returns:
        Dictionary with analysis results
    """
    # TODO: Read the log file
    # TODO: Count total requests
    # TODO: Identify unique IP addresses
    # TODO: Count login attempts
    # TODO: Count admin access attempts
    # TODO: Identify most common user agents
    # TODO: Calculate requests per hour
    
    # TODO: Return dictionary with all statistics
    pass

def identify_suspicious_patterns(log_file):
    """
    Identify suspicious patterns in the logs.
    
    Args:
        log_file: Path to the log file
    
    Returns:
        List of suspicious activities
    """
    # TODO: Look for patterns like:
    # - Multiple failed login attempts from same IP
    # - Scanning behavior (many different paths)
    # - Suspicious user agents
    # - Rapid sequential requests
    
    pass

if __name__ == '__main__':
    # TODO: Analyze logs/decoy-server.log
    # TODO: Print statistics
    # TODO: Print suspicious patterns
    pass
