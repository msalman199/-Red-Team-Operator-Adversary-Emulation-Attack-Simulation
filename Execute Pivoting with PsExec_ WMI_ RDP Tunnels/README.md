# 🔴 Execute Pivoting with PsExec, WMI & RDP Tunnels

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-red?style=for-the-badge&logo=shield&logoColor=white)
![Lab Type](https://img.shields.io/badge/Lab%20Type-Red%20Team-darkred?style=for-the-badge&logo=target&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Advanced-critical?style=for-the-badge&logo=buffer&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux%20%2F%20Docker-557C94?style=for-the-badge&logo=docker&logoColor=white)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Impacket](https://img.shields.io/badge/Impacket-Toolkit-red?style=flat-square&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?style=flat-square&logo=docker&logoColor=white)
![SSH](https://img.shields.io/badge/SSH-Tunneling-black?style=flat-square&logo=openssh&logoColor=white)
![RDP](https://img.shields.io/badge/RDP-Pivoting-0078D4?style=flat-square&logo=microsoft&logoColor=white)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE%20ATT%26CK-T1570%20%7C%20T1021%20%7C%20T1570-red?style=flat-square&logo=databricks&logoColor=white)
![Tactic](https://img.shields.io/badge/Tactic-Lateral%20Movement-purple?style=flat-square&logo=gnubash&logoColor=white)
![License](https://img.shields.io/badge/License-Educational-green?style=flat-square&logo=bookstack&logoColor=white)

</div>

---

## 📋 Table of Contents

- [🎯 Objectives](#-objectives)
- [✅ Prerequisites](#-prerequisites)
- [🧪 Lab Environment](#-lab-environment)
- [🐳 Task 1 — Configure Target Environment](#-task-1--configure-simulated-target-environment)
- [⚙️ Task 2 — PsExec & WMI Lateral Movement](#️-task-2--implement-psexec-and-wmi-lateral-movement)
- [🔀 Task 3 — SSH Tunnels & RDP Pivoting](#-task-3--establish-ssh-tunnels-for-rdp-pivoting)
- [🤖 Task 4 — Automated Pivoting Workflow](#-task-4--automate-complete-pivoting-workflow)
- [✔️ Expected Outcomes](#️-expected-outcomes)
- [🛠️ Troubleshooting](#️-troubleshooting)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

By the end of this lab, students will be able to:

- 🔀 Understand **network pivoting and lateral movement** fundamentals
- ⚙️ Configure and use **PsExec** for remote command execution
- 📡 Utilize **WMI** for lateral movement operations
- 🔐 Establish **SSH tunnels** to simulate RDP pivoting
- 🤖 Automate pivoting workflows with **Python scripts**
- 🛡️ Implement **OPSEC considerations** during lateral movement

---

## ✅ Prerequisites

| Requirement | Details |
|---|---|
| 🌐 Networking | Basic knowledge of TCP/IP, ports, protocols |
| 💻 CLI Skills | Linux command line proficiency |
| 🐍 Python | Python programming fundamentals |
| 🔐 SSH | Understanding of SSH and tunneling concepts |
| 📋 Methodology | Familiarity with penetration testing methodology |

---

## 🧪 Lab Environment

> 💡 **Ready-to-Use Cloud Machines:** Al Nafi provides pre-configured Linux-based cloud machines. Click **▶ Start Lab** to access your environment.

| Component | Details |
|---|---|
| 🔪 Kali Linux | Penetration testing tools pre-installed |
| 🐍 Python 3.x | With required libraries and frameworks |
| 🧰 Impacket Toolkit | Windows protocol exploitation |
| 🐳 Docker | Container-based target simulation |
| 🔐 SSH | Client/server capabilities |

---

## 🐳 Task 1 — Configure Simulated Target Environment

> 🔎 **Overview:** Set up isolated Docker-based target network for safe pivoting practice.

### Step 1.1 — Install Required Tools

```bash
# 🔄 Update system and install dependencies
sudo apt update
sudo apt install -y python3-pip docker.io sshpass

# 🐍 Install Impacket
pip3 install impacket

# 🐳 Start Docker service
sudo systemctl start docker
sudo usermod -aG docker $USER
newgrp docker
```

---

### Step 1.2 — Create Target Network

```bash
# 🌐 Create isolated network for lab
docker network create --subnet=192.168.100.0/24 pivot-lab

# 📁 Create lab directory
mkdir -p ~/pivot-lab && cd ~/pivot-lab
```

---

### Step 1.3 — Deploy Target Containers

```yaml
# docker-compose.yml
version: '3.8'
services:
  target1:
    image: ubuntu:20.04
    container_name: target1
    networks:
      pivot-lab:
        ipv4_address: 192.168.100.10
    command: >
      bash -c "apt update && apt install -y openssh-server &&
      echo 'root:password123' | chpasswd &&
      echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config &&
      service ssh start && tail -f /dev/null"

  target2:
    image: ubuntu:20.04
    container_name: target2
    networks:
      pivot-lab:
        ipv4_address: 192.168.100.20
    command: >
      bash -c "apt update && apt install -y openssh-server &&
      echo 'root:password123' | chpasswd &&
      echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config &&
      service ssh start && tail -f /dev/null"

networks:
  pivot-lab:
    external: true
```

```bash
# 🚀 Launch environment
docker-compose up -d
sleep 30

# ✅ Verify containers are running
docker ps
```

---

## ⚙️ Task 2 — Implement PsExec and WMI Lateral Movement

> 🔎 **Overview:** Create tools for executing commands remotely via PsExec and WMI.
> **MITRE ATT&CK:** [T1021.002 – Remote Services: SMB](https://attack.mitre.org/techniques/T1021/002/) | [T1021.006 – Remote Services: WMI](https://attack.mitre.org/techniques/T1021/006/)

### 🗺️ Lateral Movement Architecture

```
Attacker                Jump Host (target1)        Final Target (target2)
   │                          │                            │
   │──────PsExec/WMI─────────►│                           │
   │                          │                           │
   │                          │────SSH Tunnel────────────►│
   │◄──────Command Output──────│◄──Command Response───────│
```

---

### Step 2.1 — Create PsExec Simulator

```python
#!/usr/bin/env python3
"""
PsExec-like Lateral Movement Tool
Simulates remote command execution capabilities
"""

import subprocess
import sys
from datetime import datetime

class PsExecTool:
    def __init__(self, target_ip, username, password):
        """
        Initialize PsExec tool for lateral movement.

        Args:
            target_ip: Target system IP address
            username:  Authentication username
            password:  Authentication password
        """
        self.target_ip = target_ip
        self.username  = username
        self.password  = password
        self.connected = False

    def log(self, message):
        """Log activity with timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")

    def test_connection(self):
        """
        Test if target is reachable on SSH port.

        Returns:
            bool: True if reachable, False otherwise

        TODO: Implement socket connection test to port 22
        TODO: Add timeout handling (5 seconds)
        TODO: Return connection status
        """
        pass

    def authenticate(self):
        """
        Authenticate to target system.

        Returns:
            bool: True if authentication successful

        TODO: Use sshpass to test authentication
        TODO: Handle authentication failures gracefully
        TODO: Set self.connected status
        """
        pass

    def execute_command(self, command):
        """
        Execute command on remote target.

        Args:
            command: Command string to execute

        Returns:
            tuple: (success, output, error)

        TODO: Build SSH command with sshpass
        TODO: Execute command and capture output
        TODO: Handle errors and timeouts
        """
        pass

    def lateral_movement(self):
        """
        Perform lateral movement sequence.

        TODO: Execute reconnaissance commands (whoami, hostname, etc.)
        TODO: Gather system information (uname, df, ps)
        TODO: Check network configuration (ip addr, netstat)
        TODO: Log all activities with timestamps
        """
        pass

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 psexec_tool.py <target_ip> <username> <password>")
        sys.exit(1)

    # TODO: Parse command line arguments
    # TODO: Create PsExecTool instance
    # TODO: Test connection and authenticate
    # TODO: Execute lateral movement sequence
    pass

if __name__ == "__main__":
    main()
```

---

### Step 2.2 — Create WMI Lateral Movement Tool

```python
#!/usr/bin/env python3
"""
WMI-based Lateral Movement Tool
Simulates Windows Management Instrumentation exploitation
"""

import subprocess
import sys
from datetime import datetime

class WMITool:
    def __init__(self, target_ip, username, password):
        """
        Initialize WMI tool for remote management.

        Args:
            target_ip: Target system IP
            username:  Authentication username
            password:  Authentication password
        """
        self.target_ip = target_ip
        self.username  = username
        self.password  = password

    def connect(self):
        """
        Establish WMI connection to target.

        Returns:
            bool: Connection status

        TODO: Test target reachability
        TODO: Simulate WMI connection establishment
        TODO: Return connection status
        """
        pass

    def query_system_info(self):
        """
        Query system information via WMI.

        Returns:
            dict: System information

        TODO: Execute queries for OS, hostname, memory, disk
        TODO: Parse and structure results
        TODO: Return information dictionary with keys:
        TODO:   - os_version
        TODO:   - hostname
        TODO:   - total_memory
        TODO:   - disk_space
        """
        pass

    def create_process(self, command):
        """
        Create remote process via WMI.

        Args:
            command: Command to execute

        Returns:
            bool: Success status

        TODO: Execute remote process creation
        TODO: Handle process creation errors
        TODO: Return execution status
        """
        pass

    def lateral_movement_sequence(self):
        """
        Execute WMI-based lateral movement.

        TODO: Query system information
        TODO: Create persistence mechanism
        TODO: Execute and verify persistence
        TODO: Log all actions
        """
        pass

def main():
    # TODO: Parse arguments
    # TODO: Create WMITool instance
    # TODO: Connect and execute lateral movement
    pass

if __name__ == "__main__":
    main()
```

---

### Step 2.3 — Test Lateral Movement Tools

```bash
# 📧 Make scripts executable
chmod +x psexec_tool.py wmi_tool.py

# 🔧 Test PsExec tool (complete implementation first)
python3 psexec_tool.py 192.168.100.10 root password123

# 💻 Test WMI tool (complete implementation first)
python3 wmi_tool.py 192.168.100.10 root password123
```

---

## 🔀 Task 3 — Establish SSH Tunnels for RDP Pivoting

> 🔎 **Overview:** Create **multi-hop SSH tunnels** to enable RDP access through intermediate hosts.
> **MITRE ATT&CK:** [T1570 – Lateral Tool Transfer](https://attack.mitre.org/techniques/T1570/) | [T1021.001 – Remote Services: RDP](https://attack.mitre.org/techniques/T1021/001/)

### 🔐 SSH Tunnel Architecture

```
┌─────────────────────────────────────────────────────────┐
│  Local Client                                           │
│  (Attacker)                                             │
│  localhost:8389                                         │
└────────────┬────────────────────────────────────────────┘
             │
             │ SSH Tunnel (encrypted)
             │
┌────────────▼────────────────────────────────────────────┐
│  Jump Host (target1)                                    │
│  192.168.100.10:22                                      │
│  Forwards to 192.168.100.20:3389                        │
└────────────┬────────────────────────────────────────────┘
             │
             │ SSH Connection
             │
┌────────────▼────────────────────────────────────────────┐
│  Final Target (target2)                                 │
│  192.168.100.20:3389 (RDP)                              │
└─────────────────────────────────────────────────────────┘
```

---

### Step 3.1 — Create Tunnel Manager

```python
#!/usr/bin/env python3
"""
SSH Tunnel Manager
Creates and manages multi-hop SSH tunnels for pivoting
"""

import subprocess
import socket
import sys
from datetime import datetime

class TunnelManager:
    def __init__(self):
        """Initialize tunnel management system."""
        self.active_tunnels = {}
        self.tunnel_counter = 0

    def find_available_port(self, start_port=8000):
        """
        Find available local port for tunneling.

        Args:
            start_port: Starting port to check

        Returns:
            int: Available port number or None

        TODO: Iterate through port range (start_port to start_port+100)
        TODO: Test each port with socket binding
        TODO: Return first available port
        """
        pass

    def create_tunnel(self, jump_host, jump_user, jump_pass,
                      target_host, target_port, local_port=None):
        """
        Create SSH tunnel through jump host.

        Args:
            jump_host:   Intermediate host IP
            jump_user:   Jump host username
            jump_pass:   Jump host password
            target_host: Final target IP
            target_port: Target service port
            local_port:  Local port (auto-assign if None)

        Returns:
            str: Tunnel ID or None if failed

        TODO: Find available local port if not specified
        TODO: Build SSH tunnel command with sshpass:
        TODO:   sshpass -p <pass> ssh -L <local>:<target>:<port> <user>@<jump>
        TODO: Start tunnel process and verify
        TODO: Store tunnel information with ID
        TODO: Return tunnel ID
        """
        pass

    def test_tunnel(self, local_port):
        """
        Test if tunnel is operational.

        Args:
            local_port: Local tunnel port

        Returns:
            bool: Tunnel status

        TODO: Connect to localhost:local_port
        TODO: Test with socket connection
        TODO: Return connection result
        """
        pass

    def list_tunnels(self):
        """
        Display all active tunnels.

        TODO: Iterate through active_tunnels
        TODO: Print tunnel details (ID, ports, route)
        TODO: Show tunnel status for each
        """
        pass

    def close_tunnel(self, tunnel_id):
        """
        Close specific tunnel.

        Args:
            tunnel_id: ID of tunnel to close

        TODO: Terminate tunnel process
        TODO: Remove from active_tunnels
        """
        pass

    def close_all(self):
        """
        Close all active tunnels.

        TODO: Iterate and close all tunnels
        TODO: Clear active_tunnels dictionary
        """
        pass

def main():
    """
    Interactive tunnel management interface.

    TODO: Create TunnelManager instance
    TODO: Implement command loop (create, list, close, exit)
    TODO: Handle user input and execute commands
    TODO: Display tunnel status and diagnostics
    """
    pass

if __name__ == "__main__":
    main()
```

---

### Step 3.2 — Create RDP Connection Simulator

```python
#!/usr/bin/env python3
"""
RDP Connection Simulator
Simulates RDP access through SSH tunnels
"""

import socket
import time
import sys
from datetime import datetime

class RDPSimulator:
    def __init__(self, target_host, target_port=3389):
        """
        Initialize RDP connection simulator.

        Args:
            target_host: Target host (localhost for tunnel)
            target_port: RDP port (tunnel local port)
        """
        self.target_host = target_host
        self.target_port = target_port
        self.connected   = False

    def test_rdp_port(self):
        """
        Test RDP port accessibility.

        Returns:
            bool: Port accessibility status

        TODO: Create socket connection test
        TODO: Test connection to target_host:target_port
        TODO: Add 5 second timeout
        TODO: Return result
        """
        pass

    def simulate_handshake(self):
        """
        Simulate RDP connection handshake.

        Returns:
            bool: Handshake success status

        TODO: Simulate handshake phases:
        TODO:   1. Connection Initiation
        TODO:   2. Basic Settings Exchange
        TODO:   3. Channel Connection
        TODO:   4. RDP Security Commencement
        TODO: Log each phase with small delays
        TODO: Set connected status on success
        """
        pass

    def execute_command(self, command):
        """
        Simulate command execution via RDP.

        Args:
            command: Command to execute

        TODO: Check connection status
        TODO: Log command execution with timestamp
        TODO: Simulate command output delay
        TODO: Return simulated output
        """
        pass

    def disconnect(self):
        """
        Disconnect RDP session.

        TODO: Check if connected
        TODO: Log disconnection with timestamp
        TODO: Reset connection status
        """
        pass

def main():
    """
    RDP simulator demonstration.

    TODO: Parse command line arguments
    TODO: Create RDPSimulator instance
    TODO: Test port, connect, execute commands
    TODO: Disconnect when complete
    """
    pass

if __name__ == "__main__":
    main()
```

---

### Step 3.3 — Test Tunnel and RDP Simulation

```bash
# 🔐 Make scripts executable
chmod +x tunnel_manager.py rdp_simulator.py

# 🔀 Create tunnel (complete implementation first)
python3 tunnel_manager.py
# In interactive mode:
# > create
# Jump host IP: 192.168.100.10
# Username: root
# Password: password123
# Target host: 192.168.100.20
# > list

# 💻 Test RDP through tunnel (complete implementation first)
python3 rdp_simulator.py localhost 8389
```

---

## 🤖 Task 4 — Automate Complete Pivoting Workflow

> 🔎 **Overview:** Create an **automated framework** to orchestrate multi-stage pivoting campaigns.

### Step 4.1 — Create Automation Framework

```python
#!/usr/bin/env python3
"""
Pivot Automation Framework
Orchestrates complex multi-hop pivoting scenarios
"""

import json
import sys
from datetime import datetime

class PivotAutomation:
    def __init__(self, config_file=None):
        """
        Initialize pivoting automation framework.

        Args:
            config_file: JSON configuration file path
        """
        self.targets = []
        self.results = {}

    def load_config(self, config_file):
        """
        Load configuration from JSON file.

        Args:
            config_file: Path to config file

        TODO: Read and parse JSON configuration
        TODO: Load target list and settings
        TODO: Validate configuration (required fields)
        TODO: Store targets internally
        """
        pass

    def scan_network(self, network_range):
        """
        Scan network for accessible targets.

        Args:
            network_range: CIDR network range (e.g., 192.168.100.0/24)

        Returns:
            list: List of accessible hosts

        TODO: Parse network range (use ipaddress library)
        TODO: Scan each IP for open ports 22, 445, 3389
        TODO: Return list of accessible targets
        """
        pass

    def execute_lateral_movement(self, target):
        """
        Execute lateral movement to target.

        Args:
            target: Target dictionary with credentials

        Returns:
            dict: Movement results

        TODO: Test connectivity to target
        TODO: Authenticate to target
        TODO: Execute reconnaissance commands
        TODO: Gather system information
        TODO: Return results dictionary
        """
        pass

    def create_pivot_chain(self, targets):
        """
        Create multi-hop pivot chain.

        Args:
            targets: List of targets in chain (ordered)

        Returns:
            bool: Chain creation status

        TODO: Create tunnel to first target
        TODO: Use first target to reach second
        TODO: Continue chain through all targets
        TODO: Test connectivity at each hop
        """
        pass

    def generate_report(self):
        """
        Generate pivoting activity report.

        Returns:
            str: Report content

        TODO: Compile all results
        TODO: Format report with timestamps
        TODO: Include success/failure statistics
        TODO: List all hosts compromised
        TODO: Document pivot chains used
        """
        pass

def main():
    """
    Main automation workflow.

    TODO: Parse command line arguments
    TODO: Load configuration
    TODO: Execute pivoting workflow
    TODO: Generate and save report
    """
    pass

if __name__ == "__main__":
    main()
```

---

### Step 4.2 — Create Configuration File

```json
{
  "targets": [
    {
      "name": "target1",
      "ip": "192.168.100.10",
      "username": "root",
      "password": "password123",
      "role": "jump_host",
      "port": 22
    },
    {
      "name": "target2",
      "ip": "192.168.100.20",
      "username": "root",
      "password": "password123",
      "role": "final_target",
      "port": 22
    }
  ],
  "options": {
    "timeout": 30,
    "retry_attempts": 3,
    "log_file": "pivot_results.log",
    "create_tunnels": true,
    "tunnel_ports": [8389, 8445]
  }
}
```

---

### Step 4.3 — Execute Automated Pivoting

```bash
# 🤖 Complete all script implementations first
chmod +x pivot_automation.py

# ▶️ Run automated pivoting
python3 pivot_automation.py pivot_config.json

# 📄 Review results
cat pivot_results.log
```

---

## ✔️ Expected Outcomes

After completing this lab, students should have:

| # | Deliverable | Status |
|---|---|---|
| 1 | ⚙️ Functional PsExec and WMI lateral movement tools | ✅ |
| 2 | 🔐 Working SSH tunnel manager for network pivoting | ✅ |
| 3 | 💻 RDP connection simulator for testing tunnels | ✅ |
| 4 | 🤖 Automated pivoting framework with configuration support | ✅ |
| 5 | 🗺️ Understanding of multi-hop pivoting techniques | ✅ |
| 6 | 🛡️ Experience with OPSEC considerations in lateral movement | ✅ |

---

## 🛠️ Troubleshooting

<details>
<summary>❌ Connection Failures</summary>

**Cause:** Docker containers not running or network misconfigured.

**Fix:**

```bash
# ✅ Verify Docker containers are running
docker ps

# ✅ Check network connectivity
docker network inspect pivot-lab

# ✅ Ensure SSH service is active in containers
docker exec target1 service ssh status

# ✅ Test direct SSH connection
ssh root@192.168.100.10
```

</details>

<details>
<summary>❌ Tunnel Issues</summary>

**Cause:** sshpass not installed, port in use, or SSH connectivity problems.

**Fix:**

```bash
# ✅ Verify sshpass is installed
which sshpass
sudo apt install -y sshpass  # If not installed

# ✅ Check if local port is already in use
netstat -tuln | grep <port>
lsof -i :<port>

# ✅ Test SSH connectivity manually
ssh -v root@192.168.100.10
sshpass -p password123 ssh root@192.168.100.10
```

</details>

<details>
<summary>❌ Script Errors</summary>

**Cause:** Missing permissions, dependencies, or syntax errors.

**Fix:**

```bash
# ✅ Ensure all scripts are executable
chmod +x *.py

# ✅ Verify Python dependencies
pip3 list | grep impacket
pip3 install impacket

# ✅ Check for syntax errors
python3 -m py_compile psexec_tool.py
python3 -m py_compile wmi_tool.py
```

</details>

---

## 🏁 Conclusion

This lab provided **hands-on experience** with network pivoting and lateral movement techniques — critical skills for penetration testers and security professionals.

```
┌───────────────────────────────────────────────────────────┐
│  ⚙️  PsExec        →  Remote command execution            │
│  📡 WMI           →  Windows Management Instrumentation   │
│  🔐 SSH Tunnels   →  Multi-hop encrypted pivoting        │
│  💻 RDP Pivoting  →  Remote desktop access via tunnels   │
│  🤖 Automation    →  Orchestrate complex campaigns       │
└───────────────────────────────────────────────────────────┘
```

### 🔑 Key Takeaways

- 🔀 **Lateral movement** enables attackers to reach objectives across networks
- 🔐 **SSH tunnels** provide encrypted pivot chains for covert access
- 🤖 **Automation** makes complex multi-stage attacks reproducible
- 🛡️ **OPSEC** — minimize artifacts and maintain stealth during pivoting
- 🔍 **Detection** — monitor for lateral movement patterns and anomalies

### 🛡️ OPSEC Best Practices

| Practice | Purpose |
|---|---|
| 🎭 Living off the Land | Use built-in tools (cmd, powershell, ssh) |
| 🔇 Disable Logging | Clear event logs at final stage (risky) |
| 🎯 Time Windows | Pivot during business hours (blend in) |
| 💻 Tool Staging | Deploy tools only when needed |
| 🗑️ Cleanup | Remove artifacts and close tunnels |

### 🚀 Next Steps

- 🔧 Practice **multi-stage pivoting** with more targets
- 📊 Study **network reconnaissance** tools (nmap, enum4linux)
- 🔐 Explore **NTLM relay attacks** with Responder
- 📈 Scale automation for **enterprise-wide** scenarios
- 🎓 Study **detection evasion** techniques

### 🧹 Cleanup

```bash
# Stop and remove containers
cd ~/pivot-lab
docker-compose down

# Remove network
docker network rm pivot-lab

# Remove lab files (optional)
rm -rf ~/pivot-lab
```

---

<div align="center">

---

🔐 **Al Nafi Cybersecurity Training Platform**

*Empowering the Next Generation of Cyber Defenders*

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Red%20Team%20Operations-red?style=for-the-badge&logo=shield&logoColor=white)
![MITRE](https://img.shields.io/badge/MITRE%20ATT%26CK-T1570%20%7C%20T1021%20%7C%20T1080-darkred?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Impacket](https://img.shields.io/badge/Impacket-Toolkit-red?style=flat-square&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?style=flat-square&logo=docker&logoColor=white)
![SSH](https://img.shields.io/badge/SSH-Tunneling-black?style=flat-square&logo=openssh&logoColor=white)
![RDP](https://img.shields.io/badge/RDP-Pivoting-0078D4?style=flat-square&logo=microsoft&logoColor=white)
![Kali Linux](https://img.shields.io/badge/Kali%20Linux-Penetration%20Testing-557C94?style=flat-square&logo=kalilinux&logoColor=white)

*© Al Nafi — For educational and authorized lab use only.*

</div>
