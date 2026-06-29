<div align="center">

# 🕵️ Simulate OSINT Collection Using SpiderFoot & recon-ng

<img src="https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Lab-blue?style=for-the-badge&logo=shield&logoColor=white"/>
<img src="https://img.shields.io/badge/Difficulty-Intermediate-orange?style=for-the-badge&logo=target&logoColor=white"/>
<img src="https://img.shields.io/badge/Lab%20Type-Hands--On-green?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/Domain-OSINT%20%26%20Recon-red?style=for-the-badge&logo=searchengin&logoColor=white"/>

---

[![SpiderFoot](https://img.shields.io/badge/SpiderFoot-OSINT%20Framework-1a1a2e?style=flat-square&logo=spiderfoot&logoColor=white)](https://github.com/smicallef/spiderfoot)
[![recon-ng](https://img.shields.io/badge/recon--ng-Recon%20Framework-4a4a8a?style=flat-square&logo=gnubash&logoColor=white)](https://github.com/lanmaster53/recon-ng)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04%20LTS-E95420?style=flat-square&logo=ubuntu&logoColor=white)](https://ubuntu.com)
[![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=flat-square&logo=git&logoColor=white)](https://git-scm.com)
[![Bash](https://img.shields.io/badge/Bash-Scripting-4EAA25?style=flat-square&logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)
[![JSON](https://img.shields.io/badge/JSON-Data%20Format-000000?style=flat-square&logo=json&logoColor=white)](https://json.org)
[![nmap](https://img.shields.io/badge/nmap-Port%20Scanner-0E83CD?style=flat-square&logo=nmap&logoColor=white)](https://nmap.org)

</div>

---

## 📋 Table of Contents

- [🎯 Objectives](#-objectives)
- [✅ Prerequisites](#-prerequisites)
- [🖥️ Lab Environment](#️-lab-environment)
- [🔧 Task 1 — Install & Configure OSINT Tools](#-task-1--install--configure-osint-tools)
- [🔍 Task 2 — Execute Basic OSINT Scans](#-task-2--execute-basic-osint-scans)
- [🤖 Task 3 — Automate OSINT Data Aggregation](#-task-3--automate-osint-data-aggregation)
- [📊 Task 4 — Analyze & Visualize Results](#-task-4--analyze--visualize-results)
- [✅ Expected Outcomes](#-expected-outcomes)
- [🛠️ Troubleshooting Tips](#️-troubleshooting-tips)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

> By the end of this lab, students will be able to:

| # | Objective |
|---|-----------|
| 1️⃣ | Install and configure **SpiderFoot** and **recon-ng** for automated OSINT gathering |
| 2️⃣ | Execute reconnaissance scans using both frameworks |
| 3️⃣ | Develop **Python scripts** to automate OSINT data collection |
| 4️⃣ | Aggregate and analyze intelligence from **multiple sources** |
| 5️⃣ | Generate **comprehensive reports** from collected data |

---

## ✅ Prerequisites

> Ensure you have the following knowledge before starting:

| Skill | Level |
|-------|-------|
| 🐧 Linux Command Line | Basic |
| 🌐 DNS, Domains & IP Addressing | Understanding |
| 🐍 Python Programming | Fundamentals |
| 📄 JSON & CSV Formats | Familiar |
| 🔐 Cybersecurity & OSINT Concepts | Basic |

---

## 🖥️ Lab Environment

<div align="center">

[![Al Nafi Cloud](https://img.shields.io/badge/Platform-Al%20Nafi%20Cloud%20Lab-blue?style=for-the-badge&logo=cloud&logoColor=white)]()
[![Ubuntu](https://img.shields.io/badge/OS-Ubuntu%2022.04%20LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)]()
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Git](https://img.shields.io/badge/Tools-Git%20%26%20Dev%20Tools-F05032?style=for-the-badge&logo=git&logoColor=white)]()

</div>

Al Nafi provides **pre-configured Linux cloud machines**. Click **▶️ Start Lab** to access your environment with:

- ✅ Ubuntu 22.04 LTS
- ✅ Python 3.10+
- ✅ Git and development tools
- ✅ Network utilities pre-installed

---

## 🔧 Task 1 — Install & Configure OSINT Tools

---

### 🕸️ Step 1.1 — Install SpiderFoot

[![SpiderFoot](https://img.shields.io/badge/SpiderFoot-Install-1a1a2e?style=flat-square&logo=github&logoColor=white)]()
[![pip](https://img.shields.io/badge/pip-Python%20Package%20Manager-3776AB?style=flat-square&logo=pypi&logoColor=white)]()

```bash
# 📦 Update system and install dependencies
sudo apt update && sudo apt install -y python3 python3-pip git

# 📥 Clone SpiderFoot repository
cd /opt
sudo git clone https://github.com/smicallef/spiderfoot.git
sudo chown -R $USER:$USER /opt/spiderfoot

# 🔧 Install Python dependencies
cd /opt/spiderfoot
pip3 install -r requirements.txt
```

---

### 🔭 Step 1.2 — Install recon-ng

[![recon-ng](https://img.shields.io/badge/recon--ng-Install-4a4a8a?style=flat-square&logo=github&logoColor=white)]()
[![pip](https://img.shields.io/badge/pip-Dependencies-3776AB?style=flat-square&logo=pypi&logoColor=white)]()

```bash
# 📥 Clone recon-ng repository
cd /opt
sudo git clone https://github.com/lanmaster53/recon-ng.git
sudo chown -R $USER:$USER /opt/recon-ng

# 🔧 Install dependencies
cd /opt/recon-ng
pip3 install -r REQUIREMENTS

# 🔗 Create symbolic link
sudo ln -sf /opt/recon-ng/recon-ng /usr/local/bin/recon-ng
```

---

### ✔️ Step 1.3 — Verify Installations

[![Verification](https://img.shields.io/badge/Status-Verify%20Tools-brightgreen?style=flat-square&logo=checkmarx&logoColor=white)]()

```bash
# ✅ Test SpiderFoot
cd /opt/spiderfoot
python3 sf.py --help

# ✅ Test recon-ng
cd /opt/recon-ng
python3 recon-ng --help
```

---

## 🔍 Task 2 — Execute Basic OSINT Scans

---

### 🕸️ Step 2.1 — Run SpiderFoot Command-Line Scan

[![SpiderFoot](https://img.shields.io/badge/SpiderFoot-CLI%20Scan-1a1a2e?style=flat-square&logo=searchengin&logoColor=white)]()
[![Python](https://img.shields.io/badge/Python-Script-3776AB?style=flat-square&logo=python&logoColor=white)]()
[![subprocess](https://img.shields.io/badge/subprocess-Module-yellow?style=flat-square&logo=python&logoColor=white)]()

Create a basic SpiderFoot scan script:

```python
#!/usr/bin/env python3
# 📄 File: spiderfoot_scan.py

import subprocess  # 🔧 For running system commands
import sys         # 🔧 For command-line arguments
import json        # 📊 For parsing JSON output
from datetime import datetime  # 🕒 For timestamps

def run_spiderfoot_scan(target, output_file):
    """
    🕸️ Execute SpiderFoot scan on target domain.
    
    Args:
        target: Domain name to scan
        output_file: Path to save results
    
    Returns:
        Scan results dictionary
    """
    # TODO: 🛠️ Build SpiderFoot command with parameters
    # TODO: ⚙️ Execute subprocess with proper error handling
    # TODO: 📤 Parse and return results
    pass

def parse_scan_results(output_file):
    """
    📊 Parse SpiderFoot JSON output.
    
    Args:
        output_file: Path to results file
    
    Returns:
        Parsed data dictionary
    """
    # TODO: 📂 Load JSON file
    # TODO: 🔍 Extract key findings (domains, IPs, emails)
    # TODO: 📦 Return structured data
    pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("⚠️  Usage: python3 spiderfoot_scan.py <target_domain>")
        sys.exit(1)
    
    target = sys.argv[1]
    # TODO: 🚀 Call run_spiderfoot_scan()
    # TODO: 📋 Parse and display results
```

> 💡 **Manual Execution Example:**

```bash
# 🔍 Run SpiderFoot with specific modules
cd /opt/spiderfoot
python3 sf.py -s example.com -t INTERNET_NAME \
  -m sfp_dnsresolve,sfp_whois,sfp_dns_common \
  -o json -F results.json -q
```

---

### 🔭 Step 2.2 — Execute recon-ng Reconnaissance

[![recon-ng](https://img.shields.io/badge/recon--ng-Automation-4a4a8a?style=flat-square&logo=gnubash&logoColor=white)]()
[![Python](https://img.shields.io/badge/Python-OOP%20Class-3776AB?style=flat-square&logo=python&logoColor=white)]()

Create recon-ng automation script:

```python
#!/usr/bin/env python3
# 📄 File: recon_scan.py

import subprocess  # 🔧 For running recon-ng
import os          # 📂 For file operations
import sys         # 🔧 For system interactions

class ReconNGScanner:
    def __init__(self, workspace_name):
        """
        🔭 Initialize recon-ng scanner.
        
        Args:
            workspace_name: Name for recon-ng workspace
        """
        self.workspace = workspace_name
        self.recon_path = "/opt/recon-ng"  # 📂 Tool path
    
    def create_command_file(self, target):
        """
        📝 Generate recon-ng command file.
        
        Args:
            target: Domain to investigate
        
        Returns:
            Path to command file
        """
        # TODO: 📄 Create temporary command file
        # TODO: 🏗️ Add workspace creation commands
        # TODO: 📦 Add module installation commands
        # TODO: 🔍 Add reconnaissance commands
        # TODO: 📤 Return file path
        pass
    
    def execute_scan(self, command_file):
        """
        ▶️ Execute recon-ng with command file.
        
        Args:
            command_file: Path to commands
        
        Returns:
            Scan output
        """
        # TODO: 🚀 Run recon-ng subprocess
        # TODO: 📋 Capture output
        # TODO: 🧹 Clean up command file
        # TODO: 📤 Return results
        pass
    
    def parse_results(self, output):
        """
        🔎 Extract intelligence from recon-ng output.
        
        Args:
            output: Raw scan output
        
        Returns:
            Dictionary with domains, hosts, contacts
        """
        # TODO: 🌐 Parse domains from output
        # TODO: 🖥️ Parse hosts and IPs
        # TODO: 📧 Parse contact information
        # TODO: 📦 Return structured data
        pass

if __name__ == "__main__":
    # TODO: 🏗️ Initialize scanner
    # TODO: 🚀 Run scan on target
    # TODO: 📊 Display results
    pass
```

> 💡 **Manual recon-ng Workflow:**

```bash
# 🚀 Start recon-ng
cd /opt/recon-ng
python3 recon-ng

# 📋 In recon-ng console:
# workspaces create osint_lab
# marketplace install recon/domains-hosts/hackertarget
# db insert domains example.com
# modules load recon/domains-hosts/hackertarget
# run
# show hosts
```

---

### 🔄 Step 2.3 — Compare Tool Outputs

[![Comparison](https://img.shields.io/badge/Analysis-Tool%20Comparison-purple?style=flat-square&logo=chartdotjs&logoColor=white)]()
[![Python](https://img.shields.io/badge/Python-Data%20Analysis-3776AB?style=flat-square&logo=python&logoColor=white)]()

```python
#!/usr/bin/env python3
# 📄 File: compare_results.py

import json  # 📊 For JSON parsing

def load_spiderfoot_data(file_path):
    """🕸️ Load and parse SpiderFoot results."""
    # TODO: 📂 Load JSON file
    # TODO: 🔍 Extract relevant fields
    pass

def load_recon_data(file_path):
    """🔭 Load and parse recon-ng results."""
    # TODO: 📂 Load data file
    # TODO: 🔎 Parse structured output
    pass

def compare_findings(sf_data, recon_data):
    """
    🔄 Compare findings from both tools.
    
    Returns:
        Dictionary with unique and common findings
    """
    # TODO: 🔍 Identify common domains/IPs
    # TODO: 🎯 Identify unique findings per tool
    # TODO: 📊 Calculate overlap percentage
    pass

if __name__ == "__main__":
    # TODO: 📂 Load both datasets
    # TODO: 🔄 Compare and analyze
    # TODO: 📝 Generate comparison report
    pass
```

---

## 🤖 Task 3 — Automate OSINT Data Aggregation

---

### 🏗️ Step 3.1 — Build OSINT Aggregation Framework

[![Framework](https://img.shields.io/badge/Framework-OSINT%20Aggregator-darkblue?style=flat-square&logo=python&logoColor=white)]()
[![DNS](https://img.shields.io/badge/Tools-DNS%20%7C%20WHOIS%20%7C%20nmap-0E83CD?style=flat-square&logo=cloudflare&logoColor=white)]()
[![JSON](https://img.shields.io/badge/Output-JSON%20%7C%20CSV%20%7C%20HTML-000000?style=flat-square&logo=json&logoColor=white)]()

```python
#!/usr/bin/env python3
# 📄 File: osint_aggregator.py

import json               # 📊 For data serialization
import subprocess         # 🔧 For system tool execution
import os                 # 📂 For file system operations
from datetime import datetime  # 🕒 For timestamping
from pathlib import Path  # 📂 For path management

class OSINTAggregator:
    def __init__(self, target, output_dir="osint_results"):
        """
        🏗️ Initialize OSINT aggregation framework.
        
        Args:
            target: Target domain
            output_dir: Directory for results
        """
        self.target = target                                          # 🎯 Target domain
        self.output_dir = output_dir                                  # 📂 Output directory
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")    # 🕒 Run timestamp
        self.results = {}                                             # 📦 Results store
        Path(output_dir).mkdir(exist_ok=True)                        # 📂 Create directory
    
    def collect_dns_records(self):
        """
        🌐 Collect DNS records using dig.
        
        Returns:
            Dictionary of DNS records by type
        """
        # TODO: 🔍 Query A, AAAA, MX, NS, TXT records
        # TODO: 📋 Parse dig output
        # TODO: 📦 Return structured data
        pass
    
    def collect_whois_data(self):
        """
        📋 Collect WHOIS information.
        
        Returns:
            Dictionary with registrar, dates, contacts
        """
        # TODO: 🚀 Execute whois command
        # TODO: 🏢 Parse registrar information
        # TODO: 📅 Extract creation/expiration dates
        # TODO: 📦 Return structured data
        pass
    
    def enumerate_subdomains(self):
        """
        🔍 Perform basic subdomain enumeration.
        
        Returns:
            List of discovered subdomains
        """
        common_subs = ['www', 'mail', 'ftp', 'admin', 'api', 'dev']  # 🎯 Common prefixes
        # TODO: 🧪 Test each subdomain with nslookup
        # TODO: ✅ Collect valid subdomains
        # TODO: 📤 Return list
        pass
    
    def run_port_scan(self):
        """
        🔌 Execute basic port scan with nmap.
        
        Returns:
            Dictionary with open ports and services
        """
        # TODO: 🌐 Resolve target to IP
        # TODO: 🚀 Run nmap scan
        # TODO: 🔓 Parse open ports
        # TODO: 📦 Return results
        pass
    
    def aggregate_all_sources(self):
        """
        🔗 Aggregate data from all collection methods.
        
        Returns:
            Comprehensive intelligence report
        """
        # TODO: 📡 Collect from all sources
        # TODO: 🔄 Merge and deduplicate data
        # TODO: 📊 Generate summary statistics
        # TODO: 📤 Return aggregated report
        pass
    
    def export_report(self, format='json'):
        """
        📤 Export aggregated report.
        
        Args:
            format: Output format (json, csv, html)
        """
        # TODO: 🎨 Format data for export
        # TODO: 💾 Write to file
        # TODO: 📋 Generate summary
        pass

if __name__ == "__main__":
    # TODO: 🏗️ Initialize aggregator
    # TODO: 🚀 Run all collection methods
    # TODO: 📤 Export comprehensive report
    pass
```

---

### 🔗 Step 3.2 — Create Intelligence Correlation Module

[![Correlation](https://img.shields.io/badge/Module-Intelligence%20Correlator-8B0000?style=flat-square&logo=python&logoColor=white)]()
[![Risk](https://img.shields.io/badge/Feature-Risk%20Scoring-FF6347?style=flat-square&logo=shield&logoColor=white)]()

```python
#!/usr/bin/env python3
# 📄 File: correlate_intelligence.py

class IntelligenceCorrelator:
    def __init__(self, aggregated_data):
        """
        🔗 Initialize intelligence correlator.
        
        Args:
            aggregated_data: Dictionary from OSINTAggregator
        """
        self.data = aggregated_data   # 📦 Input intelligence
        self.correlations = {}        # 🔗 Correlation results
    
    def correlate_domains_ips(self):
        """
        🌐 Correlate domains with IP addresses.
        
        Returns:
            Dictionary mapping domains to IPs
        """
        # TODO: 🔍 Extract domain-IP relationships
        # TODO: 🖥️ Identify shared hosting
        # TODO: 🗺️ Return correlation map
        pass
    
    def identify_technologies(self):
        """
        🛠️ Identify technologies from collected data.
        
        Returns:
            List of detected technologies
        """
        # TODO: 📡 Analyze HTTP headers
        # TODO: 🌐 Check DNS records for clues
        # TODO: 🖥️ Identify web servers, frameworks
        pass
    
    def calculate_risk_score(self):
        """
        ⚠️ Calculate basic risk score based on findings.
        
        Returns:
            Risk score and contributing factors
        """
        # TODO: 🔓 Check for exposed services
        # TODO: 🛡️ Evaluate DNS security
        # TODO: 📊 Calculate composite score
        pass
    
    def generate_intelligence_report(self):
        """
        📝 Generate comprehensive intelligence report.
        
        Returns:
            Formatted report dictionary
        """
        # TODO: 🔗 Compile all correlations
        # TODO: ⚠️ Add risk assessment
        # TODO: 💡 Include recommendations
        pass

if __name__ == "__main__":
    # TODO: 📂 Load aggregated data
    # TODO: 🔍 Run correlation analysis
    # TODO: 📤 Generate and save report
    pass
```

---

### 📄 Step 3.3 — Build Report Generator

[![Report](https://img.shields.io/badge/Output-HTML%20%7C%20JSON%20%7C%20CSV-28a745?style=flat-square&logo=html5&logoColor=white)]()
[![HTML](https://img.shields.io/badge/HTML5-Report%20Template-E34F26?style=flat-square&logo=html5&logoColor=white)]()
[![CSV](https://img.shields.io/badge/CSV-Data%20Export-217346?style=flat-square&logo=microsoftexcel&logoColor=white)]()

```python
#!/usr/bin/env python3
# 📄 File: report_generator.py

import json                        # 📊 For JSON output
from datetime import datetime      # 🕒 For timestamps

class OSINTReportGenerator:
    def __init__(self, intelligence_data):
        """
        📝 Initialize report generator.
        
        Args:
            intelligence_data: Correlated intelligence
        """
        self.data = intelligence_data     # 📦 Intelligence input
        self.timestamp = datetime.now()   # 🕒 Report timestamp
    
    def generate_executive_summary(self):
        """
        📋 Create executive summary section.
        
        Returns:
            Summary text
        """
        # TODO: 🔍 Summarize key findings
        # TODO: ⚠️ Highlight critical issues
        # TODO: 📝 Return formatted summary
        pass
    
    def generate_technical_details(self):
        """
        🔧 Create detailed technical section.
        
        Returns:
            Technical details dictionary
        """
        # TODO: 🗂️ List all discovered assets
        # TODO: 🛠️ Document technologies
        # TODO: 📎 Include raw data references
        pass
    
    def generate_html_report(self, output_file):
        """
        🌐 Generate HTML report.
        
        Args:
            output_file: Path for HTML output
        """
        # TODO: 🏗️ Create HTML structure
        # TODO: 🎨 Add CSS styling
        # TODO: 📊 Include charts/tables
        # TODO: 💾 Write to file
        pass
    
    def generate_json_report(self, output_file):
        """
        📊 Generate JSON report.
        
        Args:
            output_file: Path for JSON output
        """
        # TODO: 🗂️ Structure data for JSON
        # TODO: 🏷️ Add metadata
        # TODO: 💾 Write to file
        pass
    
    def generate_csv_export(self, output_file):
        """
        📋 Generate CSV export of findings.
        
        Args:
            output_file: Path for CSV output
        """
        # TODO: 📐 Flatten data structure
        # TODO: 🗃️ Create CSV rows
        # TODO: 💾 Write to file
        pass

if __name__ == "__main__":
    # TODO: 📂 Load intelligence data
    # TODO: 📝 Generate all report formats
    # TODO: 💾 Save to output directory
    pass
```

---

## 📊 Task 4 — Analyze & Visualize Results

---

### 🔬 Step 4.1 — Create Analysis Script

[![Analysis](https://img.shields.io/badge/Module-OSINT%20Analyzer-6A0DAD?style=flat-square&logo=python&logoColor=white)]()
[![Statistics](https://img.shields.io/badge/Python-statistics%20module-3776AB?style=flat-square&logo=python&logoColor=white)]()

```python
#!/usr/bin/env python3
# 📄 File: analyze_osint.py

import json        # 📊 For loading report data
import statistics  # 📐 For statistical analysis

class OSINTAnalyzer:
    def __init__(self, report_file):
        """🔬 Load OSINT report for analysis."""
        # TODO: 📂 Load report data
        pass
    
    def analyze_attack_surface(self):
        """
        🎯 Analyze exposed attack surface.
        
        Returns:
            Dictionary with surface metrics
        """
        # TODO: 🔓 Count exposed services
        # TODO: 🌐 Identify public-facing assets
        # TODO: 📊 Calculate exposure score
        pass
    
    def identify_patterns(self):
        """
        🔍 Identify patterns in collected data.
        
        Returns:
            List of identified patterns
        """
        # TODO: 🏷️ Analyze naming conventions
        # TODO: 🏗️ Identify infrastructure patterns
        # TODO: ⚠️ Detect anomalies
        pass
    
    def generate_recommendations(self):
        """
        💡 Generate security recommendations.
        
        Returns:
            List of actionable recommendations
        """
        # TODO: 🛡️ Based on findings, suggest improvements
        # TODO: ⚠️ Prioritize by risk level
        # TODO: 📋 Return recommendation list
        pass

if __name__ == "__main__":
    # TODO: 📂 Load report
    # TODO: 🔬 Run analysis
    # TODO: 💡 Display recommendations
    pass
```

---

### ⚡ Step 4.2 — Execute Complete OSINT Workflow

[![Bash](https://img.shields.io/badge/Bash-Master%20Workflow-4EAA25?style=flat-square&logo=gnubash&logoColor=white)]()
[![Automation](https://img.shields.io/badge/Script-Full%20Pipeline-orange?style=flat-square&logo=autohotkey&logoColor=white)]()

```bash
#!/bin/bash
# 📄 File: osint_workflow.sh

TARGET=$1  # 🎯 Target domain from argument
OUTPUT_DIR="osint_output_$(date +%Y%m%d_%H%M%S)"  # 📂 Timestamped output dir

if [ -z "$TARGET" ]; then
    echo "⚠️  Usage: ./osint_workflow.sh <target_domain>"
    exit 1
fi

echo "🚀 Starting OSINT workflow for: $TARGET"
mkdir -p $OUTPUT_DIR  # 📂 Create output directory

# TODO: 🕸️ Run SpiderFoot scan
# TODO: 🔭 Run recon-ng scan
# TODO: 🤖 Execute aggregation script
# TODO: 🔗 Run correlation analysis
# TODO: 📄 Generate reports
# TODO: 🔬 Perform analysis
# TODO: 📊 Display summary

echo "✅ OSINT workflow completed. Results in: $OUTPUT_DIR"
```

---

## ✅ Expected Outcomes

> After completing this lab, you should have:

| # | Outcome |
|---|---------|
| ✅ | Functional **SpiderFoot** and **recon-ng** installations |
| ✅ | Working **Python scripts** for automated OSINT collection |
| ✅ | Aggregated intelligence from **multiple sources** |
| ✅ | Comprehensive reports in **JSON, CSV, and HTML** formats |
| ✅ | Understanding of **OSINT correlation techniques** |
| ✅ | Practical experience with **reconnaissance automation** |

---

## 🛠️ Troubleshooting Tips

<details>
<summary>🕸️ SpiderFoot Issues</summary>

| Problem | Solution |
|---------|----------|
| ❌ Modules fail | Check API keys in configuration |
| ❌ Dependencies missing | Run `pip3 install -r requirements.txt` again |
| ❌ Network errors | Verify internet connectivity for external queries |

</details>

<details>
<summary>🔭 recon-ng Problems</summary>

| Problem | Solution |
|---------|----------|
| ❌ Modules won't install | Run `marketplace refresh` first |
| ❌ Permission errors | Check workspace in `~/.recon-ng` |
| ❌ Module incompatibility | Verify version with current release |

</details>

<details>
<summary>🐍 Script Errors</summary>

| Problem | Solution |
|---------|----------|
| ❌ Path errors | Ensure paths point to correct tool installations |
| ❌ Version issues | Verify Python 3.8+ is active |
| ❌ Command failures | Test subprocess commands manually first |

</details>

<details>
<summary>🌐 Network Issues</summary>

| Problem | Solution |
|---------|----------|
| ❌ Rate limiting | Add delays between requests |
| ❌ Blocked queries | Consider using a VPN |
| ❌ Slow scans | Limit module scope per scan session |

</details>

---

## 🏁 Conclusion

This lab provided hands-on experience with professional OSINT tools and automation techniques. You learned to install and configure **SpiderFoot** and **recon-ng**, execute reconnaissance scans, aggregate data from multiple sources, and generate comprehensive intelligence reports.

### 🔑 Key Takeaways

| # | Takeaway |
|---|----------|
| 💡 | OSINT collection requires **multiple tools and sources** |
| 💡 | **Automation** improves efficiency and consistency |
| 💡 | **Data correlation** reveals deeper insights |
| 💡 | Proper **documentation and reporting** are critical |
| ⚖️ | Always respect **legal and ethical boundaries** |

### ➡️ Next Steps

- 🔌 Explore additional **SpiderFoot** and **recon-ng** modules
- 🔗 Integrate additional OSINT sources (**Shodan**, **VirusTotal**)
- 🛠️ Develop **custom modules** for specific intelligence needs
- 🎯 Practice on **authorized targets only**
- 📚 Study OSINT frameworks like **MITRE ATT&CK**

---

<div align="center">

[![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cloud%20Learning%20Platform-blue?style=for-the-badge&logo=cloud&logoColor=white)](https://alnafi.com)
[![OSINT](https://img.shields.io/badge/Domain-OSINT%20%26%20Reconnaissance-red?style=for-the-badge&logo=searchengin&logoColor=white)]()
[![License](https://img.shields.io/badge/Use-Authorized%20Targets%20Only-critical?style=for-the-badge&logo=shield&logoColor=white)]()

**Built with ❤️ for the next generation of cybersecurity professionals**

*© Al Nafi — Cybersecurity Training Program*

</div>
