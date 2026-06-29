#!/bin/bash

echo "Cleaning up redirector infrastructure..."

# Stop services
sudo systemctl stop nginx
sudo systemctl stop tor
pkill -f mock_c2.py

# Reset iptables
sudo iptables -F
sudo iptables -X
sudo iptables -t nat -F
sudo iptables -t nat -X
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT

# Remove configurations
sudo rm -f /etc/nginx/sites-enabled/redirector
sudo rm -f /etc/nginx/sites-available/redirector
sudo rm -rf /etc/nginx/ssl/
sudo rm -rf /var/lib/tor/c2_service/
sudo rm -rf /var/lib/tor/direct_c2/

# Restore defaults
sudo cp /etc/nginx/sites-available/default.backup /etc/nginx/sites-available/default
sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/
sudo cp /etc/tor/torrc.backup /etc/tor/torrc

# Restart services
sudo systemctl start nginx
sudo systemctl start tor

echo "Cleanup complete!"
