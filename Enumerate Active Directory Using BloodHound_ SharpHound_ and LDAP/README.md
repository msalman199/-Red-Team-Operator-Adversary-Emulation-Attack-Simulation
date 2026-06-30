# 🔴 Enumerate Active Directory Using BloodHound, SharpHound & LDAP

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-red?style=for-the-badge&logo=shield&logoColor=white)
![Lab Type](https://img.shields.io/badge/Lab%20Type-Red%20Team-darkred?style=for-the-badge&logo=target&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=for-the-badge&logo=buffer&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux%20%2F%20AD%20Sim-blue?style=for-the-badge&logo=linux&logoColor=white)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![BloodHound](https://img.shields.io/badge/BloodHound-v4.3.1-red?style=flat-square&logo=graphql&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-4.4-008CC1?style=flat-square&logo=neo4j&logoColor=white)
![LDAP](https://img.shields.io/badge/LDAP-ldap3-purple?style=flat-square&logo=microsoft&logoColor=white)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE%20ATT%26CK-T1069%20%7C%20T1087%20%7C%20T1482-red?style=flat-square&logo=databricks&logoColor=white)
![Tactic](https://img.shields.io/badge/Tactic-Discovery%20%2F%20Reconnaissance-purple?style=flat-square&logo=gnubash&logoColor=white)
![License](https://img.shields.io/badge/License-Educational-green?style=flat-square&logo=bookstack&logoColor=white)

</div>

---

## 📋 Table of Contents

- [🎯 Objectives](#-objectives)
- [✅ Prerequisites](#-prerequisites)
- [🧪 Lab Environment](#-lab-environment)
- [📁 Directory Structure](#-directory-structure)
- [🛠️ Task 1 — Install & Configure BloodHound](#️-task-1--install-and-configure-bloodhound-environment)
- [🐍 Task 2 — Simulate AD Data Collection](#-task-2--simulate-ad-data-collection-with-python)
- [🔎 Task 3 — LDAP Enumeration](#-task-3--implement-ldap-enumeration)
- [🗺️ Task 4 — Analyze AD Attack Paths](#️-task-4--analyze-ad-attack-paths)
- [✔️ Expected Outcomes](#️-expected-outcomes)
- [🛠️ Troubleshooting](#️-troubleshooting)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

By the end of this lab, students will be able to:

- 🧠 Install and configure **BloodHound** and **Neo4j** for AD visualization
- 🐍 Simulate AD enumeration data collection using **Python**
- 🔍 Analyze AD permissions, group memberships, and **attack paths**
- 📡 Implement **LDAP enumeration** techniques programmatically
- ⚠️ Identify **privilege escalation** opportunities in AD environments

---

## ✅ Prerequisites

| Requirement | Details |
|---|---|
| 🏢 AD Knowledge | Basic understanding of Active Directory (domains, users, groups) |
| 💻 CLI Skills | Familiarity with Linux command-line operations |
| 🐍 Python | Basic Python programming knowledge |
| 📄 JSON | Understanding of JSON data structures |

---

## 🧪 Lab Environment

> 💡 **Cloud-Based Setup:** This lab runs on a single **Linux machine** provided by Al Nafi. All tools are pre-installed. Click **▶ Start Lab** to begin.
>
> Since we don't have access to a real Windows AD environment, we'll **simulate AD data structures** and practice enumeration techniques using local tools.

---

## 📁 Directory Structure

```
~/ad-enum-lab/
├── 🐍  ad_collector.py
├── 🩸  bloodhound_generator.py
├── 📡  ldap_enumerator.py
├── 📋  ldap_queries.txt
├── 🗺️  attack_path_analyzer.py
├── 🩸  BloodHound-linux-x64/
│   └── BloodHound
└── 📂  sample-data/
    └── domain_structure.json
```

---

## 🛠️ Task 1 — Install and Configure BloodHound Environment

### Step 1.1 — Install Neo4j Database

```bash
# 🔄 Update system and install Java
sudo apt update
sudo apt install -y openjdk-11-jdk wget

# 📦 Add Neo4j repository and install
wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
echo 'deb https://debian.neo4j.com stable 4.4' | sudo tee /etc/apt/sources.list.d/neo4j.list
sudo apt update
sudo apt install -y neo4j

# ▶️ Start Neo4j service
sudo systemctl start neo4j
sudo systemctl enable neo4j
```

### Step 1.2 — Configure Neo4j Credentials

```bash
# ⏳ Wait for Neo4j to initialize
sleep 15

# 🔐 Change default password (neo4j/neo4j → neo4j/bloodhound123)
curl -H "Content-Type: application/json" \
     -X POST \
     -d '{"password":"bloodhound123"}' \
     -u neo4j:neo4j \
     http://localhost:7474/user/neo4j/password

# ✅ Verify Neo4j is running
sudo systemctl status neo4j
```

### Step 1.3 — Install BloodHound and Dependencies

```bash
# 📁 Create working directory
mkdir -p ~/ad-enum-lab && cd ~/ad-enum-lab

# 🐍 Install Python dependencies
pip3 install ldap3 neo4j bloodhound

# ⬇️ Download BloodHound
wget https://github.com/BloodHoundAD/BloodHound/releases/download/v4.3.1/BloodHound-linux-x64.zip
unzip BloodHound-linux-x64.zip
chmod +x BloodHound-linux-x64/BloodHound
```

### Step 1.4 — Create Sample AD Data Structure

```bash
# 📂 Create sample data directory
mkdir -p ~/ad-enum-lab/sample-data

# 🏢 Create domain structure file
cat > ~/ad-enum-lab/sample-data/domain_structure.json << 'EOF'
{
  "domain": "CORP.LOCAL",
  "users": [
    {"name": "Administrator", "sid": "S-1-5-21-1111-2222-3333-500", "groups": ["Domain Admins"]},
    {"name": "jsmith",        "sid": "S-1-5-21-1111-2222-3333-1001", "groups": ["Domain Users"]},
    {"name": "svc_backup",    "sid": "S-1-5-21-1111-2222-3333-1002", "groups": ["Backup Operators"]}
  ],
  "groups": [
    {"name": "Domain Admins", "sid": "S-1-5-21-1111-2222-3333-512"},
    {"name": "Domain Users",  "sid": "S-1-5-21-1111-2222-3333-513"}
  ],
  "computers": [
    {"name": "WS01.corp.local",  "os": "Windows 10",           "admins": ["jsmith"]},
    {"name": "SRV01.corp.local", "os": "Windows Server 2019",  "admins": ["Administrator"]}
  ]
}
EOF
```

---

## 🐍 Task 2 — Simulate AD Data Collection with Python

> **MITRE ATT&CK:** [T1087 – Account Discovery](https://attack.mitre.org/techniques/T1087/) | [T1069 – Permission Groups Discovery](https://attack.mitre.org/techniques/T1069/)

### Step 2.1 — Create AD Data Collector Template

```bash
cat > ~/ad-enum-lab/ad_collector.py << 'EOF'
#!/usr/bin/env python3
"""
AD Data Collection Simulator
Simulates SharpHound data collection for educational purposes
"""

import json
import datetime
from typing import Dict, List

class ADCollector:
    def __init__(self, domain: str):
        """
        Initialize AD collector for specified domain

        Args:
            domain: Target domain name
        """
        self.domain = domain
        self.results = {
            "meta": {
                "domain": domain,
                "collection_date": datetime.datetime.now().isoformat()
            },
            "data": {}
        }

    def collect_users(self) -> List[Dict]:
        """
        Collect user information from AD

        Returns:
            List of user dictionaries with properties

        TODO: Implement user enumeration logic
        TODO: Extract user attributes (name, SID, groups)
        TODO: Identify privileged accounts
        """
        pass

    def collect_groups(self) -> List[Dict]:
        """
        Collect group information and memberships

        Returns:
            List of group dictionaries with members

        TODO: Enumerate all groups
        TODO: Map group memberships
        TODO: Identify nested groups
        """
        pass

    def collect_computers(self) -> List[Dict]:
        """
        Collect computer objects and local admin mappings

        Returns:
            List of computer dictionaries

        TODO: Enumerate computer objects
        TODO: Identify local administrators
        TODO: Detect active sessions
        """
        pass

    def analyze_permissions(self) -> Dict:
        """
        Analyze ACLs and permissions

        Returns:
            Dictionary of permission mappings

        TODO: Parse ACL entries
        TODO: Identify dangerous permissions (GenericAll, WriteDacl, etc.)
        TODO: Map permission chains
        """
        pass

    def save_results(self, filename: str):
        """
        Save collection results to JSON file

        Args:
            filename: Output file path

        TODO: Serialize results to JSON
        TODO: Handle file I/O errors
        """
        pass

def main():
    # TODO: Initialize collector
    # TODO: Run collection methods
    # TODO: Save and display results
    pass

if __name__ == "__main__":
    main()
EOF

chmod +x ~/ad-enum-lab/ad_collector.py
```

### Step 2.2 — Create BloodHound Data Generator

```bash
cat > ~/ad-enum-lab/bloodhound_generator.py << 'EOF'
#!/usr/bin/env python3
"""
BloodHound JSON Data Generator
Creates BloodHound-compatible JSON files from AD data
"""

import json
from typing import Dict, List

class BloodHoundGenerator:
    def __init__(self):
        self.version = 4

    def generate_users_json(self, users: List[Dict]) -> Dict:
        """
        Generate BloodHound users JSON structure

        Args:
            users: List of user dictionaries

        Returns:
            BloodHound-formatted users data

        TODO: Convert user data to BloodHound format
        TODO: Add required properties (objectid, enabled, admincount)
        TODO: Include group memberships
        """
        pass

    def generate_computers_json(self, computers: List[Dict]) -> Dict:
        """
        Generate BloodHound computers JSON structure

        Args:
            computers: List of computer dictionaries

        Returns:
            BloodHound-formatted computers data

        TODO: Format computer objects
        TODO: Add LocalAdmins, Sessions, RemoteDesktopUsers
        TODO: Include delegation properties
        """
        pass

    def generate_groups_json(self, groups: List[Dict]) -> Dict:
        """
        Generate BloodHound groups JSON structure

        Args:
            groups: List of group dictionaries

        Returns:
            BloodHound-formatted groups data

        TODO: Format group objects
        TODO: Add Members array with ObjectIdentifier
        TODO: Include ACEs if applicable
        """
        pass

def main():
    # TODO: Load sample AD data
    # TODO: Generate BloodHound JSON files
    # TODO: Save to appropriate filenames
    pass

if __name__ == "__main__":
    main()
EOF

chmod +x ~/ad-enum-lab/bloodhound_generator.py
```

### Step 2.3 — Run Data Collection Simulation

```bash
# ▶️ Execute the collector (complete implementation first)
cd ~/ad-enum-lab
python3 ad_collector.py

# 🩸 Generate BloodHound-compatible files
python3 bloodhound_generator.py
```

---

## 🔎 Task 3 — Implement LDAP Enumeration

> **MITRE ATT&CK:** [T1018 – Remote System Discovery](https://attack.mitre.org/techniques/T1018/) | [T1482 – Domain Trust Discovery](https://attack.mitre.org/techniques/T1482/)

### Step 3.1 — Create LDAP Query Template

```bash
cat > ~/ad-enum-lab/ldap_enumerator.py << 'EOF'
#!/usr/bin/env python3
"""
LDAP Enumeration Tool
Performs LDAP queries against Active Directory
"""

from ldap3 import Server, Connection, ALL, SUBTREE
from typing import List, Dict

class LDAPEnumerator:
    def __init__(self, server: str, username: str, password: str, base_dn: str):
        """
        Initialize LDAP connection

        Args:
            server:   LDAP server address
            username: Authentication username
            password: Authentication password
            base_dn:  Base Distinguished Name for searches

        TODO: Establish LDAP connection
        TODO: Handle authentication
        TODO: Set up search base
        """
        pass

    def enumerate_users(self, attributes: List[str] = None) -> List[Dict]:
        """
        Enumerate all user objects

        Args:
            attributes: List of attributes to retrieve

        Returns:
            List of user dictionaries

        TODO: Build LDAP filter for users
        TODO: Execute search query
        TODO: Parse and return results
        """
        pass

    def enumerate_groups(self) -> List[Dict]:
        """
        Enumerate all group objects

        Returns:
            List of group dictionaries

        TODO: Query for group objects
        TODO: Extract group members
        TODO: Identify privileged groups
        """
        pass

    def find_spn_accounts(self) -> List[Dict]:
        """
        Find accounts with Service Principal Names (Kerberoastable)

        Returns:
            List of accounts with SPNs

        TODO: Filter for servicePrincipalName attribute
        TODO: Exclude computer accounts
        TODO: Return vulnerable accounts
        """
        pass

    def find_asreproast_accounts(self) -> List[Dict]:
        """
        Find accounts vulnerable to AS-REP roasting

        Returns:
            List of accounts without Kerberos pre-auth

        TODO: Query for DONT_REQ_PREAUTH flag
        TODO: Filter enabled accounts
        TODO: Return vulnerable accounts
        """
        pass

    def enumerate_trusts(self) -> List[Dict]:
        """
        Enumerate domain trust relationships

        Returns:
            List of trust objects

        TODO: Query trustedDomain objects
        TODO: Extract trust attributes
        TODO: Identify trust direction and type
        """
        pass

def main():
    # TODO: Parse command-line arguments
    # TODO: Initialize enumerator
    # TODO: Execute enumeration functions
    # TODO: Display results
    pass

if __name__ == "__main__":
    main()
EOF

chmod +x ~/ad-enum-lab/ldap_enumerator.py
```

### Step 3.2 — Create LDAP Query Reference

```bash
cat > ~/ad-enum-lab/ldap_queries.txt << 'EOF'
# ═══════════════════════════════════════════════════════
#   Common LDAP Queries for AD Enumeration
# ═══════════════════════════════════════════════════════

# 👤 Find all users
(&(objectCategory=person)(objectClass=user))

# 👥 Find all groups
(objectClass=group)

# 🔑 Find Domain Admins
(memberOf=CN=Domain Admins,CN=Users,DC=corp,DC=local)

# 🎯 Find accounts with SPN (Kerberoastable)
(&(objectCategory=person)(objectClass=user)(servicePrincipalName=*))

# ⚠️ Find accounts without pre-auth (AS-REP Roastable)
(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=4194304))

# 🖥️ Find computers
(objectClass=computer)

# 👑 Find privileged groups
(|(cn=Domain Admins)(cn=Enterprise Admins)(cn=Schema Admins))
EOF
```

---

## 🗺️ Task 4 — Analyze AD Attack Paths

> **MITRE ATT&CK:** [T1078 – Valid Accounts](https://attack.mitre.org/techniques/T1078/) | [T1134 – Access Token Manipulation](https://attack.mitre.org/techniques/T1134/)

### Step 4.1 — Create Attack Path Analyzer

```bash
cat > ~/ad-enum-lab/attack_path_analyzer.py << 'EOF'
#!/usr/bin/env python3
"""
AD Attack Path Analyzer
Identifies privilege escalation paths in Active Directory
"""

import json
from collections import defaultdict
from typing import List, Dict, Set

class AttackPathAnalyzer:
    def __init__(self, data_file: str):
        """
        Initialize analyzer with AD data

        Args:
            data_file: Path to JSON file with AD data

        TODO: Load AD data from file
        TODO: Build internal data structures
        """
        pass

    def find_shortest_path(self, start_user: str, target_group: str) -> List[str]:
        """
        Find shortest path from user to privileged group

        Args:
            start_user:   Starting user account
            target_group: Target privileged group

        Returns:
            List representing the path

        TODO: Implement graph traversal (BFS/DFS)
        TODO: Track visited nodes
        TODO: Return path if found
        """
        pass

    def identify_local_admin_paths(self) -> Dict:
        """
        Identify lateral movement opportunities via local admin rights

        Returns:
            Dictionary mapping users to computers they can access

        TODO: Parse local admin mappings
        TODO: Cross-reference with active sessions
        TODO: Identify credential harvesting opportunities
        """
        pass

    def find_kerberoastable_paths(self) -> List[Dict]:
        """
        Find paths involving Kerberoastable accounts

        Returns:
            List of attack paths using SPN accounts

        TODO: Identify accounts with SPNs
        TODO: Check group memberships
        TODO: Map potential escalation paths
        """
        pass

    def analyze_acl_abuse(self) -> List[Dict]:
        """
        Identify ACL-based privilege escalation opportunities

        Returns:
            List of dangerous ACL configurations

        TODO: Parse ACL entries
        TODO: Identify GenericAll, WriteDacl, WriteOwner
        TODO: Map exploitable permissions
        """
        pass

    def generate_report(self) -> str:
        """
        Generate comprehensive attack path report

        Returns:
            Formatted report string

        TODO: Compile all findings
        TODO: Prioritize by severity
        TODO: Format output
        """
        pass

def main():
    # TODO: Load AD data
    # TODO: Run analysis functions
    # TODO: Generate and display report
    pass

if __name__ == "__main__":
    main()
EOF

chmod +x ~/ad-enum-lab/attack_path_analyzer.py
```

### Step 4.2 — Run Attack Path Analysis

```bash
# 🗺️ Run analyzer against sample domain data
cd ~/ad-enum-lab
python3 attack_path_analyzer.py sample-data/domain_structure.json
```

---

## ✔️ Expected Outcomes

After completing this lab, students should have:

| # | Deliverable | Status |
|---|---|---|
| 1 | 🩸 Functional BloodHound environment with Neo4j backend | ✅ |
| 2 | 🐍 Python scripts for simulating AD data collection | ✅ |
| 3 | 📡 LDAP enumeration tools for querying AD objects | ✅ |
| 4 | 🗺️ Attack path analysis capabilities | ✅ |
| 5 | 🧠 Understanding of AD privilege escalation techniques | ✅ |
| 6 | 🔍 Ability to identify security vulnerabilities in AD environments | ✅ |

### 🔬 Verification Steps

```bash
# ✅ Check Neo4j is running
sudo systemctl status neo4j

# ✅ Verify BloodHound installation
ls -l ~/ad-enum-lab/BloodHound-linux-x64/BloodHound

# ✅ Test Python scripts exist
ls -l ~/ad-enum-lab/*.py

# ✅ Verify sample data
cat ~/ad-enum-lab/sample-data/domain_structure.json
```

---

## 🛠️ Troubleshooting

<details>
<summary>❌ Neo4j Connection Issues</summary>

**Symptoms:** BloodHound cannot connect to the database.

**Fix:**

```bash
# Restart the service
sudo systemctl restart neo4j

# Check port 7474 is open
netstat -tlnp | grep 7474

# Verify credentials (neo4j / bloodhound123)
curl -u neo4j:bloodhound123 http://localhost:7474/db/data/
```

</details>

<details>
<summary>❌ Python Import Errors</summary>

**Symptoms:** `ModuleNotFoundError` when running scripts.

**Fix:**

```bash
# Install missing packages
pip3 install ldap3 neo4j

# Check Python version (must be 3.6+)
python3 --version
```

</details>

<details>
<summary>❌ BloodHound GUI Not Starting</summary>

**Symptoms:** BloodHound binary exits immediately or displays no window.

**Fix:**

```bash
# Verify X11 forwarding (if using SSH)
echo $DISPLAY

# Ensure binary is executable
chmod +x ~/ad-enum-lab/BloodHound-linux-x64/BloodHound

# Review Neo4j logs
journalctl -u neo4j -n 50
```

</details>

---

## 🏁 Conclusion

This lab provided hands-on experience with **Active Directory enumeration techniques** using industry-standard tools.

```
┌──────────────────────────────────────────────────────────────┐
│  🩸 BloodHound + Neo4j   →  Visual AD graph & attack paths   │
│  🐍 SharpHound Sim        →  Python-based data collection    │
│  📡 LDAP Enumeration      →  Query users, groups, trusts     │
│  🗺️  Attack Path Analysis  →  Kerberoast / ACL abuse paths   │
└──────────────────────────────────────────────────────────────┘
```

### 🔑 Key Takeaways

- AD enumeration is critical for understanding **security posture**
- Multiple tools and techniques provide **comprehensive coverage**
- Attack path analysis reveals **non-obvious privilege escalation** routes
- Proper AD security requires understanding **attacker methodologies**

### 🚀 Next Steps

- Complete all Python script **TODO implementations**
- Practice with real AD environments *(in authorized contexts only)*
- Explore advanced **BloodHound Cypher queries**
- Study **AD hardening techniques** to defend against enumeration

---

<div align="center">

---

🔐 **Al Nafi Cybersecurity Training Platform**

*Empowering the Next Generation of Cyber Defenders*

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Red%20Team%20Operations-red?style=for-the-badge&logo=shield&logoColor=white)
![MITRE](https://img.shields.io/badge/MITRE%20ATT%26CK-T1069%20%7C%20T1087%20%7C%20T1482-darkred?style=flat-square)
![BloodHound](https://img.shields.io/badge/BloodHound-v4.3.1-red?style=flat-square&logo=graphql&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-4.4-008CC1?style=flat-square&logo=neo4j&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![LDAP](https://img.shields.io/badge/LDAP-ldap3-purple?style=flat-square&logo=microsoft&logoColor=white)
![Active Directory](https://img.shields.io/badge/Active%20Directory-Enumeration-0078D4?style=flat-square&logo=microsoft&logoColor=white)

*© Al Nafi — For educational and authorized lab use only.*

</div>
