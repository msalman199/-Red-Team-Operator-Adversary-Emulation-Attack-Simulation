#!/bin/bash

echo "=== Redirector Infrastructure Test Suite ==="
echo "Testing all components of the redirector setup..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

test_nginx() {
    echo -e "\n${YELLOW}Testing Nginx Redirector...${NC}"
    
    # Test normal traffic redirection
    echo "1. Testing normal traffic redirection:"
    RESPONSE=$(curl -s -I http://localhost | head -n 1)
    if [[ $RESPONSE == *"301"* ]]; then
        echo -e "${GREEN}✓ Normal traffic correctly redirected${NC}"
    else
        echo -e "${RED}✗ Normal traffic redirection failed${NC}"
    fi
    
    # Test C2 traffic
    echo "2. Testing C2 traffic routing:"
    RESPONSE=$(curl -s -H "User-Agent: RedTeamAgent" http://localhost)
    if [[ $RESPONSE == *"C2 server responding"* ]]; then
        echo -e "${GREEN}✓ C2 traffic correctly routed${NC}"
    else
        echo -e "${RED}✗ C2 traffic routing failed${NC}"
    fi
}

test_iptables() {
    echo -e "\n${YELLOW}Testing iptables Configuration...${NC}"
    
    # Check if rules are loaded
    RULE_COUNT=$(sudo iptables -L | wc -l)
    if [ $RULE_COUNT -gt 10 ]; then
        echo -e "${GREEN}✓ iptables rules are configured${NC}"
    else
        echo -e "${RED}✗ iptables rules may not be properly configured${NC}"
    fi
    
    # Test port forwarding
    echo "Testing port forwarding (8443 -> 80):"
    RESPONSE=$(curl -s -I http://localhost:8443 | head -n 1)
    if [[ $RESPONSE == *"301"* ]] || [[ $RESPONSE == *"200"* ]]; then
        echo -e "${GREEN}✓ Port forwarding working${NC}"
    else
        echo -e "${RED}✗ Port forwarding may not be working${NC}"
    fi
}

test_tor() {
    echo -e "\n${YELLOW}Testing Tor Hidden Services...${NC}"
    
    # Check if Tor is running
    if systemctl is-active --quiet tor; then
        echo -e "${GREEN}✓ Tor service is running${NC}"
    else
        echo -e "${RED}✗ Tor service is not running${NC}"
        return
    fi
    
    # Check hidden service addresses
    if [ -f "/var/lib/tor/c2_service/hostname" ]; then
        HIDDEN_ADDR=$(sudo cat /var/lib/tor/c2_service/hostname)
        echo -e "${GREEN}✓ Hidden service address: $HIDDEN_ADDR${NC}"
    else
        echo -e "${RED}✗ Hidden service address not found${NC}"
    fi
    
    # Test SOCKS proxy
    PROXY_TEST=$(curl --socks5 127.0.0.1:9050 -s http://httpbin.org/ip -m 10 2>/dev/null)
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ Tor SOCKS proxy is working${NC}"
    else
        echo -e "${RED}✗ Tor SOCKS proxy test failed${NC}"
    fi
}

test_integration() {
    echo -e "\n${YELLOW}Testing Full Integration...${NC}"
    
    # Test complete chain: Tor -> Nginx -> C2
    if [ -f "/var/lib/tor/c2_service/hostname" ]; then
        HIDDEN_ADDR=$(sudo cat /var/lib/tor/c2_service/hostname)
        echo "Testing complete chain through hidden service..."
        
        RESPONSE=$(curl --socks5 127.0.0.1:9050 -s -H "User-Agent: RedTeamAgent" "http://$HIDDEN_ADDR" -m 30 2>/dev/null)
        if [[ $RESPONSE == *"C2 server responding"* ]]; then
            echo -e "${GREEN}✓ Full integration test passed${NC}"
        else
            echo -e "${RED}✗ Full integration test failed${NC}"
        fi
    else
        echo -e "${YELLOW}⚠ Hidden service not ready for integration test${NC}"
    fi
}

# Run all tests
test_nginx
test_iptables
test_tor
test_integration

echo -e "\n${YELLOW}=== Test Suite Complete ===${NC}"
echo "Check the results above to verify your redirector infrastructure."
