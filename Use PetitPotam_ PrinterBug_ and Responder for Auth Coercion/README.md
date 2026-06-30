# 🔴 Authentication Coercion with PetitPotam, PrinterBug & Responder

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-red?style=for-the-badge&logo=shield&logoColor=white)
![Lab Type](https://img.shields.io/badge/Lab%20Type-Red%20Team-darkred?style=for-the-badge&logo=target&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Advanced-critical?style=for-the-badge&logo=buffer&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Ubuntu%2022.04%20LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Impacket](https://img.shields.io/badge/Impacket-Toolkit-red?style=flat-square&logo=python&logoColor=white)
![Responder](https://img.shields.io/badge/Responder-Hash%20Capture-FF6B35?style=flat-square&logo=gnubash&logoColor=white)
![RPC](https://img.shields.io/badge/RPC-MS--EFSRPC%20%2F%20MS--RPRN-blue?style=flat-square&logo=microsoft&logoColor=white)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE%20ATT%26CK-T1187%20%7C%20T1040%20%7C%20T1557-red?style=flat-square&logo=databricks&logoColor=white)
![Tactic](https://img.shields.io/badge/Tactic-Credential%20Access%20%2F%20Network%20Abuse-purple?style=flat-square&logo=gnubash&logoColor=white)
![License](https://img.shields.io/badge/License-Educational-green?style=flat-square&logo=bookstack&logoColor=white)

</div>

---

## 📋 Table of Contents

- [🎯 Objectives](#-objectives)
- [✅ Prerequisites](#-prerequisites)
- [🧪 Lab Environment](#-lab-environment)
- [🔑 Task 1 — Authentication Coercion Fundamentals](#-task-1--understanding-authentication-coercion)
- [📧 Task 2 — PetitPotam Attack](#-task-2--implement-petitpotam-attack)
- [🖨️ Task 3 — PrinterBug Attack](#️-task-3--implement-printerbug-attack)
- [🎯 Task 4 — Responder Hash Capture](#-task-4--configure-responder-for-hash-capture)
- [🛡️ Task 5 — Detection & Defense](#️-task-5--implement-defensive-measures)
- [✔️ Expected Outcomes](#️-expected-outcomes)
- [🛠️ Troubleshooting](#️-troubleshooting)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

By the end of this lab, students will be able to:

- 🔑 Understand **Windows authentication coercion** attack vectors
- 📧 Implement **PetitPotam (MS-EFSRPC)** coercion techniques
- 🖨️ Utilize **PrinterBug (MS-RPRN)** for forced authentication
- 🎯 Configure **Responder** to capture NetNTLMv2 hashes
- 🔍 Analyze captured authentication data for **security assessments**

---

## ✅ Prerequisites

| Requirement | Details |
|---|---|
| 🏢 AD Knowledge | Basic understanding of Windows Active Directory and NTLM authentication |
| 🐍 Python | Familiarity with Python programming |
| 🌐 Network Protocols | Knowledge of network protocols (SMB, RPC) |
| 💻 CLI Skills | Linux command-line experience |

---

## 🧪 Lab Environment

> 💡 **Ready-to-Use Cloud Machines:** Al Nafi provides **Ubuntu 22.04 LTS** machines with pre-installed tools. Click **▶ Start Lab** to begin.

| Component | Details |
|---|---|
| 🐍 Python | 3.10+ with all required libraries |
| 🧰 Impacket Toolkit | Windows protocol exploitation |
| 🎯 Responder Framework | Hash capture and NTLM relay |
| 🌐 Simulated Network | Safe environment for testing |
| 📂 Pre-loaded Tools | All scripts and sample data included |

---

## 🔑 Task 1 — Understanding Authentication Coercion

> 🔎 **Overview:** Authentication coercion attacks **force Windows systems** to authenticate to attacker-controlled servers, enabling credential capture and relay attacks.
> **MITRE ATT&CK:** [T1187 – Forced Authentication](https://attack.mitre.org/techniques/T1187/)

### 🎯 Key Attack Vectors

```
┌──────────────────────────────────────────────────────────┐
│  📧 PetitPotam (MS-EFSRPC)                               │
│     → Exploits Encrypted File System Remote Protocol     │
│     → EFS functions with UNC paths                       │
│                                                          │
│  🖨️  PrinterBug (MS-RPRN)                                │
│     → Exploits Print System Remote Protocol              │
│     → Printer change notifications                       │
│                                                          │
│  🔐 NetNTLM Challenge-Response                           │
│     → Captured by attacker listener                      │
│     → Cracked or relayed for access                      │
└──────────────────────────────────────────────────────────┘
```

---

### Step 1 — Set Up Lab Environment

```bash
# 📁 Create working directory
mkdir ~/auth-coercion-lab && cd ~/auth-coercion-lab

# ✅ Verify installations
python3 -c "import impacket; print('Impacket:', impacket.__version__)"
responder -h | head -5
```

---

### Step 2 — Configure Network Simulation

```bash
# 🌐 Add IP aliases for simulation (allows testing on single machine)
sudo ip addr add 127.0.0.2/8 dev lo
sudo ip addr add 127.0.0.3/8 dev lo

# ✅ Verify configuration
ip addr show lo | grep "127.0.0"
```

---

### Step 3 — Create Configuration File

```python
# lab_config.py
class LabConfig:
    '''Configuration for authentication coercion lab'''

    def __init__(self):
        self.attacker_ip = "127.0.0.1"
        self.target_ip   = "127.0.0.2"
        self.domain      = "TESTDOMAIN"
        self.interface   = "lo"

    def display_config(self):
        '''Display current configuration'''
        # TODO: Print configuration details
        #   - Attacker IP
        #   - Target IP
        #   - Domain name
        #   - Interface name
        pass

if __name__ == "__main__":
    config = LabConfig()
    config.display_config()
```

---

## 📧 Task 2 — Implement PetitPotam Attack

> 🔎 **Overview:** PetitPotam exploits **MS-EFSRPC** to coerce authentication by calling EFS functions with UNC paths pointing to attacker-controlled servers.
> **CVE:** CVE-2021-36942 | **MITRE:** [T1187 – Forced Authentication](https://attack.mitre.org/techniques/T1187/)

### 📋 Attack Flow

```
Attacker                          Target DC
  │                                 │
  │  1️⃣  Connect to MS-EFSRPC      │
  ├──────────────────────────────►│
  │                                 │
  │  2️⃣  Call EFS function          │
  │      with UNC path to listener   │
  ├──────────────────────────────►│
  │                                 │
  │  3️⃣  Target authenticates       │
  │      to listener IP             │
  │                                 │
  │◄──────────────────────────────┤
  │  4️⃣  NetNTLMv2 hash captured!  │
```

---

### Step 1 — Create PetitPotam Implementation

```python
#!/usr/bin/env python3
"""
PetitPotam Authentication Coercion Implementation
Exploits MS-EFSRPC protocol for forced authentication
"""

import sys
import time

class PetitPotam:
    '''PetitPotam attack implementation'''

    def __init__(self, target_ip, listener_ip):
        self.target_ip   = target_ip
        self.listener_ip = listener_ip
        self.efs_functions = [
            'EfsRpcOpenFileRaw',
            'EfsRpcEncryptFileSrv',
            'EfsRpcDecryptFileSrv'
        ]

    def create_unc_path(self):
        '''
        Generate UNC path for coercion

        Returns:
            str: UNC path pointing to listener

        TODO: Create UNC path with listener IP
        TODO: Format: \\\\<listener_ip>\\share\\file.txt
        TODO: Return formatted path
        '''
        pass

    def simulate_efsrpc_call(self, function_name, unc_path):
        '''
        Simulate EFS RPC function call

        Args:
            function_name: EFS function to call
            unc_path:      UNC path for coercion

        Returns:
            bool: Success status

        TODO: Simulate RPC connection to target
        TODO: Send EFS function call with UNC path
        TODO: Return success/failure status
        '''
        pass

    def execute_attack(self):
        '''
        Execute PetitPotam attack sequence
        '''
        print(f"[PETITPOTAM] Targeting: {self.target_ip}")
        print(f"[PETITPOTAM] Listener: {self.listener_ip}")

        # TODO: Iterate through EFS functions
        # TODO: Call simulate_efsrpc_call for each function
        # TODO: Display results with timing
        pass

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 petitpotam.py <target_ip> <listener_ip>")
        sys.exit(1)

    # TODO: Parse command-line arguments
    # TODO: Create PetitPotam instance
    # TODO: Execute attack
    pass

if __name__ == "__main__":
    main()
```

---

### Step 2 — Test PetitPotam

```bash
# 📧 Make executable
chmod +x petitpotam.py

# ▶️ Run simulation
python3 petitpotam.py 127.0.0.2 127.0.0.1
```

---

### Step 3 — Analyze Attack Flow

```
Attack Sequence:
1️⃣  Attacker connects to target's MS-EFSRPC service
2️⃣  Calls EFS function with UNC path to attacker server
3️⃣  Target attempts to authenticate to attacker server
4️⃣  Responder captures NetNTLMv2 hash
```

---

## 🖨️ Task 3 — Implement PrinterBug Attack

> 🔎 **Overview:** PrinterBug exploits **MS-RPRN (Print Spooler)** service using `RpcRemoteFindFirstPrinterChangeNotificationEx` to force authentication.
> **AKA:** SpoolSample | **MITRE:** [T1187 – Forced Authentication](https://attack.mitre.org/techniques/T1187/)

### 📋 Attack Flow

```
Attacker                          Target DC
  │                                 │
  │  1️⃣  Connect to Print Spooler   │
  ├──────────────────────────────►│
  │                                 │
  │  2️⃣  Send printer notification  │
  │      with listener UNC path     │
  ├──────────────────────────────►│
  │                                 │
  │  3️⃣  Spooler sends auth to      │
  │      listener                   │
  │                                 │
  │◄──────────────────────────────┤
  │  4️⃣  NetNTLMv2 hash captured!  │
```

---

### Step 1 — Create PrinterBug Implementation

```python
#!/usr/bin/env python3
"""
PrinterBug (SpoolSample) Implementation
Exploits MS-RPRN for authentication coercion
"""

import sys
import time

class PrinterBug:
    '''PrinterBug attack implementation'''

    def __init__(self, target_ip, listener_ip):
        self.target_ip   = target_ip
        self.listener_ip = listener_ip
        self.rprn_port   = 445

    def create_notification_request(self):
        '''
        Create printer change notification request

        Returns:
            dict: Request parameters

        TODO: Create request dictionary with:
        TODO:   - function name (RpcRemoteFindFirstPrinterChangeNotificationEx)
        TODO:   - printer name (\\\\target\\printer)
        TODO:   - notification server (\\\\listener\\pipe\\spoolss)
        TODO:   - change flags
        '''
        pass

    def simulate_rprn_connection(self):
        '''
        Simulate connection to print spooler

        Returns:
            bool: Connection status

        TODO: Simulate RPC connection to target spooler
        TODO: Authenticate to service
        TODO: Return connection status
        '''
        pass

    def send_notification_request(self):
        '''
        Send printer change notification

        Returns:
            bool: Request status

        TODO: Create notification request
        TODO: Send request to target
        TODO: Target should authenticate to listener
        '''
        pass

    def execute_attack(self):
        '''Execute PrinterBug attack sequence'''
        print(f"[PRINTERBUG] Target: {self.target_ip}")
        print(f"[PRINTERBUG] Listener: {self.listener_ip}")

        # TODO: Connect to print spooler
        # TODO: Send notification request
        # TODO: Display results
        pass

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 printerbug.py <target_ip> <listener_ip>")
        sys.exit(1)

    # TODO: Parse arguments
    # TODO: Create PrinterBug instance
    # TODO: Execute attack
    pass

if __name__ == "__main__":
    main()
```

---

### Step 2 — Test PrinterBug

```bash
# 🖨️ Make executable
chmod +x printerbug.py

# ▶️ Run simulation
python3 printerbug.py 127.0.0.2 127.0.0.1
```

---

### Step 3 — Compare Attack Vectors

| Feature | PetitPotam | PrinterBug |
|---|---|---|
| **Protocol** | 📧 MS-EFSRPC | 🖨️ MS-RPRN |
| **Service** | Encrypted File System | Print Spooler |
| **Authentication** | ✅ Optional | ✅ Required |
| **Patched** | CVE-2021-36942 | ⚠️ Partially |
| **Stealth** | 🟢 High | 🟡 Medium |

---

## 🎯 Task 4 — Configure Responder for Hash Capture

> 🔎 **Overview:** Responder captures **NetNTLMv2 hashes** by responding to authentication requests from coerced targets — enabling offline cracking or relay attacks.
> **MITRE:** [T1040 – Network Sniffing](https://attack.mitre.org/techniques/T1040/) | [T1557 – Man-in-the-Middle](https://attack.mitre.org/techniques/T1557/)

---

### Step 1 — Create Responder Manager

```python
#!/usr/bin/env python3
"""
Responder Management and Hash Capture Tool
"""

import subprocess
import time
import re

class ResponderManager:
    '''Manage Responder for hash capture'''

    def __init__(self, interface='lo'):
        self.interface = interface
        self.process = None
        self.captured_hashes = []

    def start_responder(self, options=None):
        '''
        Start Responder with specified options

        Args:
            options: List of Responder command-line options

        Returns:
            bool: Success status

        TODO: Build Responder command with options
        TODO: Include interface, IP address, output file
        TODO: Start subprocess
        TODO: Return status
        '''
        pass

    def monitor_output(self, duration=30):
        '''
        Monitor Responder output for hash captures

        Args:
            duration: Monitoring duration in seconds

        Returns:
            list: Captured hashes

        TODO: Read Responder output
        TODO: Parse for NetNTLMv2 hashes
        TODO: Store captured hashes
        TODO: Return list of hashes
        '''
        pass

    def stop_responder(self):
        '''Stop Responder process

        TODO: Terminate Responder subprocess
        TODO: Wait for graceful shutdown
        '''
        pass

    def simulate_capture(self):
        '''
        Simulate hash capture for demonstration

        Returns:
            list: Simulated captured hashes

        TODO: Generate sample NetNTLMv2 hashes
        TODO: Display capture events
        TODO: Return simulated hashes
        '''
        pass

def main():
    print("[RESPONDER] Hash Capture Demonstration")

    # TODO: Create ResponderManager instance
    # TODO: Start Responder or run simulation
    # TODO: Monitor for captures
    # TODO: Display results
    pass

if __name__ == "__main__":
    main()
```

---

### Step 2 — Create Hash Analysis Tool

```python
#!/usr/bin/env python3
"""
NetNTLMv2 Hash Analysis Tool
Parses and formats captured hashes for cracking
"""

import re

class HashAnalyzer:
    '''Analyze captured NetNTLMv2 hashes'''

    def __init__(self):
        # NetNTLMv2 format: username::domain:challenge:response
        self.hash_pattern = r'([^:]+)::([^:]+):([a-fA-F0-9]{16}):([a-fA-F0-9]{32}):([a-fA-F0-9]+)'

    def parse_hash(self, hash_string):
        '''
        Parse NetNTLMv2 hash components

        Args:
            hash_string: NetNTLMv2 hash string

        Returns:
            dict: Parsed hash components

        TODO: Match hash pattern
        TODO: Extract username, domain, challenge, response
        TODO: Return dictionary with components
        '''
        pass

    def format_for_hashcat(self, hash_string):
        '''
        Format hash for Hashcat cracking

        Args:
            hash_string: NetNTLMv2 hash

        Returns:
            str: Hashcat-formatted hash

        TODO: Parse hash components
        TODO: Format for Hashcat mode 5600 (NTLMv2)
        TODO: Return formatted string
        '''
        pass

    def analyze_batch(self, hash_file):
        '''
        Analyze multiple hashes from file

        Args:
            hash_file: Path to file with captured hashes

        Returns:
            list: Analysis results

        TODO: Read hashes from file
        TODO: Parse each hash
        TODO: Generate statistics (count, unique users, etc.)
        TODO: Return analysis results
        '''
        pass

def main():
    # TODO: Create HashAnalyzer instance
    # TODO: Load sample hashes
    # TODO: Parse and analyze
    # TODO: Display results
    pass

if __name__ == "__main__":
    main()
```

---

### Step 3 — Test Complete Attack Chain

```bash
# 🖥️ Terminal 1: Start Responder (simulation mode)
python3 responder_manager.py

# 🖥️ Terminal 2: Execute PetitPotam
python3 petitpotam.py 127.0.0.2 127.0.0.1

# 🖥️ Terminal 3: Execute PrinterBug
python3 printerbug.py 127.0.0.2 127.0.0.1

# 🔍 Analyze captured hashes
python3 hash_analyzer.py captured_hashes.txt
```

---

## 🛡️ Task 5 — Implement Defensive Measures

> **MITRE:** [T1562 – Impair Defenses](https://attack.mitre.org/techniques/T1562/) (detection focus)

### Step 1 — Create Detection Script

```python
#!/usr/bin/env python3
"""
Authentication Coercion Detection Tool
Identifies PetitPotam and PrinterBug attack attempts
"""

class CoercionDetector:
    '''Detect authentication coercion attempts'''

    def __init__(self):
        self.suspicious_patterns = []
        self.alerts = []

    def monitor_rpc_calls(self):
        '''
        Monitor for suspicious RPC calls

        Returns:
            list: Detected suspicious activities

        TODO: Monitor MS-EFSRPC calls
        TODO: Monitor MS-RPRN calls
        TODO: Detect unusual UNC path access
        TODO: Return alerts
        '''
        pass

    def check_spooler_status(self):
        '''
        Check Print Spooler service status

        Returns:
            dict: Service status information

        TODO: Query Print Spooler service
        TODO: Check if service is running
        TODO: Return status
        '''
        pass

    def recommend_mitigations(self):
        '''
        Provide mitigation recommendations

        Returns:
            list: Recommended security measures

        TODO: Generate mitigation list
        TODO: Include service hardening steps
        TODO: Return recommendations
        '''
        pass

def main():
    # TODO: Create detector instance
    # TODO: Run detection checks
    # TODO: Display findings and recommendations
    pass

if __name__ == "__main__":
    main()
```

---

### Step 2 — Document Mitigation Strategies

| Mitigation | Priority | Details |
|---|---|---|
| 🔴 Disable Print Spooler | Critical | Stop and disable on non-print servers |
| 🔴 Apply Patches | Critical | Install KB5005010 and later updates |
| 🟠 Network Segmentation | High | Restrict RPC access between systems |
| 🟠 Monitor Authentication | High | Alert on unusual authentication patterns |
| 🟡 Disable NTLM | Medium | Use Kerberos where possible |

---

### Step 3 — Test Detection Capabilities

```bash
# 🔍 Run detection script
python3 detect_coercion.py

# 🔎 Check Print Spooler status
sudo systemctl status spooler

# 📋 Review recommendations
python3 detect_coercion.py --recommendations
```

---

## ✔️ Expected Outcomes

After completing this lab, students should have:

| # | Deliverable | Status |
|---|---|---|
| 1 | 📧 Working PetitPotam attack implementation | ✅ |
| 2 | 🖨️ Functional PrinterBug attack implementation | ✅ |
| 3 | 🎯 Responder configured for hash capture | ✅ |
| 4 | 🔍 Hash analysis tools for captured credentials | ✅ |
| 5 | 🛡️ Detection scripts for coercion attempts | ✅ |
| 6 | 📄 Understanding of defensive measures | ✅ |

### 📊 Sample Successful Output

```
[PETITPOTAM] Coercion successful
[RESPONDER] NetNTLMv2 captured: testuser::DOMAIN:challenge:response
[ANALYZER] Hash formatted for cracking (Hashcat mode 5600)
[DETECTOR] Suspicious RPC activity detected - Event ID 5145
```

---

## 🛠️ Troubleshooting

<details>
<summary>❌ Responder not capturing hashes</summary>

**Cause:** Network interface misconfiguration or firewall blocking.

**Fix:**

```bash
# ✅ Verify network interface configuration
ip addr show lo | grep 127.0.0

# ✅ Check firewall rules allow SMB traffic
sudo ufw status
sudo ufw allow 445/tcp

# ✅ Ensure target can reach listener IP
ping 127.0.0.1
```

</details>

<details>
<summary>❌ Permission denied errors</summary>

**Cause:** Script permissions or Responder requires elevated privileges.

**Fix:**

```bash
# ✅ Make scripts executable
chmod +x *.py

# ✅ Run Responder with sudo
sudo responder -I lo -v

# ✅ Verify file permissions
ls -la *.py
```

</details>

<details>
<summary>❌ Connection timeouts</summary>

**Cause:** IP aliases not configured or services not listening.

**Fix:**

```bash
# ✅ Confirm IP aliases are configured
ip addr show lo | grep 127.0.0

# ✅ Check services listening on correct ports
sudo netstat -tlnp | grep :445

# ✅ Verify no port conflicts
lsof -i :445
```

</details>

---

## 🏁 Conclusion

This lab demonstrated **authentication coercion techniques** using PetitPotam and PrinterBug to force Windows systems to authenticate to attacker-controlled servers.

```
┌──────────────────────────────────────────────────────────┐
│  📧 PetitPotam    →  MS-EFSRPC coercion + hash capture   │
│  🖨️  PrinterBug    →  MS-RPRN coercion + hash capture    │
│  🎯 Responder     →  Hash capture and analysis           │
│  🛡️  Detection     →  Monitor RPC calls and services     │
└──────────────────────────────────────────────────────────┘
```

### 🔑 Key Takeaways

- 📧 **Authentication coercion exploits legitimate Windows protocols**
- 🔐 **Multiple attack vectors exist** (MS-EFSRPC, MS-RPRN)
- 🎯 **Captured hashes can be cracked or relayed** for access
- 🛡️ **Defense requires layered security controls**
- 🔄 **Regular patching and service hardening are essential**

### 🛡️ Defensive Recommendations

- ✋ **Disable Print Spooler** on non-print servers
- 🔐 **Apply security patches** (KB5005010+)
- 🌐 **Network segmentation** to restrict RPC access
- 👁️ **Monitor authentication patterns** and RPC calls
- 🔒 **Prefer Kerberos** over NTLM for authentication

### 🚀 Next Steps

- 💻 Practice **hash cracking** with Hashcat
- 🔄 Explore **NTLM relay attacks** (Impacket tools)
- 🏢 Implement **enterprise-wide mitigations**
- 🎓 Study **additional coercion techniques** (ADCSPwn, etc.)

---

<div align="center">

---

🔐 **Al Nafi Cybersecurity Training Platform**

*Empowering the Next Generation of Cyber Defenders*

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Red%20Team%20Operations-red?style=for-the-badge&logo=shield&logoColor=white)
![MITRE](https://img.shields.io/badge/MITRE%20ATT%26CK-T1187%20%7C%20T1040%20%7C%20T1557-darkred?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Impacket](https://img.shields.io/badge/Impacket-Toolkit-red?style=flat-square&logo=python&logoColor=white)
![Responder](https://img.shields.io/badge/Responder-Hash%20Capture-FF6B35?style=flat-square&logo=gnubash&logoColor=white)
![RPC](https://img.shields.io/badge/RPC-MS--EFSRPC%20%2F%20MS--RPRN-blue?style=flat-square&logo=microsoft&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04%20LTS-E95420?style=flat-square&logo=ubuntu&logoColor=white)

*© Al Nafi — For educational and authorized lab use only.*

</div>
