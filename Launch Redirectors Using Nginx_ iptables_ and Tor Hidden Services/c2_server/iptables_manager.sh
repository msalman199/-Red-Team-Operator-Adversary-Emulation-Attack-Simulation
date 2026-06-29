#!/bin/bash

RULES_FILE="/etc/iptables/rules.v4"

case "$1" in
    save)
        echo "Saving iptables rules..."
        sudo mkdir -p /etc/iptables
        sudo iptables-save | sudo tee $RULES_FILE > /dev/null
        echo "Rules saved to $RULES_FILE"
        ;;
    restore)
        echo "Restoring iptables rules..."
        if [ -f "$RULES_FILE" ]; then
            sudo iptables-restore < $RULES_FILE
            echo "Rules restored from $RULES_FILE"
        else
            echo "No rules file found at $RULES_FILE"
        fi
        ;;
    status)
        echo "Current iptables rules:"
        sudo iptables -L -n -v --line-numbers
        echo ""
        echo "NAT table rules:"
        sudo iptables -t nat -L -n -v --line-numbers
        ;;
    *)
        echo "Usage: $0 {save|restore|status}"
        exit 1
        ;;
esac
