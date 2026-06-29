<div align="center">

# 🛡️ Analyze MFA Bypass Attacks Using Evilginx2

<img src="https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Lab-blue?style=for-the-badge&logo=shield&logoColor=white"/>
<img src="https://img.shields.io/badge/Difficulty-Advanced-red?style=for-the-badge&logo=target&logoColor=white"/>
<img src="https://img.shields.io/badge/Lab%20Type-Hands--On-green?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/Domain-Red%20Team%20%26%20Defense-darkred?style=for-the-badge&logo=hackthebox&logoColor=white"/>

---

[![Evilginx2](https://img.shields.io/badge/Evilginx2-MFA%20Bypass%20Framework-1a1a2e?style=flat-square&logo=go&logoColor=white)](https://github.com/kgretzky/evilginx2)
[![Go](https://img.shields.io/badge/Go-1.21+-00ADD8?style=flat-square&logo=go&logoColor=white)](https://go.dev)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![dnstwist](https://img.shields.io/badge/dnstwist-Domain%20Analysis-FF6B35?style=flat-square&logo=dns&logoColor=white)](https://github.com/elceef/dnstwist)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04%20LTS-E95420?style=flat-square&logo=ubuntu&logoColor=white)](https://ubuntu.com)
[![requests](https://img.shields.io/badge/requests-HTTP%20Library-2CA5E0?style=flat-square&logo=python&logoColor=white)](https://docs.python-requests.org)
[![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK%20Framework-red?style=flat-square&logo=mitre&logoColor=white)](https://attack.mitre.org)
[![FIDO2](https://img.shields.io/badge/FIDO2-WebAuthn%20Defense-2D9CDB?style=flat-square&logo=webauthn&logoColor=white)](https://fidoalliance.org)

> ⚠️ **Educational Use Only** — All activities must be performed exclusively within the Al Nafi controlled lab environment.

</div>

---

## 📋 Table of Contents

- [🎯 Objectives](#-objectives)
- [✅ Prerequisites](#-prerequisites)
- [🖥️ Lab Environment](#️-lab-environment)
- [🔧 Task 1 — Install & Configure Evilginx2](#-task-1--install--configure-evilginx2)
- [🌐 Task 2 — Domain Analysis with dnstwist](#-task-2--domain-analysis-with-dnstwist)
- [🤖 Task 3 — Automate MFA Bypass Simulations](#-task-3--automate-mfa-bypass-simulations)
- [📊 Task 4 — Analyze Results & Implement Defenses](#-task-4--analyze-results--implement-defenses)
- [✅ Expected Outcomes](#-expected-outcomes)
- [🛠️ Troubleshooting Tips](#️-troubleshooting-tips)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

> By the end of this lab, students will be able to:

| # | Objective |
|---|-----------|
| 1️⃣ | Understand **MFA bypass attack methodologies** and their security implications |
| 2️⃣ | Configure **Evilginx2** for phishing-based MFA bypass simulations |
| 3️⃣ | Use **dnstwist** to identify domain lookalike opportunities |
| 4️⃣ | Develop **Python scripts** to automate attack simulations |
| 5️⃣ | Analyze attack vectors and implement **defensive countermeasures** |

---

## ✅ Prerequisites

| Skill | Level |
|-------|-------|
| 🐧 Linux Command Line | Basic |
| 🌐 HTTP/HTTPS & DNS Protocols | Understanding |
| 🔐 Multi-Factor Authentication Concepts | Familiar |
| 🐍 Python Programming | Fundamentals |
| 🎣 Phishing Attack Methodologies | Basic Knowledge |

---

## 🖥️ Lab Environment

<div align="center">

[![Al Nafi Cloud](https://img.shields.io/badge/Platform-Al%20Nafi%20Cloud%20Lab-blue?style=for-the-badge&logo=cloud&logoColor=white)]()
[![Ubuntu](https://img.shields.io/badge/OS-Ubuntu%2020.04%20LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)]()
[![Go](https://img.shields.io/badge/Runtime-Go%201.21+-00ADD8?style=for-the-badge&logo=go&logoColor=white)]()
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)]()

</div>

Al Nafi provides **pre-configured Ubuntu 20.04 LTS cloud machines**. Click **▶️ Start Lab** to access your environment with:

- ✅ Pre-installed development tools and dependencies
- ✅ Network access for tool downloads
- ✅ Sufficient resources for running simulations

> 🔒 **Note:** This lab is for **educational purposes only**. All activities must be performed in the controlled lab environment.

---

## 🔧 Task 1 — Install & Configure Evilginx2

---

### ⚙️ Step 1.1 — Install Go and Dependencies

[![Go](https://img.shields.io/badge/Go-1.21.0-00ADD8?style=flat-square&logo=go&logoColor=white)]()
[![apt](https://img.shields.io/badge/apt-Package%20Manager-E95420?style=flat-square&logo=ubuntu&logoColor=white)]()
[![build-essential](https://img.shields.io/badge/build--essential-Compiler%20Tools-4EAA25?style=flat-square&logo=gnubash&logoColor=white)]()

```bash
# 📦 Update system and install prerequisites
sudo apt update && sudo apt upgrade -y
sudo apt install -y git curl wget build-essential

# 📥 Download and install Go
wget https://go.dev/dl/go1.21.0.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.21.0.linux-amd64.tar.gz

# 🔧 Configure Go environment
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
echo 'export GOPATH=$HOME/go' >> ~/.bashrc
source ~/.bashrc

# ✅ Verify installation
go version
```

---

### 🏗️ Step 1.2 — Build Evilginx2

[![Evilginx2](https://img.shields.io/badge/Evilginx2-Build%20from%20Source-1a1a2e?style=flat-square&logo=go&logoColor=white)]()
[![Make](https://img.shields.io/badge/make-Build%20Tool-4EAA25?style=flat-square&logo=gnubash&logoColor=white)]()
[![Git](https://img.shields.io/badge/git-Clone%20Repo-F05032?style=flat-square&logo=git&logoColor=white)]()

```bash
# 📂 Create workspace
mkdir -p ~/redteam-lab/evilginx2
cd ~/redteam-lab/evilginx2

# 📥 Clone and build Evilginx2
git clone https://github.com/kgretzky/evilginx2.git
cd evilginx2
make

# ✅ Verify build
./build/evilginx -h
```

---

### 📄 Step 1.3 — Create Custom Phishlet Template

[![YAML](https://img.shields.io/badge/YAML-Phishlet%20Config-CB171E?style=flat-square&logo=yaml&logoColor=white)]()
[![Evilginx2](https://img.shields.io/badge/Evilginx2-Phishlet-1a1a2e?style=flat-square&logo=go&logoColor=white)]()

```bash
# 📂 Create phishlets directory
mkdir -p ~/redteam-lab/phishlets

# 📝 Write phishlet configuration
cat > ~/redteam-lab/phishlets/demo-mfa.yaml << 'EOF'
name: 'demo-mfa'
author: '@lab-student'
min_ver: '3.0.0'

proxy_hosts:
  - {phish_sub: '', orig_sub: '', domain: 'login.example.com', session: true, is_landing: true}

auth_tokens:
  - domain: '.example.com'
    keys: ['session_token']

credentials:
  username:
    key: 'username'
    search: 'username'
    type: 'post'
  password:
    key: 'password'
    search: 'password'
    type: 'post'
EOF
```

---

## 🌐 Task 2 — Domain Analysis with dnstwist

---

### 📦 Step 2.1 — Install dnstwist

[![dnstwist](https://img.shields.io/badge/dnstwist-Domain%20Fuzzer-FF6B35?style=flat-square&logo=dns&logoColor=white)]()
[![pip](https://img.shields.io/badge/pip-Python%20Package%20Manager-3776AB?style=flat-square&logo=pypi&logoColor=white)]()

```bash
# 📦 Install dnstwist with all optional dependencies
sudo apt install -y python3-pip
pip3 install dnstwist[full]

# ✅ Verify installation
dnstwist --version
```

---

### 🔍 Step 2.2 — Create Domain Analysis Script

[![Python](https://img.shields.io/badge/Python-Domain%20Analyzer-3776AB?style=flat-square&logo=python&logoColor=white)]()
[![dnstwist](https://img.shields.io/badge/dnstwist-Backend%20Engine-FF6B35?style=flat-square&logo=searchengin&logoColor=white)]()
[![subprocess](https://img.shields.io/badge/subprocess-System%20Commands-yellow?style=flat-square&logo=python&logoColor=white)]()

Students will complete this script to analyze domain variations:

```python
#!/usr/bin/env python3
"""
🔍 Domain Analysis Tool for Phishing Campaign Planning
Students: Complete the TODO sections
"""

import subprocess  # 🔧 For running dnstwist
import json        # 📊 For parsing JSON output
import sys         # 🔧 For command-line arguments

def analyze_domain(target_domain):
    """
    🌐 Analyze domain for potential phishing variations.
    
    Args:
        target_domain: The legitimate domain to analyze
    
    Returns:
        List of domain variations
    """
    print(f"[+] 🔍 Analyzing: {target_domain}")
    
    # TODO: 🚀 Execute dnstwist command with appropriate flags
    # 💡 Hint: Use subprocess.run() with JSON output format
    # TODO: 📊 Parse the JSON output
    # TODO: 🔎 Filter and return relevant results
    
    pass

def generate_custom_variations(base_domain):
    """
    🎭 Generate custom phishing domain variations.
    
    Args:
        base_domain: Base domain for variations
    
    Returns:
        List of custom domain variations
    """
    variations = []
    
    # TODO: ✏️ Implement typosquatting variations
    # TODO: 🔤 Implement homograph variations
    # TODO: 🌐 Implement subdomain variations
    # TODO: 📤 Return the variations list
    
    pass

def check_availability(domain_list):
    """
    🔎 Check if domains are registered.
    
    Args:
        domain_list: List of domains to check
    
    Returns:
        Dictionary with availability status
    """
    # TODO: 🌐 Implement DNS lookup for each domain
    # TODO: ✅ Categorize as available or registered
    # TODO: 📦 Return results dictionary
    
    pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("⚠️  Usage: python3 domain_analysis.py <domain>")
        sys.exit(1)
    
    target = sys.argv[1]
    # TODO: 🚀 Call analyze_domain()
    # TODO: 🎭 Call generate_custom_variations()
    # TODO: 🔎 Call check_availability()
    # TODO: 📋 Print formatted results
```

> 💾 Save and make executable:

```bash
chmod +x ~/redteam-lab/domain_analysis.py
```

---

### ▶️ Step 2.3 — Run Domain Analysis

[![dnstwist](https://img.shields.io/badge/dnstwist-Run%20Scan-FF6B35?style=flat-square&logo=searchengin&logoColor=white)]()
[![Bash](https://img.shields.io/badge/Bash-Execute-4EAA25?style=flat-square&logo=gnubash&logoColor=white)]()

```bash
# 🧪 Test with safe example domain
cd ~/redteam-lab
python3 domain_analysis.py example.com > domain_report.txt
```

---

## 🤖 Task 3 — Automate MFA Bypass Simulations

---

### 🏗️ Step 3.1 — Create MFA Bypass Simulator Framework

[![Python](https://img.shields.io/badge/Python-Simulator%20Class-3776AB?style=flat-square&logo=python&logoColor=white)]()
[![requests](https://img.shields.io/badge/requests-HTTP%20Sessions-2CA5E0?style=flat-square&logo=python&logoColor=white)]()
[![logging](https://img.shields.io/badge/logging-Audit%20Trail-9B59B6?style=flat-square&logo=python&logoColor=white)]()

Students will implement the core simulation logic:

```python
#!/usr/bin/env python3
"""
🤖 MFA Bypass Attack Simulator
Students: Complete the implementation
"""

import requests          # 🌐 For HTTP simulation
import json              # 📊 For data serialization
import time              # ⏱️ For timing delays
import random            # 🎲 For randomization
from datetime import datetime  # 🕒 For timestamps
import logging           # 📋 For audit logging

# 📋 Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MFABypassSimulator:
    def __init__(self):
        self.session = requests.Session()  # 🌐 Persistent HTTP session
        self.results = []                  # 📦 Store simulation results
        
    def simulate_credential_harvest(self, target_url, credentials):
        """
        🎣 Simulate credential harvesting from phishing page.
        
        Args:
            target_url: Phishing page URL
            credentials: Dictionary with username/password
        
        Returns:
            Dictionary with harvest results
        """
        # TODO: 📤 Create POST request with credentials
        # TODO: 📥 Handle response and extract relevant data
        # TODO: 📋 Log results and return status
        
        pass
    
    def simulate_mfa_bypass(self, target_url, mfa_token):
        """
        🔐 Simulate MFA token submission and bypass attempt.
        
        Args:
            target_url: MFA verification endpoint
            mfa_token: MFA code to submit
        
        Returns:
            Dictionary with bypass attempt results
        """
        # TODO: 📤 Submit MFA token via POST request
        # TODO: 🔍 Analyze response for success indicators
        # TODO: 📊 Record bypass attempt results
        
        pass
    
    def simulate_session_hijacking(self, session_cookies):
        """
        🍪 Simulate session hijacking after successful MFA bypass.
        
        Args:
            session_cookies: Dictionary of session cookies
        
        Returns:
            Dictionary with hijacking results
        """
        # TODO: 🍪 Apply session cookies to requests session
        # TODO: 🔑 Attempt authenticated actions
        # TODO: ✅ Verify session validity
        
        pass
    
    def generate_report(self):
        """
        📝 Generate comprehensive attack simulation report.
        
        Returns:
            Dictionary with complete simulation results
        """
        # TODO: 🔗 Aggregate all simulation results
        # TODO: 📊 Calculate success rates and statistics
        # TODO: 💾 Format report and save to JSON file
        
        pass

class PhishingCampaignManager:
    def __init__(self):
        self.campaigns = []  # 📋 Campaign storage
    
    def create_campaign(self, name, target_domain, phishing_domain):
        """
        🏗️ Create new phishing campaign configuration.
        
        Args:
            name: Campaign name
            target_domain: Legitimate domain being spoofed
            phishing_domain: Phishing domain to use
        
        Returns:
            Campaign configuration dictionary
        """
        # TODO: 🗂️ Create campaign data structure
        # TODO: 📊 Initialize tracking metrics
        # TODO: 📤 Return campaign object
        
        pass
    
    def simulate_victim_interaction(self, campaign_id, victim_data):
        """
        👤 Simulate victim interaction with phishing campaign.
        
        Args:
            campaign_id: ID of the campaign
            victim_data: Dictionary with victim information
        
        Returns:
            Interaction results dictionary
        """
        # TODO: 📧 Simulate email delivery
        # TODO: 🖱️ Simulate link click behavior
        # TODO: ⌨️ Simulate credential entry
        # TODO: 📊 Track interaction metrics
        
        pass
    
    def get_campaign_statistics(self, campaign_id):
        """
        📊 Calculate campaign performance statistics.
        
        Args:
            campaign_id: ID of the campaign
        
        Returns:
            Dictionary with campaign statistics
        """
        # TODO: 📊 Calculate click-through rate
        # TODO: 🔑 Calculate credential harvest rate
        # TODO: 🔐 Calculate MFA bypass success rate
        
        pass

def main():
    """
    🚀 Main execution workflow for MFA bypass simulation.
    """
    print("=" * 60)
    print("🤖 MFA Bypass Attack Simulation Framework")
    print("=" * 60)
    
    # TODO: 🏗️ Initialize simulator and campaign manager
    # TODO: 📋 Create test campaign
    # TODO: 🎣 Run credential harvest simulations
    # TODO: 🔐 Run MFA bypass simulations
    # TODO: 📝 Generate and display report
    
    pass

if __name__ == "__main__":
    main()
```

> 💾 Save and make executable:

```bash
chmod +x ~/redteam-lab/mfa_bypass_automation.py
```

---

### 🎭 Step 3.2 — Implement Attack Scenarios

[![Scenarios](https://img.shields.io/badge/Module-Attack%20Scenarios-8B0000?style=flat-square&logo=python&logoColor=white)]()
[![MITRE](https://img.shields.io/badge/MITRE-ATT%26CK%20Mapped-red?style=flat-square&logo=mitre&logoColor=white)]()
[![Python](https://img.shields.io/badge/Python-OOP%20Classes-3776AB?style=flat-square&logo=python&logoColor=white)]()

```python
#!/usr/bin/env python3
"""
🎭 Advanced MFA Bypass Attack Scenarios
Students: Implement each scenario
"""

import json              # 📊 For data serialization
import time              # ⏱️ For timing delays
import random            # 🎲 For stochastic simulation
from datetime import datetime  # 🕒 For timestamps

class AttackScenarios:
    def __init__(self):
        self.results = []  # 📦 Scenario results store
    
    def scenario_mass_phishing(self, target_list):
        """
        📧 Execute mass phishing campaign simulation.
        
        Args:
            target_list: List of target email addresses
        
        Returns:
            Campaign results dictionary
        """
        # TODO: 🔄 Iterate through target list
        # TODO: 📧 Simulate email delivery for each target
        # TODO: 🖱️ Simulate click and credential entry rates
        # TODO: 🔐 Track MFA bypass attempts
        
        pass
    
    def scenario_targeted_attack(self, high_value_target):
        """
        🎯 Execute targeted attack on high-value user.
        
        Args:
            high_value_target: Target user information
        
        Returns:
            Attack progression results
        """
        # TODO: 🔍 Implement reconnaissance phase
        # TODO: 🤝 Implement trust-building phase
        # TODO: 🎣 Implement credential harvest phase
        # TODO: 🔐 Implement MFA bypass phase
        
        pass
    
    def scenario_automated_bypass(self, bypass_techniques):
        """
        ⚡ Test multiple automated MFA bypass techniques.
        
        Args:
            bypass_techniques: List of techniques to test
        
        Returns:
            Technique effectiveness results
        """
        # TODO: 🍪 Implement session hijacking simulation
        # TODO: 🔄 Implement token replay simulation
        # TODO: 📱 Implement push notification fatigue
        # TODO: 📊 Compare technique success rates
        
        pass
    
    def scenario_persistence(self, compromised_account):
        """
        🔒 Establish persistence after successful MFA bypass.
        
        Args:
            compromised_account: Account information
        
        Returns:
            Persistence establishment results
        """
        # TODO: 🔑 Simulate OAuth app registration
        # TODO: 📬 Simulate mailbox rule creation
        # TODO: 📱 Simulate additional MFA device registration
        # TODO: ⚠️ Assess detection risk for each method
        
        pass
    
    def generate_scenario_report(self):
        """
        📝 Generate comprehensive scenario analysis report.
        
        Returns:
            Complete scenario results and metrics
        """
        # TODO: 🔗 Aggregate results from all scenarios
        # TODO: 📊 Calculate success rates per scenario
        # TODO: 🎯 Identify most effective techniques
        # TODO: 💡 Generate recommendations
        
        pass

if __name__ == "__main__":
    scenarios = AttackScenarios()
    # TODO: 🚀 Execute all scenarios
    # TODO: 📝 Generate final report
```

> 💾 Save as `~/redteam-lab/advanced_scenarios.py`

---

### ▶️ Step 3.3 — Run Complete Simulation

[![Python](https://img.shields.io/badge/Python-Run%20Framework-3776AB?style=flat-square&logo=python&logoColor=white)]()
[![JSON](https://img.shields.io/badge/Output-JSON%20Report-000000?style=flat-square&logo=json&logoColor=white)]()

```bash
# 🚀 Execute the automation framework
cd ~/redteam-lab
python3 mfa_bypass_automation.py

# 📊 Review generated reports
cat mfa_bypass_report.json
```

---

## 📊 Task 4 — Analyze Results & Implement Defenses

---

### 🔬 Step 4.1 — Create Analysis Script

[![Analysis](https://img.shields.io/badge/Module-Results%20Analyzer-6A0DAD?style=flat-square&logo=python&logoColor=white)]()
[![MITRE](https://img.shields.io/badge/MITRE-ATT%26CK%20Mapping-red?style=flat-square&logo=mitre&logoColor=white)]()
[![SIEM](https://img.shields.io/badge/Output-SIEM%20Detection%20Rules-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)]()

```python
#!/usr/bin/env python3
"""
🔬 Attack Results Analysis and Defense Recommendations
Students: Complete the analysis functions
"""

import json                    # 📊 For loading results
from collections import Counter  # 📐 For pattern counting

def analyze_attack_patterns(results_file):
    """
    🔍 Analyze attack simulation results for patterns.
    
    Args:
        results_file: Path to JSON results file
    
    Returns:
        Dictionary with pattern analysis
    """
    # TODO: 📂 Load and parse results file
    # TODO: 🔍 Identify common attack vectors
    # TODO: 📊 Calculate success rates by technique
    # TODO: 👤 Identify vulnerable user behaviors
    
    pass

def generate_defense_recommendations(analysis_results):
    """
    🛡️ Generate defense recommendations based on analysis.
    
    Args:
        analysis_results: Attack pattern analysis
    
    Returns:
        List of prioritized recommendations
    """
    # TODO: ⚠️ Identify highest-risk attack vectors
    # TODO: 🗺️ Map attacks to MITRE ATT&CK framework
    # TODO: 🔧 Generate technical countermeasures
    # TODO: 👥 Generate user awareness recommendations
    
    pass

def create_detection_rules(attack_indicators):
    """
    📡 Create detection rules for identified attack patterns.
    
    Args:
        attack_indicators: List of attack indicators
    
    Returns:
        Dictionary with detection rules
    """
    # TODO: 🚨 Define suspicious login patterns
    # TODO: 📱 Define anomalous MFA behavior
    # TODO: 🍪 Define session hijacking indicators
    # TODO: 📋 Format as SIEM-compatible rules
    
    pass

if __name__ == "__main__":
    # TODO: 📂 Load simulation results
    # TODO: 🔬 Perform analysis
    # TODO: 🛡️ Generate recommendations
    # TODO: 📡 Create detection rules
    pass
```

---

### 🛡️ Step 4.2 — Document Defensive Measures

[![Markdown](https://img.shields.io/badge/Checklist-Defense%20Controls-28a745?style=flat-square&logo=markdown&logoColor=white)]()
[![FIDO2](https://img.shields.io/badge/FIDO2-Phishing%20Resistant%20MFA-2D9CDB?style=flat-square&logo=webauthn&logoColor=white)]()
[![SIEM](https://img.shields.io/badge/SIEM-Detection%20Rules-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)]()

```bash
# 📝 Create defense implementation checklist
cat > ~/redteam-lab/defense_checklist.md << 'EOF'
# 🛡️ MFA Bypass Defense Checklist

## 🔧 Technical Controls
- [ ] Implement FIDO2/WebAuthn for phishing-resistant MFA
- [ ] Enable conditional access policies
- [ ] Deploy email security gateway with link analysis
- [ ] Implement session timeout policies
- [ ] Enable device compliance checks

## 🚨 Detection Capabilities
- [ ] Monitor for impossible travel scenarios
- [ ] Alert on multiple failed MFA attempts
- [ ] Detect suspicious OAuth app registrations
- [ ] Monitor for mailbox rule changes
- [ ] Track session anomalies

## 👥 User Awareness
- [ ] Conduct phishing simulation training
- [ ] Educate on MFA prompt fatigue attacks
- [ ] Train on URL verification techniques
- [ ] Establish security reporting procedures

## 🚑 Incident Response
- [ ] Define MFA bypass response procedures
- [ ] Establish account recovery processes
- [ ] Create communication templates
- [ ] Document forensic collection steps
EOF
```

---

## ✅ Expected Outcomes

> After completing this lab, students should have:

| # | Outcome |
|---|---------|
| ✅ | Functional **Evilginx2** installation and custom phishlet |
| ✅ | Domain analysis scripts identifying **phishing opportunities** |
| ✅ | Python **automation framework** for MFA bypass simulations |
| ✅ | Comprehensive **attack simulation reports** |
| ✅ | Defense **recommendations and detection rules** |
| ✅ | Understanding of the **MFA bypass attack lifecycle** |

---

## 🛠️ Troubleshooting Tips

<details>
<summary>🏗️ Evilginx2 Build Fails</summary>

| Problem | Solution |
|---------|----------|
| ❌ Build error | Verify Go version is **1.19 or higher** |
| ❌ Path issues | Check `GOPATH` configuration in `.bashrc` |
| ❌ Missing deps | Re-run `sudo apt install -y build-essential` |

</details>

<details>
<summary>🔍 dnstwist Returns No Results</summary>

| Problem | Solution |
|---------|----------|
| ❌ Empty output | Check internet connectivity |
| ❌ Syntax error | Verify domain format (no `https://`) |
| ❌ No registered | Try with `--registered` flag |

</details>

<details>
<summary>🐍 Python Script Errors</summary>

| Problem | Solution |
|---------|----------|
| ❌ Import errors | Run `pip3 install requests` |
| ❌ Version issues | Verify Python 3.8+ with `python3 --version` |
| ❌ No output | Ensure all `TODO` sections are implemented |

</details>

<details>
<summary>⚙️ Simulation Scripts Produce No Output</summary>

| Problem | Solution |
|---------|----------|
| ❌ Permission denied | Run `chmod +x <script.py>` |
| ❌ Silent failure | Review `logging` output for errors |
| ❌ Missing results | Verify all class methods are fully implemented |

</details>

---

## 🏁 Conclusion

This lab provided hands-on experience with MFA bypass attack methodologies using **Evilginx2** and custom automation scripts. Students learned to identify vulnerable domains, simulate phishing campaigns, and analyze attack effectiveness. The defensive analysis component emphasized the importance of **phishing-resistant MFA** implementations and comprehensive detection strategies.

### 🔑 Key Takeaways

| # | Takeaway |
|---|----------|
| ⚠️ | Traditional MFA methods remain **vulnerable to sophisticated phishing** |
| 🛡️ | **FIDO2/WebAuthn** provides stronger protection against credential phishing |
| 👥 | User awareness training is **critical but insufficient alone** |
| 📡 | **Layered security controls** and behavioral analytics enhance detection |
| 🔍 | Regular security assessments help **identify organizational vulnerabilities** |

### ➡️ Next Steps

- 🔐 Research **FIDO2 implementation** best practices
- 📡 Explore advanced detection techniques using **SIEM platforms**
- 📚 Study real-world **MFA bypass case studies**
- 🚑 Practice **incident response** for compromised accounts

---

<div align="center">

[![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cloud%20Learning%20Platform-blue?style=for-the-badge&logo=cloud&logoColor=white)](https://alnafi.com)
[![Red Team](https://img.shields.io/badge/Domain-Red%20Team%20%26%20Defense-red?style=for-the-badge&logo=hackthebox&logoColor=white)]()
[![Ethics](https://img.shields.io/badge/Use-Authorized%20Lab%20Environment%20Only-critical?style=for-the-badge&logo=shield&logoColor=white)]()

**Built with ❤️ for the next generation of cybersecurity professionals**

*© Al Nafi — Cybersecurity Training Program*

</div>
