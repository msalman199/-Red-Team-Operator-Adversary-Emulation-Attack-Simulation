<div align="center">

```
 █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗███████╗██████╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████║   ██║      ██║   ███████║██║     █████╔╝ █████╗  ██████╔╝
██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
```

# 🕵️ Build Attacker Profile & Select Campaign Objectives
### Threat Actor Profiling · ATT&CK TTP Extraction · Red Team Campaign Planning

*Profile. Plan. Emulate. — Intelligence-Driven Red Team Operations*

---

[![Platform](https://img.shields.io/badge/Platform-Al_Nafi_Cloud_Lab-blueviolet?style=for-the-badge&logo=cloudflare&logoColor=white)](/)
[![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-Enterprise-orange?style=for-the-badge&logo=mitre)](https://attack.mitre.org/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)](/)
[![Type](https://img.shields.io/badge/Type-Hands--On_Lab-red?style=for-the-badge)](/)

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![YAML](https://img.shields.io/badge/YAML-Output-CB171E?style=for-the-badge&logo=yaml&logoColor=white)](/)
[![JSON](https://img.shields.io/badge/JSON-Profiles-000000?style=for-the-badge&logo=json&logoColor=white)](/)
[![Django](https://img.shields.io/badge/Django-TRAM_Backend-092E20?style=for-the-badge&logo=django&logoColor=white)](/)

[![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04_LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](/)
[![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=for-the-badge&logo=git&logoColor=white)](/)
[![TRAM](https://img.shields.io/badge/TRAM-ATT%26CK_Mapping-FF4500?style=for-the-badge)](https://github.com/center-for-threat-informed-defense/tram)
[![Linux](https://img.shields.io/badge/Linux-CLI-4EAA25?style=for-the-badge&logo=linux&logoColor=white)](/)

</div>

---

## 🎯 Lab Overview

In this lab you will build a complete **threat actor profiling and campaign planning pipeline**. Using the **TRAM** tool and custom Python scripting, you will analyze real-world threat intelligence reports, extract adversary TTPs, map them to MITRE ATT&CK, and auto-generate structured red team campaign plans — transforming raw intelligence into operational objectives.

---

## 📚 Lab Objectives

By the end of this lab, you will be able to:

| # | Objective |
|---|-----------|
| 🧠 1 | Build comprehensive threat actor profiles using MITRE ATT&CK framework |
| 🔍 2 | Analyze threat intelligence reports to extract TTPs |
| 🎯 3 | Define strategic campaign objectives based on threat actor analysis |
| 📋 4 | Create structured documentation for red team operations |
| 🤖 5 | Automate profile analysis using Python scripting |

---

## 🧰 Prerequisites

> ✅ Basic understanding of cybersecurity concepts
> ✅ Familiarity with Linux command line
> ✅ Basic knowledge of MITRE ATT&CK framework
> ✅ Python programming fundamentals
> ✅ Understanding of threat intelligence concepts

---

## 🖥️ Lab Environment

**Al Nafi** provides pre-configured Linux-based cloud machines.
Click **▶️ Start Lab** to access your environment.

| Component | Version |
|-----------|---------|
| 🐧 OS | Ubuntu 22.04 LTS |
| 🐍 Python | 3.10+ |
| 🛠️ Tools | Git, nano, vim, Firefox |
| 📦 Dependencies | Pre-installed |

```
Working Directories:
~/threat_reports/         → Raw CTI report files
~/attacker_profiles/      → JSON threat actor profiles
~/campaign_plans/         → Generated YAML/JSON campaign plans
```

---

## 📋 Task 1 — Set Up TRAM & Create Threat Reports

### 🔧 Step 1.1: Install TRAM

```bash
# 📥 Clone TRAM repository
cd ~
git clone https://github.com/center-for-threat-informed-defense/tram.git
cd tram

# 📦 Install dependencies
pip3 install -r requirements.txt

# 🗄️ Initialize database
python3 manage.py migrate
python3 manage.py createsuperuser

# 🚀 Start TRAM service
python3 manage.py runserver 0.0.0.0:8000 &
```

### 📄 Step 1.2: Create Threat Intelligence Report

```bash
# 📁 Create directory structure
mkdir -p ~/threat_reports
cd ~/threat_reports

# ✏️ Create APT29 threat report
nano apt29_report.txt
```

Add the following content to the file:

```
THREAT INTELLIGENCE REPORT: APT29 (Cozy Bear)

Executive Summary:
APT29 is a sophisticated Russian state-sponsored threat actor targeting government,
diplomatic, and technology organizations since 2008.

Attack Techniques Observed:

Initial Access:
- Spear-phishing with malicious attachments
- Supply chain compromises
- Exploitation of public-facing applications

Execution:
- PowerShell script execution
- WMI for remote execution
- Scheduled task creation

Persistence:
- Registry modification
- Windows service creation
- Bootkit installation

Privilege Escalation:
- CVE exploitation (CVE-2020-0688, CVE-2019-19781)
- Token impersonation
- UAC bypass

Defense Evasion:
- Process injection (DLL injection)
- Obfuscated PowerShell
- Timestomping
- Process masquerading

Credential Access:
- Mimikatz credential dumping
- LSASS memory dumping
- Kerberoasting attacks

Discovery:
- Network service scanning
- Active Directory enumeration
- WMI queries for system information

Lateral Movement:
- RDP usage
- Windows Admin Shares
- Pass-the-hash attacks

Collection:
- Exchange server email collection
- Network share file discovery
- Screen capture

Command and Control:
- HTTPS communication
- Domain fronting
- DNS tunneling

Exfiltration:
- Data compression and encryption
- DNS-based exfiltration
- Cloud storage services

Tools: CozyDuke, SeaDuke, CloudDuke, PowerDuke, WellMess
```

### 🌐 Step 1.3: Use TRAM for ATT&CK Mapping

```
1. 🌐 Open browser:    firefox http://localhost:8000
2. 🔐 Login:           Use superuser credentials
3. ➕ Click:           "New Report"
4. 📝 Enter details:
   - Name:             "APT29 Profile Analysis"
   - Description:      "Comprehensive APT29 TTP analysis"
5. 📋 Paste:           Threat report content
6. ⚙️  Click:          "Analyze Report"
7. ✅ Review:          Validate ATT&CK technique mappings
8. 💾 Export:          JSON → ~/attacker_profiles/apt29_profile.json
```

---

## 📋 Task 2 — Create Profile Analysis Script

### 🔧 Step 2.1: Build `profile_analyzer.py`

```bash
cd ~
nano profile_analyzer.py
```

```python
#!/usr/bin/env python3
"""
Attacker Profile Analyzer
Students: Complete the TODO sections to implement full functionality
"""

import json
import yaml
import datetime
from collections import defaultdict
import argparse

class AttackerProfileAnalyzer:
    def __init__(self):
        self.attack_framework = self.load_attack_framework()

    def load_attack_framework(self):
        """Load simplified ATT&CK framework structure."""
        framework = {
            "tactics": {
                "TA0001": {"name": "Initial Access"},
                "TA0002": {"name": "Execution"},
                "TA0003": {"name": "Persistence"},
                "TA0004": {"name": "Privilege Escalation"},
                "TA0005": {"name": "Defense Evasion"},
                "TA0006": {"name": "Credential Access"},
                "TA0007": {"name": "Discovery"},
                "TA0008": {"name": "Lateral Movement"},
                "TA0009": {"name": "Collection"},
                "TA0011": {"name": "Command and Control"},
                "TA0010": {"name": "Exfiltration"},
                "TA0040": {"name": "Impact"}
            }
        }
        return framework

    def analyze_profile(self, profile_data):
        """
        Analyze attacker profile and extract key characteristics.

        Args:
            profile_data: Dictionary containing threat actor profile

        Returns:
            Dictionary with analysis results
        """
        # TODO: 🏷️  Extract threat actor name
        # TODO: 📊 Assess sophistication level
        # TODO: 🎯 Extract primary motivations
        # TODO: 🏢 Identify target sectors
        # TODO: 🔍 Analyze attack patterns
        # TODO: 📤 Return comprehensive analysis dictionary
        pass

    def assess_sophistication(self, profile_data):
        """
        Assess threat actor sophistication level.

        Args:
            profile_data: Profile dictionary

        Returns:
            String: "Advanced Persistent Threat (APT)", "Intermediate", or "Basic"
        """
        # TODO: 🔢 Count advanced technique indicators
        # Keywords: "supply chain", "zero-day", "kernel", "bootkit", "domain fronting"
        # TODO: 📊 Analyze technique complexity
        # TODO: 📤 Return sophistication assessment
        pass

    def extract_motivations(self, profile_data):
        """
        Extract primary motivations from profile.

        Args:
            profile_data: Profile dictionary

        Returns:
            List of motivation strings
        """
        motivation_keywords = {
            "financial":   ["money", "financial", "bank", "cryptocurrency"],
            "espionage":   ["intelligence", "espionage", "government", "state-sponsored"],
            "disruption":  ["disruption", "destruction", "sabotage"],
            "hacktivism":  ["activist", "political", "ideology"]
        }

        # TODO: 🔍 Search description for motivation keywords
        # TODO: 📤 Return list of identified motivations
        pass

    def generate_campaign_objectives(self, analysis):
        """
        Generate campaign objectives based on profile analysis.

        Args:
            analysis: Analysis dictionary from analyze_profile()

        Returns:
            List of campaign objective strings
        """
        objectives = []

        # TODO: 💰 Generate objectives based on motivations (financial/espionage/disruption)
        # TODO: 🏢 Add sector-specific objectives
        # TODO: 🔴 Include APT-level sophistication objectives
        # TODO: 🗑️  Return unique objectives list
        pass

    def create_campaign_plan(self, analysis, objectives):
        """
        Create comprehensive campaign plan.

        Args:
            analysis: Profile analysis dictionary
            objectives: List of campaign objectives

        Returns:
            Dictionary containing complete campaign plan
        """
        plan = {
            "campaign_metadata": {
                "name": f"Red Team Campaign - {analysis.get('threat_actor', 'Unknown')} Emulation",
                "created_date": datetime.datetime.now().isoformat(),
                # TODO: 📋 Add additional metadata fields
            },
            "threat_profile":      analysis,
            "campaign_objectives": objectives,
            # TODO: ⚔️  Add attack phases
            # TODO: ✅ Add success criteria
            # TODO: ⚠️  Add risk assessment
        }

        return plan

    def generate_attack_phases(self, analysis):
        """
        Generate attack phases based on profile.

        Args:
            analysis: Profile analysis dictionary

        Returns:
            List of attack phase dictionaries
        """
        # TODO: 📋 Define standard attack phases
        # TODO: 🔧 Customize based on threat actor capabilities
        # TODO: 🎯 Include technique IDs for each phase
        # TODO: 📤 Return phases list
        pass


def main():
    parser = argparse.ArgumentParser(description="Analyze attacker profiles")
    parser.add_argument("--profile", required=True, help="Path to profile JSON")
    parser.add_argument("--output",  required=True, help="Output file path")
    parser.add_argument("--format",  choices=["json", "yaml"], default="yaml")

    args = parser.parse_args()

    # TODO: ⚙️  Initialize analyzer
    # TODO: 📥 Load profile data from file
    # TODO: 🔍 Perform analysis
    # TODO: 🎯 Generate objectives
    # TODO: 📋 Create campaign plan
    # TODO: 💾 Save output in specified format
    # TODO: 🖨️  Print summary information

if __name__ == "__main__":
    main()
```

```bash
chmod +x profile_analyzer.py
```

### 📄 Step 2.2: Create Sample APT29 Profile Data

```bash
mkdir -p ~/attacker_profiles
nano ~/attacker_profiles/apt29_profile.json
```

```json
{
  "name": "APT29 (Cozy Bear)",
  "attribution": "Russian Foreign Intelligence Service (SVR)",
  "first_seen": "2008",
  "description": "APT29 is a sophisticated threat actor targeting government organizations, diplomatic entities, and technology companies. They employ advanced techniques including supply chain compromises, zero-day exploits, and living-off-the-land techniques.",
  "motivations": ["espionage", "intelligence_gathering"],
  "target_sectors": ["government", "diplomatic", "technology"],
  "sophistication": "advanced",
  "techniques": [
    "T1566.001", "T1195.002", "T1059.001", "T1047",
    "T1053.005", "T1112",   "T1055",     "T1027",
    "T1003.001", "T1083",   "T1021.001", "T1114.002",
    "T1071.001", "T1041"
  ],
  "malware_families": ["CozyDuke", "SeaDuke", "CloudDuke", "PowerDuke"],
  "infrastructure": {
    "c2_methods": ["https", "domain_fronting", "dns_tunneling"],
    "hosting":    ["compromised_legitimate_sites", "bulletproof_hosting"]
  }
}
```

---

## 📋 Task 3 — Implement Analysis Functions

### 🔧 Step 3.1: Complete Sophistication Assessment

Implement `assess_sophistication()` using the following logic:

```
Advanced Keywords to detect:
  → "supply chain", "zero-day", "kernel", "bootkit", "domain fronting"

Scoring Rules:
  ≥ 4 advanced keywords  OR  > 15 techniques  →  "Advanced Persistent Threat (APT)"
  ≥ 2 advanced keywords  OR  > 8  techniques  →  "Intermediate"
  Otherwise                                   →  "Basic"
```

### 🔧 Step 3.2: Complete Motivation Extraction

Implement `extract_motivations()`:

```
→ Search profile description against motivation_keywords dictionary
→ Return all matching motivation categories as a list
→ Return ["unknown"] if no keywords match
```

### 🔧 Step 3.3: Complete Objective Generation

Implement `generate_campaign_objectives()` using the following objective map:

| Motivation | Campaign Objectives |
|------------|-------------------|
| 💰 Financial | Test transaction security, payment systems, cryptocurrency wallets |
| 🕵️ Espionage | Test data classification, DLP capabilities, insider threat detection |
| 💥 Disruption | Test business continuity, recovery capabilities, backup processes |

> Also add **sector-specific** and **APT-level sophistication** objectives. Remove duplicates before returning.

### 🔧 Step 3.4: Complete Attack Phase Generation

Implement `generate_attack_phases()` — each phase must follow this structure:

```python
{
    "phase":       "Phase Name",
    "description": "Phase description",
    "duration":    "Estimated time",
    "techniques":  ["T1234", "T5678"]
}
```

Required phases in sequence:

```
1  → Reconnaissance
2  → Initial Access
3  → Execution & Persistence
4  → Privilege Escalation
5  → Defense Evasion
6  → Credential Access
7  → Discovery
8  → Lateral Movement
9  → Collection
10 → Exfiltration
11 → Impact  ⚠️  (only if disruption motivation is present)
```

---

## 📋 Task 4 — Test & Generate Campaign Plans

### ▶️ Step 4.1: Run Profile Analysis

```bash
python3 profile_analyzer.py \
    --profile ~/attacker_profiles/apt29_profile.json \
    --output  ~/campaign_plans/apt29_campaign.yaml \
    --format  yaml
```

### 📄 Step 4.2: Review Generated Campaign Plan

```bash
cat ~/campaign_plans/apt29_campaign.yaml
```

> ✅ **Expected Output Structure:**

```yaml
campaign_metadata:
  name: "Red Team Campaign - APT29 Emulation"
  created_date: "2024-xx-xxTxx:xx:xx"
  threat_actor: "APT29 (Cozy Bear)"

threat_profile:
  sophistication: "Advanced Persistent Threat (APT)"
  motivations: [espionage, intelligence_gathering]
  target_sectors: [government, diplomatic, technology]

campaign_objectives:
  - Test data classification controls
  - Assess DLP capabilities
  - Evaluate insider threat detection

attack_phases:
  - phase: "Reconnaissance"
    ...
  - phase: "Initial Access"
    ...

success_criteria: [...]
risk_assessment: [...]
```

### 🏆 Step 4.3: Challenge — Lazarus Group Profile

Create a second profile for **Lazarus Group** and compare campaign outputs:

```json
{
  "name": "Lazarus Group",
  "motivations": ["financial", "espionage", "disruption"],
  "target_sectors": ["financial", "cryptocurrency", "entertainment"],
  "sophistication": "advanced",
  "techniques": ["T1566.001", "T1189", "T1195.002", "T1553.002"]
}
```

```bash
python3 profile_analyzer.py \
    --profile ~/attacker_profiles/lazarus_profile.json \
    --output  ~/campaign_plans/lazarus_campaign.yaml \
    --format  yaml
```

> 🔍 Compare the two generated plans — observe how different motivations shape campaign objectives and attack phases.

---

## 🗺️ ATT&CK Tactic Coverage — APT29

| Tactic ID | Tactic Name | Techniques Used |
|-----------|-------------|-----------------|
| TA0001 | Initial Access | T1566.001, T1195.002 |
| TA0002 | Execution | T1059.001, T1047, T1053.005 |
| TA0003 | Persistence | T1112, T1053.005 |
| TA0004 | Privilege Escalation | CVE-2020-0688, CVE-2019-19781 |
| TA0005 | Defense Evasion | T1055, T1027 |
| TA0006 | Credential Access | T1003.001 |
| TA0007 | Discovery | T1083 |
| TA0008 | Lateral Movement | T1021.001 |
| TA0009 | Collection | T1114.002 |
| TA0011 | Command and Control | T1071.001 |
| TA0010 | Exfiltration | T1041 |

---

## ✅ Expected Lab Outcomes

| Output | Location | Description |
|--------|----------|-------------|
| 🌐 TRAM Instance | `http://localhost:8000` | Live ATT&CK mapping tool |
| 📄 `apt29_profile.json` | `~/attacker_profiles/` | Structured threat actor profile |
| 🐍 `profile_analyzer.py` | `~/` | Working Python analyzer script |
| 📋 `apt29_campaign.yaml` | `~/campaign_plans/` | Full red team campaign plan |
| 📋 `lazarus_campaign.yaml` | `~/campaign_plans/` | Comparative Lazarus campaign |

---

## 🔧 Troubleshooting

| ❗ Issue | ✅ Solution |
|---------|-----------|
| TRAM won't start | Check port: `netstat -tuln \| grep 8000` → Kill with `pkill -f runserver` → Verify Django: `pip3 list \| grep -i django` |
| Script execution errors | Fix permissions: `chmod +x profile_analyzer.py` → Check Python: `python3 --version` (requires 3.8+) → Validate JSON: `python3 -m json.tool apt29_profile.json` |
| Missing analysis results | Ensure all TODO sections are implemented → Verify profile JSON has required fields → Check functions return values instead of `pass` |

---

## 💡 Key Takeaways

> 🎯 **Intelligence-Driven Planning** — Threat actor profiles guide red team campaigns toward realistic, meaningful objectives
>
> 🗺️ **Standardized Taxonomy** — MITRE ATT&CK provides a universal language for describing and communicating adversary behavior
>
> 🤖 **Automation** — Scripted analysis improves consistency and accelerates campaign planning across multiple threat actors
>
> 🧠 **Motivation Matters** — Understanding adversary motivations is what separates realistic emulation from generic penetration testing

---

## 🚀 Next Steps

After completing this lab, continue building your red team capabilities:

- 🔗 Expand the profile database with additional threat actors (FIN7, Sandworm, Scattered Spider)
- 🔗 Integrate the analyzer with red team automation frameworks (Caldera, Atomic Red Team)
- 🔗 Develop custom ATT&CK sub-technique mappings for your target environment
- 🔗 Create organization-specific threat profiles based on sector and geopolitical risk

---

## 📚 References

- [MITRE ATT&CK Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/)
- [TRAM — Threat Report ATT&CK Mapper](https://github.com/center-for-threat-informed-defense/tram)
- [APT29 MITRE Profile](https://attack.mitre.org/groups/G0016/)
- [Lazarus Group MITRE Profile](https://attack.mitre.org/groups/G0032/)
- [CTID Adversary Emulation Library](https://github.com/center-for-threat-informed-defense/adversary_emulation_library)

---

<div align="center">

**Built with ❤️ for the next generation of cybersecurity professionals**

*Al Nafi — Cloud-Based Cybersecurity Training Platform*

[![Al Nafi](https://img.shields.io/badge/Al_Nafi-Cybersecurity_Training-blueviolet?style=for-the-badge)](/)
[![Red Team](https://img.shields.io/badge/Domain-Red_Team_Operations-red?style=for-the-badge)](/)
[![ATT&CK](https://img.shields.io/badge/Framework-MITRE_ATT%26CK-orange?style=for-the-badge)](https://attack.mitre.org/)

</div>
