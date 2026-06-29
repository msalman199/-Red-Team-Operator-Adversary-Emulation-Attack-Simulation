#!/bin/bash

echo "Testing Tor connectivity..."

# Test SOCKS proxy
echo "1. Testing SOCKS proxy connection:"
curl --socks5 127.0.0.1:9050 http://httpbin.org/ip

echo -e "\n2. Testing hidden service connectivity:"
HIDDEN_SERVICE=$(sudo cat /var/lib/tor/c2_service/hostname 2>/dev/null)

if [ -n "$HIDDEN_SERVICE" ]; then
    echo "Hidden service address: $HIDDEN_SERVICE"
    echo "Testing connection to hidden service..."
    curl --socks5 127.0.0.1:9050 "http://$HIDDEN_SERVICE/health" -m 30
else
    echo "Hidden service not yet available. Please wait and try again."
fi

echo -e "\n3. Testing direct C2 hidden service:"
DIRECT_C2=$(sudo cat /var/lib/tor/direct_c2/hostname 2>/dev/null)

if [ -n "$DIRECT_C2" ]; then
    echo "Direct C2 address: $DIRECT_C2"
    curl --socks5 127.0.0.1:9050 "http://$DIRECT_C2" -H "User-Agent: RedTeamAgent" -m 30
else
    echo "Direct C2 service not yet available. Please wait and try again."
fi
