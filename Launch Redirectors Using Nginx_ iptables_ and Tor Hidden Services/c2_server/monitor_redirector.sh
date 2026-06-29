#!/bin/bash

echo "Starting redirector monitoring..."
echo "Press Ctrl+C to stop monitoring"

# Function to monitor logs
monitor_logs() {
    echo "=== Monitoring Nginx Access Logs ==="
    sudo tail -f /var/log/nginx/redirector_access.log &
    NGINX_PID=$!
    
    echo "=== Monitoring iptables Logs ==="
    sudo tail -f /var/log/kern.log | grep "C2_TRAFFIC" &
    IPTABLES_PID=$!
    
    echo "=== Monitoring Tor Logs ==="
    sudo tail -f /var/log/tor/notices.log &
    TOR_PID=$!
    
    # Wait for interrupt
    trap "kill $NGINX_PID $IPTABLES_PID $TOR_PID 2>/dev/null; exit" INT
    wait
}

monitor_logs
