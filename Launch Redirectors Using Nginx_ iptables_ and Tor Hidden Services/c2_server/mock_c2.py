#!/usr/bin/env python3
import http.server
import socketserver
import json
from datetime import datetime

class C2Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            "status": "active",
            "timestamp": datetime.now().isoformat(),
            "message": "C2 server responding",
            "client_ip": self.client_address[0]
        }
        
        self.wfile.write(json.dumps(response).encode())
        print(f"[{datetime.now()}] C2 Request from {self.client_address[0]}")
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            "status": "received",
            "timestamp": datetime.now().isoformat(),
            "data_length": content_length
        }
        
        self.wfile.write(json.dumps(response).encode())
        print(f"[{datetime.now()}] C2 POST from {self.client_address[0]} - {content_length} bytes")

PORT = 8080
with socketserver.TCPServer(("", PORT), C2Handler) as httpd:
    print(f"Mock C2 server running on port {PORT}")
    httpd.serve_forever()
