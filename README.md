<div align="center">

```
██████╗ ███████╗██████╗     ████████╗███████╗ █████╗ ███╗   ███╗
██╔══██╗██╔════╝██╔══██╗    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
██████╔╝█████╗  ██║  ██║       ██║   █████╗  ███████║██╔████╔██║
██╔══██╗██╔══╝  ██║  ██║       ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
██║  ██║███████╗██████╔╝       ██║   ███████╗██║  ██║██║ ╚═╝ ██║
╚═╝  ╚═╝╚══════╝╚═════╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
```

# 🔴 Red Team Operator
### Adversary Emulation & Attack Simulation Framework

*Simulate. Evade. Dominate. — Built for the modern offensive security operator.*

---

[![License](https://img.shields.io/badge/License-MIT-red.svg?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge&logo=statuspage)](/)
[![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-v15-orange?style=for-the-badge&logo=mitre)](https://attack.mitre.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20|%20Windows%20|%20macOS-blue?style=for-the-badge&logo=linux)](/)

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PowerShell](https://img.shields.io/badge/PowerShell-7.x-5391FE?style=for-the-badge&logo=powershell&logoColor=white)](https://github.com/PowerShell/PowerShell)
[![Bash](https://img.shields.io/badge/Bash-5.x-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)
[![C](https://img.shields.io/badge/C-17-A8B9CC?style=for-the-badge&logo=c&logoColor=white)](/)

[![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)](https://www.kali.org/)
[![Metasploit](https://img.shields.io/badge/Metasploit-Framework-E34F26?style=for-the-badge&logo=metasploit&logoColor=white)](https://www.metasploit.com/)
[![Cobalt Strike](https://img.shields.io/badge/Cobalt_Strike-Compatible-darkred?style=for-the-badge)](/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)

</div>

---

## ⚠️ Legal Disclaimer

> **This framework is intended strictly for authorized security testing, red team engagements, and educational research. Unauthorized use against systems you do not own or have explicit written permission to test is illegal and unethical. The authors assume no liability for misuse.**

---

## 🎯 Purpose

**Red Team Operator** is a comprehensive adversary emulation and attack simulation framework designed for professional red teamers, penetration testers, and security researchers. It enables teams to conduct realistic, structured offensive operations that mirror the tactics, techniques, and procedures (TTPs) of real-world threat actors — helping organizations understand and strengthen their true security posture.

The core philosophy: **think like an adversary, operate like a professional**.

---

## 🧠 What Is Adversary Emulation?

Adversary emulation goes beyond traditional penetration testing. Instead of simply finding vulnerabilities, this framework empowers operators to:

- **Replicate real threat actors** — APT groups, ransomware gangs, nation-state actors
- **Execute full kill-chain operations** — from initial access to exfiltration
- **Test detection and response capabilities** — not just defenses, but the humans behind them
- **Generate intelligence-driven reports** — actionable findings mapped to MITRE ATT&CK

---

## 🗂️ Framework Structure

```
red-team-operator/
├── 📁 recon/                  # OSINT & reconnaissance modules
│   ├── passive/               # Shodan, WHOIS, DNS enumeration
│   └── active/                # Port scanning, service fingerprinting
├── 📁 initial-access/         # Phishing, exploits, supply chain
│   ├── phishing/              # Email & credential harvesting
│   └── exploits/              # CVE-based exploitation modules
├── 📁 execution/              # Payload delivery & code execution
│   ├── loaders/               # Shellcode loaders (BYOL)
│   └── evasion/               # AV/EDR bypass techniques
├── 📁 persistence/            # Scheduled tasks, registry, startup
├── 📁 lateral-movement/       # Pass-the-hash, Kerberoasting, pivoting
├── 📁 c2/                     # Command & Control infrastructure
│   ├── profiles/              # Malleable C2 profiles
│   └── redirectors/           # NGINX/Apache redirector configs
├── 📁 exfiltration/           # Data staging & exfil modules
├── 📁 reporting/              # Automated report generation
├── 📁 playbooks/              # Pre-built adversary emulation plans
│   ├── apt29/                 # Cozy Bear emulation
│   ├── lazarus/               # Lazarus Group TTPs
│   └── fin7/                  # FIN7 financial sector TTPs
└── 📁 utils/                  # Shared utilities & helpers
```

---

## ⚙️ Core Capabilities

### 🔍 Reconnaissance
- Passive OSINT gathering (LinkedIn, Shodan, Certificate Transparency)
- Active network scanning and service enumeration
- Attack surface mapping and asset discovery

### 🎣 Initial Access
- Spearphishing simulation (email, SMS, voice)
- Exploitation of public-facing applications
- Trusted relationship and supply chain attacks

### 🐚 Execution & Evasion
- BYOL (Bring Your Own Loader) shellcode execution
- Process injection (DLL, reflective, process hollowing)
- AV/EDR evasion — AMSI bypass, ETW patching, unhooking
- Living-off-the-land (LOLBins) techniques

### 🔁 Persistence & Privilege Escalation
- Registry-based persistence
- Scheduled task and service installation
- Token impersonation and local privilege escalation

### 🌐 Lateral Movement
- Pass-the-Hash / Pass-the-Ticket
- Kerberoasting & AS-REP Roasting
- WMI, PSExec, and SMB lateral movement
- SSH tunneling and SOCKS proxying

### 📡 Command & Control (C2)
- Malleable C2 profile library
- HTTPS/DNS/HTTP C2 channel support
- Redirector configuration templates (Nginx, Apache, Caddy)
- Domain fronting setup guides

### 📦 Exfiltration
- Staged data collection and compression
- Encrypted exfil over HTTPS/DNS
- Cloud storage exfiltration simulation (S3, OneDrive, Dropbox)

---

## 🗺️ MITRE ATT&CK Coverage

This framework maps all techniques to the **MITRE ATT&CK Enterprise Matrix**.

| Tactic | Coverage | Key Techniques |
|--------|----------|----------------|
| Reconnaissance | ✅ Full | T1595, T1596, T1598 |
| Initial Access | ✅ Full | T1566, T1190, T1195 |
| Execution | ✅ Full | T1059, T1203, T1204 |
| Persistence | ✅ Full | T1053, T1543, T1547 |
| Privilege Escalation | 🔶 Partial | T1055, T1068, T1134 |
| Defense Evasion | ✅ Full | T1027, T1055, T1562 |
| Credential Access | ✅ Full | T1003, T1110, T1558 |
| Lateral Movement | ✅ Full | T1021, T1550, T1534 |
| Collection | 🔶 Partial | T1005, T1039, T1560 |
| C2 | ✅ Full | T1071, T1090, T1095 |
| Exfiltration | ✅ Full | T1041, T1048, T1567 |

---

## 🚀 Quick Start

### Prerequisites

```bash
# Minimum Requirements
Python >= 3.11
Go >= 1.21
Docker >= 24.x
```

### Installation

```bash
# Clone the repository
git clone https://github.com/your-org/red-team-operator.git
cd red-team-operator

# Install Python dependencies
pip install -r requirements.txt

# Build Go tooling
make build-tools

# Initialize the framework
./rto.sh init
```

### Run Your First Emulation

```bash
# List available adversary playbooks
./rto.sh playbook list

# Execute APT29 emulation plan (dry-run)
./rto.sh playbook run --actor apt29 --phase recon --dry-run

# Start a full operation
./rto.sh op new --name "IRON TEMPEST" --target 192.168.1.0/24
```

---

## 📋 Adversary Playbooks

Pre-built emulation plans based on real-world threat intelligence:

| Threat Actor | Sector Target | Complexity | Status |
|---|---|---|---|
| APT29 (Cozy Bear) | Government, Think Tanks | 🔴 High | ✅ Ready |
| APT41 | Tech, Healthcare | 🔴 High | ✅ Ready |
| Lazarus Group | Finance, Crypto | 🟠 Medium | ✅ Ready |
| FIN7 | Retail, Hospitality | 🟠 Medium | ✅ Ready |
| Scattered Spider | Cloud, Telco | 🔴 High | 🔧 WIP |
| LockBit 3.0 | Cross-sector | 🔴 High | ✅ Ready |

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=flat-square&logo=powershell&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)

![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=flat-square&logo=kalilinux&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat-square&logo=windows&logoColor=white)

</div>

---

## 📊 Reporting

Every operation generates structured output:

- **Operator Logs** — Timestamped command history with context
- **MITRE ATT&CK Navigator Layer** — Visual heatmap of executed techniques
- **Executive Summary** — Business-impact oriented findings
- **Technical Report** — Full kill-chain narrative with evidence
- **Purple Team Report** — Detection gap analysis for blue team

---

## 🤝 Contributing

Contributions are welcome from the security community.

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/new-technique`)
3. Follow the [contribution guidelines](CONTRIBUTING.md)
4. Submit a pull request with a clear description

All new modules **must** include:
- MITRE ATT&CK technique mapping
- Tested on at least two target platforms
- Documented in the module header

---

## 📚 References & Resources

- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [Red Team Development & Operations](https://redteam.guide/)
- [Adversary Emulation Library (CTID)](https://github.com/center-for-threat-informed-defense/adversary_emulation_library)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
- [OPSEC Considerations for Beacon Operators](https://www.cobaltstrike.com/blog/)

---

## 📄 License

```
MIT License — Use responsibly, test legally, report ethically.
```

---

<div align="center">

**Built with ☕ and controlled chaos by the Red Team community.**

*"The red team exists not to attack, but to reveal truth."*

[![Star this repo](https://img.shields.io/github/stars/your-org/red-team-operator?style=social)](/)
[![Follow](https://img.shields.io/twitter/follow/your-handle?style=social)](/)

</div>
