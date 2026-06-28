<div align="center">

```
 ██████╗████████╗██╗    ██████╗  █████╗ ██████╗ ███████╗███████╗██████╗
██╔════╝╚══██╔══╝██║    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
██║        ██║   ██║    ██████╔╝███████║██████╔╝███████╗█████╗  ██████╔╝
██║        ██║   ██║    ██╔═══╝ ██╔══██║██╔══██╗╚════██║██╔══╝  ██╔══██╗
╚██████╗   ██║   ██║    ██║     ██║  ██║██║  ██║███████║███████╗██║  ██║
 ╚═════╝   ╚═╝   ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
```

# 🧠 Parse Real CTI Reports & Map to ATT&CK
### Cyber Threat Intelligence Analysis & MITRE ATT&CK Framework Mapping

*Extract. Map. Visualize. Operationalize.*

---

[![Platform](https://img.shields.io/badge/Platform-Al_Nafi_Cloud_Lab-blueviolet?style=for-the-badge&logo=cloudflare&logoColor=white)](/)
[![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-v12-orange?style=for-the-badge&logo=mitre)](https://attack.mitre.org/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)](/)
[![Type](https://img.shields.io/badge/Type-Hands--On_Lab-red?style=for-the-badge)](/)

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![JSON](https://img.shields.io/badge/JSON-Output-000000?style=for-the-badge&logo=json&logoColor=white)](/)

[![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](/)
[![Regex](https://img.shields.io/badge/Regex-IOC_Extraction-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)](/)
[![NLTK](https://img.shields.io/badge/NLTK-NLP-FF6B6B?style=for-the-badge&logo=python&logoColor=white)](https://www.nltk.org/)
[![Navigator](https://img.shields.io/badge/ATT%26CK-Navigator-FF4500?style=for-the-badge)](https://mitre-attack.github.io/attack-navigator/)

</div>

---

## 🎯 Lab Overview

In this hands-on lab, you will build a complete **Cyber Threat Intelligence (CTI) analysis pipeline** from scratch. Using Python, you will parse real-world style threat reports, extract Indicators of Compromise (IOCs), map adversary behaviors to the **MITRE ATT&CK framework**, and generate visual intelligence outputs ready for red team planning.

---

## 📚 Learning Objectives

By the end of this lab, you will be able to:

| # | Objective |
|---|-----------|
| 🔍 1 | Extract threat intelligence indicators from CTI reports using Python |
| 🗺️ 2 | Map extracted indicators to MITRE ATT&CK tactics and techniques |
| 📊 3 | Create ATT&CK Navigator layer files for visualization |
| 📋 4 | Generate actionable intelligence reports for red team operations |

---

## 🧰 Prerequisites

> ✅ Basic Python programming knowledge
> ✅ Understanding of cybersecurity fundamentals
> ✅ Familiarity with Linux command line
> ✅ Basic knowledge of MITRE ATT&CK framework

---

## 🖥️ Lab Environment

**Al Nafi** provides pre-configured Linux cloud machines.
Click **▶️ Start Lab** to access your environment — Python 3, pip, and all necessary tools are pre-installed.

```
Lab Path:  ~/cti-lab/
├── 📁 reports/           → Raw CTI report files
├── 📁 parsed_data/       → JSON output from parser
└── 📁 visualizations/    → Charts, dashboards, Navigator layers
```

---

## 📋 Task 1 — Set Up Environment & Create Sample CTI Data

### 🔧 Step 1: Prepare Working Directory

```bash
mkdir -p ~/cti-lab/{reports,parsed_data,visualizations}
cd ~/cti-lab
```

### 📦 Step 2: Install Required Dependencies

```bash
pip3 install requests pandas matplotlib seaborn pdfplumber nltk
python3 -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### 📄 Step 3: Create Sample CTI Report

```bash
cat > reports/apt_report.txt << 'EOF'
THREAT INTELLIGENCE REPORT: APT-FINANCE-2024

Executive Summary:
APT-FINANCE-2024 targets financial institutions using sophisticated techniques.

Attack Chain:
1. Initial Access: Spear phishing emails with malicious attachments
2. Execution: PowerShell scripts and macro-enabled documents
3. Persistence: Registry run keys and scheduled tasks
4. Credential Access: Mimikatz for credential dumping from LSASS
5. Lateral Movement: PSExec and WMI for network propagation
6. Command and Control: HTTPS beaconing to external servers
7. Exfiltration: Data theft via encrypted channels

Infrastructure:
C2 Servers:
- 203.0.113.45
- 198.51.100.78
- malicious-c2.example.com
- backup-server.attacker.net

File Hashes:
MD5:    d41d8cd98f00b204e9800998ecf8427e
SHA1:   da39a3ee5e6b4b0d3255bfef95601890afd80709
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

Phishing Infrastructure:
- phishing@fake-bank.com
- security-alert@malicious-domain.net
- https://fake-login.badsite.org/portal
- https://malware-payload.example.com/update.exe

Techniques Observed:
- Spear phishing attachments
- Credential dumping via mimikatz
- Lateral movement using PSExec
- Registry key persistence mechanisms
- Command and control over HTTPS
- Data exfiltration to external servers
EOF
```

---

## 📋 Task 2 — Build the CTI Parser

### 🔧 Step 1: Create `cti_parser.py`

```python
#!/usr/bin/env python3
"""
CTI Report Parser — Extracts indicators from threat reports
"""

import re
import json
from collections import defaultdict

class CTIParser:
    def __init__(self):
        # 📦 Indicator storage buckets
        self.indicators = {
            'ip_addresses': [],
            'domains': [],
            'file_hashes': [],
            'urls': [],
            'email_addresses': [],
            'techniques': []
        }

        # 🔍 Regex patterns for technique detection
        self.technique_patterns = {
            'spear_phishing':     r'spear.?phishing',
            'credential_dumping': r'credential.?dump|mimikatz|lsass',
            'lateral_movement':   r'lateral.?movement|psexec|wmi',
            'persistence':        r'persistence|registry.?key|scheduled.?task',
            'command_control':    r'command.?control|c2|beacon',
            'data_exfiltration':  r'exfiltration|data.?theft'
        }

    def extract_indicators(self, text):
        """
        Extract various IOCs from text content.

        Args:
            text: String content from CTI report
        """
        # TODO: 🌐 Extract IP addresses
        # Pattern: \b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b

        # TODO: 🔗 Extract domains
        # Pattern: \b[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.([a-zA-Z]{2,})\b

        # TODO: #️⃣  Extract hashes (MD5=32, SHA1=40, SHA256=64 hex chars)

        # TODO: 🔗 Extract URLs
        # Pattern: https?://[^\s<>"{}|\\^`\[\]]+

        # TODO: 📧 Extract email addresses
        # Pattern: \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b

        # TODO: 🎯 Match techniques using self.technique_patterns
        pass

    def parse_file(self, filepath):
        """
        Parse CTI report file and extract indicators.

        Args:
            filepath: Path to report file
        """
        # TODO: 📂 Read file content
        # TODO: ⚙️  Call extract_indicators()
        # TODO: 📤 Return extracted indicators
        pass

    def clean_indicators(self):
        """Remove duplicates and filter false positives."""
        # TODO: 🗑️  Deduplicate all indicator lists
        # TODO: 🚫 Filter private IPs (10.x, 192.168.x, 172.16-31.x)
        # TODO: ✅ Filter common legitimate domains
        pass

    def save_results(self, output_file):
        """Save parsed indicators to JSON file."""
        # TODO: 🧹 Clean indicators
        # TODO: 💾 Write to JSON with proper formatting
        # TODO: 📊 Print summary statistics
        pass

if __name__ == "__main__":
    parser = CTIParser()
    # TODO: 📄 Parse the sample report
    # TODO: 💾 Save results to parsed_data/indicators.json
```

### ▶️ Step 2: Implement and Test Parser

```bash
chmod +x cti_parser.py
python3 cti_parser.py
```

> ✅ **Expected Output:** `parsed_data/indicators.json` with extracted IPs, domains, hashes, URLs, emails, and techniques.

---

## 📋 Task 3 — Map Indicators to ATT&CK Framework

### 🔧 Step 1: Create `attack_mapper.py`

```python
#!/usr/bin/env python3
"""
ATT&CK Mapper — Maps CTI indicators to MITRE ATT&CK techniques
"""

import json

class AttackMapper:
    def __init__(self):
        # 🗺️ Technique → ATT&CK ID mappings
        self.technique_mappings = {
            'spear_phishing': {
                'id':     'T1566.001',
                'name':   'Spearphishing Attachment',
                'tactic': 'Initial Access'
            },
            'credential_dumping': {
                'id':     'T1003',
                'name':   'OS Credential Dumping',
                'tactic': 'Credential Access'
            },
            'lateral_movement': {
                'id':     'T1021',
                'name':   'Remote Services',
                'tactic': 'Lateral Movement'
            },
            'persistence': {
                'id':     'T1547.001',
                'name':   'Registry Run Keys',
                'tactic': 'Persistence'
            },
            'command_control': {
                'id':     'T1071.001',
                'name':   'Web Protocols',
                'tactic': 'Command and Control'
            },
            'data_exfiltration': {
                'id':     'T1041',
                'name':   'Exfiltration Over C2',
                'tactic': 'Exfiltration'
            }
        }

    def load_indicators(self, filepath):
        """Load parsed indicators from JSON file."""
        # TODO: 📂 Read and return JSON data
        pass

    def map_to_attack(self, indicators):
        """
        Map extracted techniques to ATT&CK framework.

        Args:
            indicators: Dictionary of parsed indicators

        Returns:
            List of mapped techniques with ATT&CK IDs
        """
        # TODO: 🔄 Iterate through indicators['techniques']
        # TODO: 🗺️  Map each to ATT&CK using self.technique_mappings
        # TODO: 📤 Return list of mapped techniques
        pass

    def create_navigator_layer(self, mapped_techniques, output_file):
        """
        Create ATT&CK Navigator layer JSON file.

        Args:
            mapped_techniques: List of mapped techniques
            output_file: Path to save layer file
        """
        # 🏗️ Navigator layer scaffold
        layer = {
            "name": "CTI Analysis Results",
            "versions": {
                "attack":    "12",
                "navigator": "4.8.1",
                "layer":     "4.4"
            },
            "domain":      "enterprise-attack",
            "description": "Mapped from CTI report analysis",
            "techniques":  []  # TODO: Populate this list
            # Each entry needs: techniqueID, tactic, color, enabled
        }

        # TODO: 💾 Write layer to JSON file
        pass

    def generate_report(self, indicators, mapped_techniques, output_file):
        """Generate comprehensive mapping report."""
        # TODO: 📊 Calculate statistics (total indicators, techniques, tactics)
        # TODO: 📋 Create report dictionary with summary and details
        # TODO: 💾 Save to JSON file
        # TODO: 🖨️  Print summary to console
        pass

if __name__ == "__main__":
    mapper = AttackMapper()
    # TODO: 📥 Load indicators from parsed_data/indicators.json
    # TODO: 🗺️  Map techniques to ATT&CK
    # TODO: 🗂️  Create Navigator layer file
    # TODO: 📋 Generate mapping report
```

### ▶️ Step 2: Execute Mapping

```bash
chmod +x attack_mapper.py
python3 attack_mapper.py
```

> ✅ **Expected Output:** ATT&CK Navigator layer file + comprehensive mapping report.

---

## 📋 Task 4 — Visualize Results

### 🔧 Step 1: Create `visualize_results.py`

```python
#!/usr/bin/env python3
"""
CTI Visualization — Creates charts and graphs from analysis results
"""

import json
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

class CTIVisualizer:
    def __init__(self):
        plt.style.use('seaborn-v0_8-darkgrid')
        # 🎨 Color palette for charts
        self.colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']

    def load_data(self, indicators_file, mapping_file):
        """Load analysis results from JSON files."""
        # TODO: 📂 Load both JSON files
        # TODO: 📤 Return indicators and mapping data
        pass

    def plot_indicator_distribution(self, indicators, output_file):
        """
        Create bar chart of indicator types and counts.

        Args:
            indicators: Dictionary of indicators
            output_file: Path to save chart image
        """
        # TODO: 📊 Count indicators by type
        # TODO: 📊 Create bar chart with matplotlib
        # TODO: 🏷️  Add labels and title
        # TODO: 💾 Save figure to file
        pass

    def plot_tactic_coverage(self, mapping_data, output_file):
        """Create visualization of ATT&CK tactic coverage."""
        # TODO: 🎯 Extract tactics from mapping data
        # TODO: 🔢 Count techniques per tactic
        # TODO: 📊 Create horizontal bar chart
        # TODO: 💾 Save figure
        pass

    def plot_technique_timeline(self, mapped_techniques, output_file):
        """Create attack chain visualization."""
        # TODO: ⏱️  Order techniques by typical attack progression
        # TODO: 🔗 Create timeline or flow diagram
        # TODO: 💾 Save visualization
        pass

    def generate_dashboard(self, indicators, mapping_data):
        """Create comprehensive dashboard with multiple visualizations."""
        # TODO: 🖼️  Create figure with subplots (2x2 grid)
        # TODO: 📊 Add indicator distribution chart
        # TODO: 🎯 Add tactic coverage chart
        # TODO: 📈 Add technique frequency chart
        # TODO: 📋 Add summary statistics text
        # TODO: 💾 Save complete dashboard
        pass

if __name__ == "__main__":
    viz = CTIVisualizer()
    # TODO: 📥 Load data files
    # TODO: 📊 Generate all visualizations
    # TODO: 🖥️  Create dashboard
```

### ▶️ Step 2: Generate Visualizations

```bash
chmod +x visualize_results.py
python3 visualize_results.py
```

### 🌐 Step 3: View ATT&CK Navigator Layer

```
1. 🌐 Visit:  https://mitre-attack.github.io/attack-navigator/
2. 📂 Click:  "Open Existing Layer"
3. 📤 Upload: visualizations/attack_layer.json
4. 🔍 Explore mapped techniques across all ATT&CK tactics
```

---

## 🗺️ ATT&CK Technique Coverage — APT-FINANCE-2024

| ATT&CK ID | Technique Name | Tactic | Source Indicator |
|-----------|----------------|--------|-----------------|
| T1566.001 | Spearphishing Attachment | Initial Access | Phishing emails |
| T1003 | OS Credential Dumping | Credential Access | Mimikatz / LSASS |
| T1021 | Remote Services | Lateral Movement | PSExec / WMI |
| T1547.001 | Registry Run Keys | Persistence | Registry modification |
| T1071.001 | Web Protocols | Command and Control | HTTPS beaconing |
| T1041 | Exfiltration Over C2 | Exfiltration | Encrypted channels |

---

## ✅ Expected Lab Outcomes

Upon successful completion you will have produced:

| Output | Location | Description |
|--------|----------|-------------|
| 📄 `indicators.json` | `parsed_data/` | IPs, domains, hashes, URLs, emails |
| 🗺️ `attack_layer.json` | `visualizations/` | ATT&CK Navigator layer file |
| 📊 `dashboard.png` | `visualizations/` | Visual chart dashboard |
| 📋 `mapping_report.json` | `parsed_data/` | Full technique mapping report |

---

## 🔧 Troubleshooting

| ❗ Issue | ✅ Solution |
|---------|-----------|
| Parser extracts too many false positives | Enhance `clean_indicators()` — add exclusion lists for known-good IPs/domains; refine regex patterns |
| No techniques extracted from report | Check `technique_patterns` dictionary; verify report has keyword matches; add more regex variations |
| Navigator layer doesn't load | Validate JSON with `python3 -m json.tool`; ensure technique IDs match `T####` format; verify all required fields |

---

## 💡 Key Takeaways

> 🤖 **Automation** — Automated parsing saves time and improves consistency across large report volumes
>
> 🗺️ **Standardization** — ATT&CK mapping provides a common language for threat understanding across teams
>
> 📊 **Visualization** — Charts and Navigator layers make findings accessible to both technical and executive audiences
>
> 🔴 **Operationalization** — Structured intelligence directly supports red team planning and purple team exercises

---

## 🚀 Next Steps

After completing this lab, continue your learning journey:

- 🔗 Apply these techniques to real-world public CTI reports (VirusTotal, AlienVault OTX, CISA advisories)
- 🔗 Integrate the pipeline with SIEM/SOAR platforms for automated ingestion
- 🔗 Develop custom parsers for organization-specific intelligence sources
- 🔗 Build a threat actor profile database using mapped TTPs

---

## 📚 References

- [MITRE ATT&CK Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/)
- [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)
- [CISA Threat Intelligence Reports](https://www.cisa.gov/resources-tools/resources/malware-analysis-reports)
- [AlienVault OTX](https://otx.alienvault.com/)
- [NLTK Documentation](https://www.nltk.org/)

---

<div align="center">

**Built with ❤️ for the next generation of cybersecurity professionals**

*Al Nafi — Cloud-Based Cybersecurity Training Platform*

[![Al Nafi](https://img.shields.io/badge/Al_Nafi-Cybersecurity_Training-blueviolet?style=for-the-badge)](/)
[![CTI](https://img.shields.io/badge/Domain-Threat_Intelligence-orange?style=for-the-badge)](/)
[![ATT&CK](https://img.shields.io/badge/Framework-MITRE_ATT%26CK-red?style=for-the-badge)](https://attack.mitre.org/)

</div>
