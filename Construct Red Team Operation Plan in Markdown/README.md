<div align="center">

```
 ██████╗██████╗ ██╗███╗   ███╗███████╗ ██████╗ ███╗   ██╗
██╔════╝██╔══██╗██║████╗ ████║██╔════╝██╔═══██╗████╗  ██║
██║     ██████╔╝██║██╔████╔██║███████╗██║   ██║██╔██╗ ██║
██║     ██╔══██╗██║██║╚██╔╝██║╚════██║██║   ██║██║╚██╗██║
╚██████╗██║  ██║██║██║ ╚═╝ ██║███████║╚██████╔╝██║ ╚████║
 ╚═════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝

██╗  ██╗ █████╗ ██╗    ██╗██╗  ██╗
██║  ██║██╔══██╗██║    ██║██║ ██╔╝
███████║███████║██║ █╗ ██║█████╔╝
██╔══██║██╔══██║██║███╗██║██╔═██╗
██║  ██║██║  ██║╚███╔███╔╝██║  ██╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝
```

# 📄 Construct Red Team Operation Plan in Markdown
### Operation Planning · Threat Heatmaps · Executive Reporting · Project CRIMSON HAWK

*Plan. Visualize. Report. — Professional Red Team Documentation from Start to Finish.*

---

[![Platform](https://img.shields.io/badge/Platform-Al_Nafi_Cloud_Lab-blueviolet?style=for-the-badge&logo=cloudflare&logoColor=white)](/)
[![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-Enterprise-orange?style=for-the-badge&logo=mitre)](https://attack.mitre.org/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)](/)
[![Type](https://img.shields.io/badge/Type-Hands--On_Lab-red?style=for-the-badge)](/)

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Heatmaps-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Pandas](https://img.shields.io/badge/Pandas-DataFrames-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

[![Markdown](https://img.shields.io/badge/Markdown-Documentation-000000?style=for-the-badge&logo=markdown&logoColor=white)](/)
[![Bash](https://img.shields.io/badge/Bash-Automation-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)](/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04_LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](/)
[![JSON](https://img.shields.io/badge/JSON-Reports-000000?style=for-the-badge&logo=json&logoColor=white)](/)

</div>

---

## 🎯 Lab Overview

In this lab you will build a **complete professional Red Team engagement package** from scratch — including a structured operation plan, threat intelligence report, Python-generated heatmap visualizations, and a polished executive-ready final report. This mirrors real-world Red Team documentation workflows used in professional security engagements.

---

## 📚 Lab Objectives

By the end of this lab, you will be able to:

| # | Objective |
|---|-----------|
| 📋 1 | Design and document a comprehensive Red Team operation plan in Markdown format |
| 🌡️ 2 | Create visual threat heatmaps using Python and Matplotlib to identify high-risk areas |
| 📊 3 | Generate professional Red Team engagement reports with actionable recommendations |
| 🧠 4 | Apply threat modeling techniques to create realistic attack scenarios |
| 🗂️ 5 | Document findings in a format suitable for stakeholder presentation |

---

## 🧰 Prerequisites

> ✅ Basic understanding of cybersecurity concepts and the MITRE ATT&CK framework
> ✅ Familiarity with Linux command line operations and text editors
> ✅ Basic knowledge of Python programming and data visualization concepts

---

## 🖥️ Lab Environment

**Al Nafi** provides pre-configured Linux cloud machines. Click **▶️ Start Lab** to access your environment.

| Component | Details |
|-----------|---------|
| 🐧 OS | Ubuntu 22.04 LTS |
| 🐍 Python | 3.8+ with pip |
| ✏️ Editors | nano, vim |
| 📦 Libraries | matplotlib, numpy, pandas, seaborn (pre-installed) |

```
Project Structure:
~/redteam-lab3/
├── 📁 docs/          → Operation plan & threat intelligence docs
├── 📁 scripts/       → Python heatmap & analysis scripts
├── 📁 reports/       → Final report & JSON statistics
├── 📁 assets/        → Generated PNG visualizations
└── 📁 report-package/→ Compiled stakeholder-ready package
```

---

## 📋 Task 1 — Create Red Team Operation Plan Structure

### 🔧 Step 1.1: Set Up Project Directory

```bash
mkdir -p ~/redteam-lab3/{docs,scripts,reports,assets}
cd ~/redteam-lab3
```

### 📦 Step 1.2: Install Required Libraries

```bash
pip3 install matplotlib numpy pandas seaborn
python3 -c "import matplotlib, numpy, pandas, seaborn; print('Libraries installed successfully')"
```

### 📄 Step 1.3: Create Operation Plan Template

```bash
nano ~/redteam-lab3/docs/operation-plan.md
```

Paste the following content:

```markdown
# Red Team Operation Plan: Project CRIMSON HAWK

## Executive Summary

### Operation Overview
- **Operation Name**: Project CRIMSON HAWK
- **Target Organization**: Fictional Corp Industries
- **Engagement Type**: Full-scope Red Team Assessment
- **Duration**: 4 weeks
- **Start Date**: 2024-01-15
- **End Date**: 2024-02-12
- **Red Team Lead**: [Your Name]

### Objectives
- Assess detection and response capabilities
- Identify critical vulnerabilities in network infrastructure
- Test employee security awareness through social engineering
- Evaluate physical security controls
- Provide actionable recommendations for security improvements

## Scope and Rules of Engagement

### In-Scope Assets
- Corporate network (192.168.1.0/24)
- Web applications (www.fictionalcorp.com)
- Email systems
- Employee workstations
- Physical facilities (main office)

### Out-of-Scope Assets
- Third-party vendor systems
- Customer data repositories
- Production databases containing PII
- Critical infrastructure systems

### Rules of Engagement
- No destructive activities
- No data exfiltration of sensitive information
- Maintain stealth and avoid detection when possible
- Immediate notification of critical vulnerabilities
- Daily status updates to engagement manager

## Threat Model

### Adversary Profile
**Threat Actor**: Advanced Persistent Threat (APT) Group
**Motivation**: Financial gain and intellectual property theft
**Sophistication Level**: High
**Resources**: Well-funded with custom tools and zero-day exploits

### Attack Scenarios
1. **Initial Access**: Spear-phishing campaign targeting executives
2. **Persistence**: Deploy custom backdoors and establish C2 channels
3. **Privilege Escalation**: Exploit local vulnerabilities and misconfigurations
4. **Lateral Movement**: Use legitimate tools for network reconnaissance
5. **Data Exfiltration**: Identify and access sensitive data repositories

## Methodology and Tactics

### Phase 1: Reconnaissance (Week 1)
- OSINT gathering: Social media, public records, DNS enumeration
- Network scanning: Port scanning, service enumeration
- Social engineering: Pretexting calls, LinkedIn reconnaissance

### Phase 2: Initial Access (Week 2)
- Phishing campaign: Targeted emails with malicious attachments
- Web application testing: SQL injection, XSS, authentication bypass
- Physical access: Badge cloning, tailgating attempts

### Phase 3: Post-Exploitation (Week 3)
- Privilege escalation: Local exploits, credential harvesting
- Lateral movement: Network pivoting, service account abuse
- Persistence: Registry modifications, scheduled tasks

### Phase 4: Objectives and Cleanup (Week 4)
- Data discovery: Locate sensitive information
- Objective completion: Achieve defined goals
- Evidence collection: Document all activities
- System cleanup: Remove artifacts and restore systems

## Tools and Techniques

### Reconnaissance Tools
- Nmap, Recon-ng, theHarvester, Shodan

### Exploitation Tools
- Metasploit, Cobalt Strike, Empire, Custom Scripts

### Post-Exploitation Tools
- Mimikatz, BloodHound, PowerView, Living off the Land

## Communication Plan

### Reporting Schedule
- Daily briefings: 9:00 AM EST via secure channel
- Weekly reports: Detailed progress updates
- Critical findings: Immediate notification within 2 hours
- Final report: Within 5 business days of engagement completion

## Success Criteria

### Primary Objectives
- [ ] Gain initial network access
- [ ] Escalate privileges to domain administrator
- [ ] Access sensitive data repositories
- [ ] Maintain persistence for 72 hours undetected
- [ ] Document all attack paths and vulnerabilities

## Timeline and Milestones

| Week | Phase | Key Activities | Deliverables |
|------|-------|----------------|--------------|
| 1 | Reconnaissance | OSINT, Network Scanning | Reconnaissance Report |
| 2 | Initial Access | Phishing, Web App Testing | Access Documentation |
| 3 | Post-Exploitation | Privilege Escalation, Lateral Movement | Technical Findings |
| 4 | Objectives | Data Discovery, Cleanup | Final Report |
```

> 💾 Save with `Ctrl+X → Y → Enter`

### 📄 Step 1.4: Create Threat Intelligence Document

```bash
nano ~/redteam-lab3/docs/threat-intelligence.md
```

```markdown
# Threat Intelligence Report

## Executive Summary
Threat intelligence analysis for Project CRIMSON HAWK — current threat landscape
and adversary tactics relevant to Fictional Corp Industries.

## Current Threat Landscape

### Industry-Specific Threats
- Financial Sector: Increased targeting by banking trojans
- Healthcare: Ransomware attacks on critical infrastructure
- Manufacturing: Supply chain compromises and IP theft

### Emerging Attack Vectors
- Cloud misconfigurations: 65% increase in cloud-related breaches
- Supply chain attacks: 300% increase in third-party compromises
- Social engineering: 85% of breaches involve human element

## ATT&CK Mapped TTPs

**Initial Access**
- T1566.001 — Spearphishing Attachment
- T1566.002 — Spearphishing Link
- T1190     — Exploit Public-Facing Application

**Persistence**
- T1053.005 — Scheduled Task/Job
- T1547.001 — Registry Run Keys
- T1078     — Valid Accounts

**Privilege Escalation**
- T1068 — Exploitation for Privilege Escalation
- T1134 — Access Token Manipulation
- T1055 — Process Injection

## Threat Actor Profiles

### APT Groups
- APT29 — Russian state-sponsored, healthcare targeting
- APT40 — Chinese maritime and healthcare focus
- FIN7  — Financially motivated, retail and hospitality

### Ransomware Groups
- Conti    — Double extortion tactics
- REvil    — Ransomware-as-a-Service model
- DarkSide — Critical infrastructure targeting

## Recommendations
- Implement multi-factor authentication across all systems
- Conduct regular security awareness training
- Deploy network segmentation and monitoring
- Test and update incident response plans quarterly
```

---

## 📋 Task 2 — Develop Threat Heatmap Visualization Scripts

### 🔧 Step 2.1: Create `threat_heatmap.py`

```bash
nano ~/redteam-lab3/scripts/threat_heatmap.py
```

```python
#!/usr/bin/env python3
"""
Red Team Threat Heatmap Generator
Students: Complete all TODO sections to generate visual threat heatmaps
"""

import matplotlib
matplotlib.use('Agg')  # ⚠️ Required for non-display environments
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os

class ThreatHeatmapGenerator:
    def __init__(self):
        self.output_dir = "../assets"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def create_network_threat_heatmap(self):
        """
        Create a network-based threat heatmap showing threat levels
        across network segments.

        TODO: Complete this function to:
        1. 🌐 Define network_segments list
           → DMZ, Internal LAN, Server Farm, Executive Network, Guest Network
        2. ⚠️  Define threat_types list
           → Malware, Phishing, Insider Threat, APT, DDoS, Data Breach
        3. 📊 Create threat_matrix (5x6 np.array, values 1–10)
        4. 🌡️  Generate heatmap using sns.heatmap()
        5. 💾 Save to assets/network_threat_heatmap.png
        """
        # TODO: 🌐 Define network_segments list
        network_segments = []

        # TODO: ⚠️  Define threat_types list
        threat_types = []

        # TODO: 📊 Create threat_matrix using np.array()
        threat_matrix = np.array([])

        # TODO: 🖼️  Create figure and heatmap with plt.figure() + sns.heatmap()

        # TODO: 🏷️  Add title, axis labels, and save figure
        pass

    def create_attack_timeline_heatmap(self):
        """
        Create an attack timeline heatmap showing activity intensity over time.

        TODO: Complete this function to:
        1. ⏱️  Define time periods (Week 1 → Week 4)
        2. 🎯 Define attack phases
           → Reconnaissance, Initial Access, Persistence, Privilege Escalation,
             Lateral Movement, Exfiltration
        3. 📊 Create activity intensity matrix
        4. 💾 Generate and save heatmap
        """
        # TODO: Implement timeline heatmap
        pass

    def create_vulnerability_severity_heatmap(self):
        """
        Create a vulnerability severity heatmap by system type.

        TODO: Complete this function to:
        1. 🖥️  Define system types
           → Web Servers, Database Servers, Workstations, Network Devices, Cloud Services
        2. 🔴 Define vulnerability categories
           → Critical, High, Medium, Low, Info
        3. 📊 Create vulnerability count matrix
        4. 💾 Generate and save heatmap
        """
        # TODO: Implement vulnerability heatmap
        pass

    def create_risk_assessment_matrix(self):
        """
        Create a risk assessment matrix heatmap (likelihood vs impact).

        TODO: Complete this function to:
        1. 📉 Define likelihood levels (Very Low → Very High)
        2. 💥 Define impact levels (Very Low → Very High)
        3. 🧮 Calculate risk scores: likelihood * impact
        4. 💾 Generate and save heatmap with RdYlGn_r color scheme
        """
        # TODO: Implement risk assessment matrix
        pass

    def generate_all_heatmaps(self):
        """Generate all threat heatmaps."""
        print("🌡️  Generating threat heatmaps...")
        print("-" * 50)

        self.create_network_threat_heatmap()
        self.create_attack_timeline_heatmap()
        self.create_vulnerability_severity_heatmap()
        self.create_risk_assessment_matrix()

        print("-" * 50)
        print("✅ All heatmaps generated successfully!")

def main():
    generator = ThreatHeatmapGenerator()
    generator.generate_all_heatmaps()

if __name__ == "__main__":
    main()
```

```bash
chmod +x ~/redteam-lab3/scripts/threat_heatmap.py
```

### 🔧 Step 2.2: Create `threat_analysis.py`

```bash
nano ~/redteam-lab3/scripts/threat_analysis.py
```

```python
#!/usr/bin/env python3
"""
Threat Analysis and Statistics Generator
Students: Complete all TODO sections to produce threat metrics and visualizations
"""

import matplotlib
matplotlib.use('Agg')  # ⚠️ Required for non-display environments
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
from datetime import datetime

class ThreatAnalyzer:
    def __init__(self):
        self.output_dir = "../reports"
        self.assets_dir = "../assets"

    def generate_threat_statistics(self):
        """
        Generate comprehensive threat statistics and visualizations.

        TODO: Complete this function to:
        1. 📋 Create threat_data dictionary with columns:
           → Threat_Type, Frequency, Severity, Detection_Rate, Mitigation_Cost
        2. 📊 Create DataFrame from threat_data
        3. 🧮 Calculate risk score per threat:
           Formula: Frequency * Severity * (100 - Detection_Rate) / 100
        4. 🖼️  Create 2x2 subplot figure with 4 charts:
           → Chart 1: Bar chart — Top threats by risk score
           → Chart 2: Pie chart — Threat frequency distribution
           → Chart 3: Scatter plot — Detection rate vs severity
           → Chart 4: Bar chart — Mitigation costs
        5. 💾 Save figure to assets/threat_statistics_analysis.png
        6. 💾 Save JSON summary to reports/threat_statistics.json
        7. 📤 Return sorted DataFrame
        """

        # TODO: 📋 Populate threat_data with realistic values
        threat_data = {
            'Threat_Type':      [],
            'Frequency':        [],
            'Severity':         [],
            'Detection_Rate':   [],
            'Mitigation_Cost':  []
        }

        # TODO: 🐼 Create DataFrame
        df = pd.DataFrame(threat_data)

        # TODO: 🧮 Calculate risk score column
        # df['Risk_Score'] = df['Frequency'] * df['Severity'] * (100 - df['Detection_Rate']) / 100

        # TODO: 🖼️  Create 2x2 subplot (fig, axes = plt.subplots(2, 2, figsize=(14, 10)))

        # TODO: 📊 Chart 1 — Top threats bar chart (axes[0,0])

        # TODO: 🥧 Chart 2 — Frequency pie chart (axes[0,1])

        # TODO: 🔵 Chart 3 — Detection vs Severity scatter (axes[1,0])

        # TODO: 💰 Chart 4 — Mitigation cost bar chart (axes[1,1])

        # TODO: 💾 plt.tight_layout() + save to assets directory

        # TODO: 📄 Build stats_summary dict and write to JSON

        return df

def main():
    analyzer = ThreatAnalyzer()
    analyzer.generate_threat_statistics()

if __name__ == "__main__":
    main()
```

```bash
chmod +x ~/redteam-lab3/scripts/threat_analysis.py
```

### ▶️ Step 2.3: Test Your Scripts

```bash
cd ~/redteam-lab3/scripts
python3 threat_heatmap.py
python3 threat_analysis.py

# ✅ Verify all outputs exist
ls -la ~/redteam-lab3/assets/
ls -la ~/redteam-lab3/reports/
```

---

## 📋 Task 3 — Generate Final Red Team Report

### 📄 Step 3.1: Create Executive Final Report

```bash
nano ~/redteam-lab3/reports/final-report.md
```

```markdown
# Red Team Assessment Final Report
## Project CRIMSON HAWK

**Classification**: CONFIDENTIAL
**Report Date**: [Current Date]
**Engagement Period**: January 15 – February 12, 2024
**Red Team Lead**: [Your Name]
**Client**: Fictional Corp Industries

---

## Executive Summary

### Key Findings Summary
| Severity | Count |
|----------|-------|
| 🔴 Critical | 5 |
| 🟠 High | 12 |
| 🟡 Medium | 28 |
| 🟢 Low | 35 |

### Overall Security Posture: **MODERATE RISK**

### Primary Concerns
1. Inadequate email security — 35% phishing success rate
2. Weak network segmentation — lateral movement achieved in 48 hours
3. Insufficient privilege management — domain admin access obtained
4. Limited detection capabilities — 60% of activities went undetected
5. Outdated security policies — last updated 18 months ago

---

## Critical Findings

### 🔴 Finding 1: Unrestricted Domain Administrator Access
**Risk Level**: CRITICAL | **CVSS Score**: 9.8

**Description**: Domain administrator privileges obtained within 72 hours through
credential harvesting and privilege escalation.

**Technical Details**:
- Exploited unpatched vulnerability (CVE-2021-34527)
- Harvested credentials using Mimikatz
- Leveraged service account with excessive privileges

**Business Impact**: Complete network compromise, full data access,
ransomware deployment risk, data exfiltration exposure.

**Recommendations**:
- Implement principle of least privilege immediately
- Deploy Privileged Access Management (PAM) solution
- Establish credential rotation policy
- Patch all critical CVEs within 48 hours

---

### 🔴 Finding 2: Successful Phishing Campaign
**Risk Level**: CRITICAL | **CVSS Score**: 8.5

**Description**: Targeted phishing achieved 35% click rate and 15% credential
compromise among executive staff.

**Recommendations**:
- Implement MFA for all accounts immediately
- Deploy advanced email security (DMARC, SPF, DKIM)
- Conduct monthly security awareness training
- Run quarterly phishing simulations

---

### 🟠 Finding 3: Weak Network Segmentation
**Risk Level**: HIGH | **CVSS Score**: 7.8

**Description**: Insufficient segmentation enabled unrestricted lateral movement.

**Recommendations**:
- Implement network micro-segmentation
- Deploy next-generation firewalls
- Adopt zero-trust architecture principles

---

## Attack Path Analysis

| Path | Chain |
|------|-------|
| Path 1 | Phishing → Credential Theft → Lateral Movement → Domain Compromise |
| Path 2 | Web App Exploit → Privilege Escalation → Data Access |
| Path 3 | Physical Access → Network Connection → Internal Reconnaissance |

---

## Risk Assessment Matrix

| Risk Category | Likelihood | Impact | Score | Priority |
|---------------|------------|--------|-------|----------|
| Ransomware Attack | High | Critical | 20 | 🥇 1 |
| Data Breach | High | High | 16 | 🥈 2 |
| APT Campaign | Medium | Critical | 15 | 🥉 3 |
| Insider Threat | Medium | High | 12 | 4 |
| DDoS Attack | Medium | Medium | 9 | 5 |

---

## Remediation Roadmap

### ⚡ Immediate (0–30 days)
1. Deploy emergency patches for identified CVEs
2. Implement MFA for all administrative accounts
3. Deploy advanced email threat protection (DMARC, SPF, DKIM)

### 🔧 Short-term (30–90 days)
1. Develop security awareness training curriculum
2. Design and implement network micro-segmentation
3. Update and test incident response procedures

### 🏗️ Long-term (90+ days)
1. Develop and implement Zero Trust Architecture roadmap
2. Establish 24/7 SOC with SIEM platform
3. Schedule quarterly assessments and annual Red Team engagements

---

## Appendices

- **Appendix A**: Detailed Technical Findings
- **Appendix B**: Evidence and Screenshots
- **Appendix C**: Complete MITRE ATT&CK TTP Mapping
- **Appendix D**: Remediation Tracking Checklist
```

### 🔧 Step 3.2: Create Report Generator Script

```bash
nano ~/redteam-lab3/scripts/generate_report.sh
```

```bash
#!/bin/bash
# 📋 Red Team Report Generator

echo "=== 🔴 Red Team Report Generator ==="
echo "📦 Compiling full engagement report package..."

# 📁 Create report package directory
mkdir -p ~/redteam-lab3/report-package

# 📄 Copy all documents
cp ~/redteam-lab3/docs/*.md    ~/redteam-lab3/report-package/
cp ~/redteam-lab3/reports/*.md ~/redteam-lab3/report-package/

# 🖼️  Copy all visualizations
cp ~/redteam-lab3/assets/*.png ~/redteam-lab3/report-package/ 2>/dev/null

# 📋 Create package README
cat > ~/redteam-lab3/report-package/README.md << 'EOF'
# Red Team Assessment Report Package
## Project CRIMSON HAWK

## Contents
- operation-plan.md       → Complete Red Team operation plan
- threat-intelligence.md  → Threat landscape and adversary TTPs
- final-report.md         → Executive summary, findings, recommendations
- *.png                   → Threat heatmaps and statistical analysis charts

## Review Order
1. operation-plan.md
2. threat-intelligence.md
3. final-report.md
4. Visual assets (heatmaps, charts)
EOF

echo ""
echo "✅ Report package created at: ~/redteam-lab3/report-package/"
echo ""
ls -lh ~/redteam-lab3/report-package/
```

```bash
chmod +x ~/redteam-lab3/scripts/generate_report.sh
~/redteam-lab3/scripts/generate_report.sh
```

### 🔍 Step 3.3: Review and Validate

```bash
cd ~/redteam-lab3/report-package
ls -la
cat README.md
```

---

## ✅ Expected Lab Outputs

| Output File | Location | Description |
|-------------|----------|-------------|
| 📄 `operation-plan.md` | `docs/` | Full 4-week engagement plan |
| 📄 `threat-intelligence.md` | `docs/` | ATT&CK-mapped threat report |
| 🐍 `threat_heatmap.py` | `scripts/` | Network / timeline / vuln / risk heatmaps |
| 🐍 `threat_analysis.py` | `scripts/` | Statistical threat analysis charts |
| 📋 `final-report.md` | `reports/` | Executive findings & recommendations |
| 📊 `threat_statistics.json` | `reports/` | JSON statistics summary |
| 🖼️ `network_threat_heatmap.png` | `assets/` | Network segment threat levels |
| 🖼️ `attack_timeline_heatmap.png` | `assets/` | Activity intensity by phase/week |
| 🖼️ `vulnerability_severity_heatmap.png` | `assets/` | Vulnerabilities by system type |
| 🖼️ `risk_assessment_matrix.png` | `assets/` | Likelihood vs impact matrix |
| 🖼️ `threat_statistics_analysis.png` | `assets/` | 4-panel statistical dashboard |
| 📦 `report-package/` | `~/redteam-lab3/` | Compiled stakeholder-ready package |

---

## 🔧 Troubleshooting

| ❗ Issue | ✅ Solution |
|---------|-----------|
| pip install fails | Use `pip3 install --user matplotlib numpy pandas seaborn` or `sudo apt-get install python3-matplotlib python3-numpy python3-pandas python3-seaborn` |
| Matplotlib display error (`no $DISPLAY`) | Add `import matplotlib; matplotlib.use('Agg')` **before** `import matplotlib.pyplot as plt` in every script |
| Permission denied saving files | Run `chmod -R 755 ~/redteam-lab3` then `mkdir -p ~/redteam-lab3/{assets,reports}` |

---

## 💡 Key Takeaways

> 📋 **Structured Planning** — A detailed operation plan ensures comprehensive coverage, clear objectives, and defined rules of engagement before a single command is run
>
> 🌡️ **Visual Communication** — Heatmaps and charts transform raw data into insights that resonate with both technical operators and executive stakeholders
>
> 📄 **Professional Documentation** — Quality reporting is what separates a Red Team engagement from an unstructured attack — it creates accountability and drives remediation
>
> 🔀 **Version-Controlled Docs** — Markdown enables Red Team documentation to live alongside code in Git, making it auditable, diffable, and collaborative

---

## 🚀 Next Steps

After completing this lab, continue building your documentation skills:

- 🔗 Create operation plans for different scenarios — insider threat, cloud environment, OT/ICS
- 🔗 Automate report generation with Jinja2 templates for faster turnaround
- 🔗 Integrate heatmap generation into a CI/CD pipeline for continuous threat modeling
- 🔗 Build an interactive HTML dashboard version of the threat heatmaps

---

## 📚 References

- [MITRE ATT&CK Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/)
- [Red Team Development & Operations Guide](https://redteam.guide/)
- [CVSS Scoring System](https://www.first.org/cvss/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Heatmap Guide](https://seaborn.pydata.org/generated/seaborn.heatmap.html)

---

<div align="center">

**Built with ❤️ for the next generation of cybersecurity professionals**

*Al Nafi — Cloud-Based Cybersecurity Training Platform*

[![Al Nafi](https://img.shields.io/badge/Al_Nafi-Cybersecurity_Training-blueviolet?style=for-the-badge)](/)
[![Red Team](https://img.shields.io/badge/Domain-Red_Team_Operations-red?style=for-the-badge)](/)
[![ATT&CK](https://img.shields.io/badge/Framework-MITRE_ATT%26CK-orange?style=for-the-badge)](https://attack.mitre.org/)

</div>
