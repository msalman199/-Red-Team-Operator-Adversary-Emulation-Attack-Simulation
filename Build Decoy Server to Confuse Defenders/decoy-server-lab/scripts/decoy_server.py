#!/usr/bin/env python3

import flask
from flask import Flask, request, jsonify
import logging
import datetime
import random
import time

app = Flask(__name__)

# TODO: Configure logging to write to both file and console
# Hint: Use logging.basicConfig with FileHandler and StreamHandler

# Global variables for tracking
visitor_count = 0
login_attempts = []

def log_visitor(request):
    """
    Log visitor information in a realistic format.
    
    Args:
        request: Flask request object
    
    Returns:
        Dictionary with visitor information
    """
    global visitor_count
    visitor_count += 1
    
    # TODO: Create visitor_info dictionary with:
    # - timestamp (use datetime.datetime.now().isoformat())
    # - ip address (request.remote_addr)
    # - user_agent (request.headers.get('User-Agent'))
    # - method (request.method)
    # - path (request.path)
    # - visitor_id
    
    # TODO: Log the visitor information
    
    pass

@app.route('/')
def index():
    """Serve the main homepage"""
    # TODO: Log the visitor
    # TODO: Read and return web-content/index.html
    pass

@app.route('/admin')
def admin():
    """Serve the admin login page"""
    # TODO: Log the visitor
    # TODO: Read and return web-content/admin.html
    pass

@app.route('/login', methods=['POST'])
def login():
    """
    Handle login attempts and log credentials.
    Always returns failure but logs the attempt.
    """
    # TODO: Extract username and password from request.form
    # TODO: Create login_attempt dictionary with timestamp, ip, credentials
    # TODO: Append to login_attempts list
    # TODO: Log the attempt with logging.warning()
    # TODO: Simulate processing time with time.sleep(random.uniform(1.0, 3.0))
    # TODO: Return HTML response indicating login failure
    pass

@app.route('/admin-auth', methods=['POST'])
def admin_auth():
    """
    Handle admin login attempts with higher severity logging.
    """
    # TODO: Similar to login() but use logging.critical()
    # TODO: Longer processing time (2-5 seconds)
    pass

@app.route('/api/status')
def api_status():
    """
    Fake API endpoint that returns realistic system status.
    """
    # TODO: Create status_data dictionary with:
    # - status: 'operational'
    # - version: '2.1.4'
    # - timestamp
    # - services dict (web_server, database, backup_service all 'running')
    # - system_stats (cpu_usage, memory_usage, disk_usage with random values)
    
    # TODO: Return jsonify(status_data)
    pass

@app.route('/robots.txt')
def robots():
    """Return realistic robots.txt"""
    return '''User-agent: *
Disallow: /admin/
Disallow: /api/
Allow: /
'''

@app.route('/health')
def health_check():
    """Health check endpoint"""
    # TODO: Return JSON with status, timestamp, and fake uptime
    pass

if __name__ == '__main__':
    # TODO: Configure logging
    # TODO: Start the Flask app on 0.0.0.0:8080
    pass
