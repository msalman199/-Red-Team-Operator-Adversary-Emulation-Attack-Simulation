# 🔴 Gain Persistence with `schtasks`, Registry Run Keys & WMImplant

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-red?style=for-the-badge&logo=shield&logoColor=white)
![Lab Type](https://img.shields.io/badge/Lab%20Type-Red%20Team-darkred?style=for-the-badge&logo=target&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=for-the-badge&logo=buffer&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux%20%2F%20Windows%20Sim-blue?style=for-the-badge&logo=linux&logoColor=white)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE%20ATT%26CK-T1053%20%7C%20T1547%20%7C%20T1546-red?style=flat-square&logo=databricks&logoColor=white)
![Tactic](https://img.shields.io/badge/Tactic-Persistence-purple?style=flat-square&logo=gnubash&logoColor=white)
![License](https://img.shields.io/badge/License-Educational-green?style=flat-square&logo=bookstack&logoColor=white)

</div>

---

## 📋 Table of Contents

- [🎯 Objectives](#-objectives)
- [✅ Prerequisites](#-prerequisites)
- [🧪 Lab Environment](#-lab-environment)
- [📁 Directory Structure](#-directory-structure)
- [🗂️ Task 1 — Scheduled Task Persistence](#️-task-1--simulate-scheduled-task-persistence)
- [🗝️ Task 2 — Registry Run Key Persistence](#️-task-2--implement-registry-run-key-persistence)
- [👾 Task 3 — WMI-Based Persistence](#-task-3--deploy-wmi-based-persistence)
- [🚀 Task 4 — Automated Deployment](#-task-4--create-automated-persistence-deployment)
- [✔️ Expected Outcomes](#️-expected-outcomes)
- [🛠️ Troubleshooting](#️-troubleshooting)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

By the end of this lab, students will be able to:

- 🔍 Understand Windows persistence mechanisms used by adversaries
- 🗂️ Simulate **scheduled task** persistence using Python-based tools
- 🗝️ Implement **registry run key** persistence techniques
- 👾 Deploy **WMI-based** persistence mechanisms
- 🛡️ Analyze and detect persistence from a **defensive perspective**

---

## ✅ Prerequisites

| Requirement | Details |
|---|---|
| 🖥️ OS Knowledge | Basic understanding of Windows operating system |
| 💻 CLI Skills | Familiarity with command-line interfaces |
| 🐍 Python | Familiarity with Python programming |
| 📂 Registry | Understanding of Windows registry and scheduled tasks |

---

## 🧪 Lab Environment

> 💡 This lab uses a **Linux-based cloud machine** that simulates Windows persistence techniques through Python scripts. All tools are pre-installed.

Click **▶ Start Lab** to begin.

---

## 📁 Directory Structure

```
~/persistence_lab/
├── 🗂️  schtasks/
│   ├── schtasks_simulator.py
│   └── windows_sim/
│       ├── system32/tasks/
│       └── temp/persistence_payload.py
├── 🗝️  registry/
│   ├── registry_simulator.py
│   └── windows_registry/
│       ├── HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Windows/CurrentVersion/Run/
│       └── HKEY_CURRENT_USER/SOFTWARE/Microsoft/Windows/CurrentVersion/Run/
└── 👾  wmi/
    ├── wmi_persistence.py
    ├── deploy_persistence.py
    └── wmi_repository/root/subscription/
```

---

## 🗂️ Task 1 — Simulate Scheduled Task Persistence

> 🔎 **Overview:** Scheduled tasks allow adversaries to execute code at specific intervals or system events, providing reliable persistence.
> **MITRE ATT&CK:** [T1053.005 – Scheduled Task](https://attack.mitre.org/techniques/T1053/005/)

### Step 1 — Create Lab Directory Structure

```bash
mkdir -p ~/persistence_lab/{schtasks,registry,wmi}
cd ~/persistence_lab/schtasks
mkdir -p windows_sim/{system32/tasks,temp}
```

### Step 2 — Create Persistence Payload Template

```bash
cat > windows_sim/temp/persistence_payload.py << 'EOF'
#!/usr/bin/env python3
import datetime

def execute_persistence():
    '''
    Simulates persistence mechanism execution.
    TODO: Implement logging functionality
    TODO: Add timestamp recording
    TODO: Write to log file at /tmp/persistence_log.txt
    '''
    # TODO: Get current timestamp
    # TODO: Open log file in append mode
    # TODO: Write execution message with timestamp
    pass

if __name__ == "__main__":
    execute_persistence()
EOF

chmod +x windows_sim/temp/persistence_payload.py
```

### Step 3 — Create Scheduled Task Simulator

```bash
cat > schtasks_simulator.py << 'EOF'
#!/usr/bin/env python3
import json
import os
import sys
from datetime import datetime

class SchTasksSimulator:
    def __init__(self):
        self.tasks_file = "windows_sim/system32/tasks/scheduled_tasks.json"
        self.ensure_tasks_file()

    def ensure_tasks_file(self):
        '''
        TODO: Check if tasks file exists
        TODO: Create empty JSON file if not exists
        '''
        pass

    def create_task(self, task_name, command, schedule_type="DAILY"):
        '''
        Create a new scheduled task.
        Args:
            task_name: Name of the task
            command: Command to execute
            schedule_type: Schedule type (DAILY, ONLOGON, ONIDLE)
        TODO: Load existing tasks
        TODO: Create task configuration dictionary
        TODO: Save updated tasks
        TODO: Print success message
        '''
        pass

    def query_tasks(self, task_name=None):
        '''
        Query scheduled tasks.
        TODO: Load tasks from file
        TODO: Display task information in table format
        TODO: Handle specific task query if task_name provided
        '''
        pass

    def delete_task(self, task_name):
        '''
        TODO: Load tasks
        TODO: Remove specified task
        TODO: Save updated tasks
        '''
        pass

def main():
    '''
    TODO: Parse command line arguments
    TODO: Handle /CREATE, /QUERY, /DELETE actions
    TODO: Extract task parameters from arguments
    '''
    pass

if __name__ == "__main__":
    main()
EOF

chmod +x schtasks_simulator.py
```

### Step 4 — Deploy Scheduled Task Persistence

```bash
# 📅 Create daily update task
python3 schtasks_simulator.py /CREATE /TN "SystemUpdate" \
  /TR "python3 $(pwd)/windows_sim/temp/persistence_payload.py" /SC DAILY

# 🔐 Create logon-based task
python3 schtasks_simulator.py /CREATE /TN "WindowsDefender" \
  /TR "python3 $(pwd)/windows_sim/temp/persistence_payload.py" /SC ONLOGON

# 🔍 Query all tasks
python3 schtasks_simulator.py /QUERY
```

---

## 🗝️ Task 2 — Implement Registry Run Key Persistence

> 🔎 **Overview:** Registry Run keys execute programs automatically at system startup or user logon, providing stealthy persistence.
> **MITRE ATT&CK:** [T1547.001 – Registry Run Keys](https://attack.mitre.org/techniques/T1547/001/)

### Step 1 — Create Registry Simulation Environment

```bash
cd ~/persistence_lab/registry
mkdir -p windows_registry/HKEY_{LOCAL_MACHINE,CURRENT_USER}/SOFTWARE/Microsoft/Windows/CurrentVersion/{Run,RunOnce}
```

### Step 2 — Create Registry Manipulation Tool

```bash
cat > registry_simulator.py << 'EOF'
#!/usr/bin/env python3
import json
import os
import sys
from datetime import datetime

class RegistrySimulator:
    def __init__(self):
        self.registry_base = "windows_registry"
        self.hklm_run     = f"{self.registry_base}/HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Windows/CurrentVersion/Run/entries.json"
        self.hkcu_run     = f"{self.registry_base}/HKEY_CURRENT_USER/SOFTWARE/Microsoft/Windows/CurrentVersion/Run/entries.json"
        self.hklm_runonce = f"{self.registry_base}/HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Windows/CurrentVersion/RunOnce/entries.json"
        self.ensure_registry_files()

    def ensure_registry_files(self):
        '''
        TODO: Create registry file structure
        TODO: Initialize empty JSON files for each hive
        '''
        pass

    def add_entry(self, hive, key_path, value_name, value_data):
        '''
        Add registry entry for persistence.
        Args:
            hive: Registry hive (HKLM or HKCU)
            key_path: Path to registry key
            value_name: Name of the value
            value_data: Data/command to execute
        TODO: Determine correct registry file based on hive and path
        TODO: Load existing entries
        TODO: Add new entry with metadata
        TODO: Save updated entries
        '''
        pass

    def query_entries(self, hive, key_path):
        '''
        TODO: Load entries from appropriate registry file
        TODO: Display entries in Windows registry format
        '''
        pass

    def delete_entry(self, hive, key_path, value_name):
        '''
        TODO: Load entries
        TODO: Remove specified entry
        TODO: Save updated entries
        '''
        pass

def main():
    '''
    TODO: Parse command line arguments (ADD, DELETE, QUERY)
    TODO: Extract registry parameters
    TODO: Call appropriate simulator methods
    '''
    pass

if __name__ == "__main__":
    main()
EOF

chmod +x registry_simulator.py
```

### Step 3 — Deploy Registry Persistence

```bash
# 🏠 Add HKLM Run key entry (system-wide)
python3 registry_simulator.py ADD HKEY_LOCAL_MACHINE \
  "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" \
  /v "WindowsSecurityUpdate" \
  /d "python3 $(pwd)/../schtasks/windows_sim/temp/persistence_payload.py"

# 👤 Add HKCU Run key entry (current user)
python3 registry_simulator.py ADD HKEY_CURRENT_USER \
  "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" \
  /v "UserPreferences" \
  /d "python3 $(pwd)/../schtasks/windows_sim/temp/persistence_payload.py"

# 🔍 Query entries
python3 registry_simulator.py QUERY HKEY_LOCAL_MACHINE \
  "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
```

---

## 👾 Task 3 — Deploy WMI-Based Persistence

> 🔎 **Overview:** WMI event subscriptions provide sophisticated persistence through event filters and consumers that trigger on system events.
> **MITRE ATT&CK:** [T1546.003 – WMI Event Subscription](https://attack.mitre.org/techniques/T1546/003/)

### Step 1 — Create WMI Environment

```bash
cd ~/persistence_lab/wmi
mkdir -p wmi_repository/root/{subscription,cimv2}
```

### Step 2 — Create WMImplant Simulator

```bash
cat > wmi_persistence.py << 'EOF'
#!/usr/bin/env python3
import json
import os
import uuid
import sys
from datetime import datetime

class WMIImplantSimulator:
    def __init__(self):
        self.wmi_base          = "wmi_repository"
        self.subscription_path = f"{self.wmi_base}/root/subscription"
        self.consumers_file    = f"{self.subscription_path}/event_consumers.json"
        self.filters_file      = f"{self.subscription_path}/event_filters.json"
        self.bindings_file     = f"{self.subscription_path}/filter_bindings.json"
        self.ensure_wmi_files()

    def ensure_wmi_files(self):
        '''
        TODO: Create WMI repository structure
        TODO: Initialize JSON files for consumers, filters, bindings
        '''
        pass

    def create_event_filter(self, name, query):
        '''
        Create WMI event filter.
        Returns: filter_id (UUID)
        TODO: Generate unique filter ID
        TODO: Create filter configuration with query
        TODO: Save to filters file
        TODO: Return filter ID
        '''
        pass

    def create_command_line_consumer(self, name, command):
        '''
        Create command line event consumer.
        TODO: Generate unique consumer ID
        TODO: Create consumer configuration
        TODO: Save to consumers file
        TODO: Return consumer ID
        '''
        pass

    def create_filter_binding(self, filter_id, consumer_id):
        '''
        Bind event filter to consumer.
        TODO: Generate binding ID
        TODO: Create binding between filter and consumer
        TODO: Save binding
        '''
        pass

    def list_event_filters(self):
        ''' TODO: Load and display all event filters '''
        pass

    def list_consumers(self):
        ''' TODO: Load and display all event consumers '''
        pass

    def list_bindings(self):
        ''' TODO: Load and display filter-to-consumer bindings '''
        pass

def main():
    '''
    TODO: Parse command line arguments
    TODO: Handle create, list, remove commands
    TODO: Support logon, process, and timer persistence types
    '''
    pass

if __name__ == "__main__":
    main()
EOF

chmod +x wmi_persistence.py
```

### Step 3 — Deploy WMI Persistence Mechanisms

```bash
# 🔑 Create logon-based persistence
python3 wmi_persistence.py create logon "SystemMonitor" \
  "python3 $(pwd)/../schtasks/windows_sim/temp/persistence_payload.py"

# ⚙️ Create process-based persistence
python3 wmi_persistence.py create process "SecurityAgent" \
  "python3 $(pwd)/../schtasks/windows_sim/temp/persistence_payload.py"

# 📋 List all WMI components
python3 wmi_persistence.py list filters
python3 wmi_persistence.py list consumers
python3 wmi_persistence.py list bindings
```

---

## 🚀 Task 4 — Create Automated Persistence Deployment

### Step 1 — Create Comprehensive Deployment Script

```bash
cd ~/persistence_lab/wmi
cat > deploy_persistence.py << 'EOF'
#!/usr/bin/env python3
import os
import sys
import subprocess
import json
from datetime import datetime

class PersistenceDeployer:
    def __init__(self):
        self.base_dir       = os.getcwd()
        self.deployment_log = "persistence_deployment.json"

    def log_deployment(self, method, details):
        '''
        TODO: Create log entry with timestamp
        TODO: Append to deployment log file
        '''
        pass

    def deploy_schtasks_persistence(self):
        '''
        TODO: Define list of tasks to create
        TODO: Iterate and create each task
        TODO: Log successful deployments
        '''
        pass

    def deploy_registry_persistence(self):
        '''
        TODO: Define registry entries to create
        TODO: Create each registry entry
        TODO: Log deployments
        '''
        pass

    def deploy_wmi_persistence(self):
        '''
        TODO: Create event filters
        TODO: Create event consumers
        TODO: Bind filters to consumers
        TODO: Log deployments
        '''
        pass

    def deploy_all(self):
        '''
        TODO: Call all deployment methods
        TODO: Generate summary report
        '''
        pass

    def generate_report(self):
        '''
        TODO: Load deployment log
        TODO: Display summary of deployed persistence mechanisms
        '''
        pass

def main():
    '''
    TODO: Parse command line arguments
    TODO: Support deploy-all, deploy-schtasks, deploy-registry, deploy-wmi
    TODO: Support report generation
    '''
    pass

if __name__ == "__main__":
    main()
EOF

chmod +x deploy_persistence.py
```

### Step 2 — Deploy All Persistence Mechanisms

```bash
# 🚀 Deploy all persistence methods
python3 deploy_persistence.py deploy-all

# 📊 Generate deployment report
python3 deploy_persistence.py report
```

### Step 3 — Verify Persistence Deployment

```bash
# ✅ Check scheduled tasks
cd ~/persistence_lab/schtasks
python3 schtasks_simulator.py /QUERY

# ✅ Check registry entries
cd ~/persistence_lab/registry
python3 registry_simulator.py QUERY HKEY_LOCAL_MACHINE \
  "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"

# ✅ Check WMI bindings
cd ~/persistence_lab/wmi
python3 wmi_persistence.py list bindings
```

---

## ✔️ Expected Outcomes

After completing this lab, you should have:

| # | Deliverable | Status |
|---|---|---|
| 1 | 🗂️ Functional scheduled task persistence simulator with multiple tasks | ✅ |
| 2 | 🗝️ Registry run key entries in **HKLM** and **HKCU** hives | ✅ |
| 3 | 👾 WMI event subscription persistence with filters, consumers & bindings | ✅ |
| 4 | 🚀 Automated deployment script for all persistence methods | ✅ |
| 5 | 📋 Deployment logs tracking all persistence mechanisms | ✅ |

---

## 🛠️ Troubleshooting

<details>
<summary>❌ Scripts fail with "file not found" errors</summary>

**Cause:** Wrong working directory.

**Fix:** Ensure you're in the correct directory for each task.

```bash
pwd   # Verify current location
cd ~/persistence_lab/schtasks   # Navigate if needed
```

</details>

<details>
<summary>❌ JSON files become corrupted</summary>

**Cause:** Incomplete write operations or malformed data.

**Fix:** Delete the JSON files and re-run the initialization methods.

```bash
rm windows_sim/system32/tasks/scheduled_tasks.json
python3 schtasks_simulator.py /QUERY   # Triggers file re-creation
```

</details>

<details>
<summary>❌ Persistence payload doesn't execute</summary>

**Cause:** Relative path used or missing execute permissions.

**Fix:** Verify the payload path is **absolute** and the script is executable.

```bash
chmod +x windows_sim/temp/persistence_payload.py
realpath windows_sim/temp/persistence_payload.py   # Get absolute path
```

</details>

---

## 🏁 Conclusion

This lab demonstrated **three primary Windows persistence mechanisms**:

```
┌─────────────────────────────────────────────────────┐
│  🗂️  Scheduled Tasks   →  schtasks / Task Scheduler  │
│  🗝️  Registry Run Keys  →  HKLM & HKCU Run entries   │
│  👾  WMI Subscriptions  →  Filters + Consumers       │
└─────────────────────────────────────────────────────┘
```

You created Python-based simulators to understand how adversaries establish persistence and built an **automated deployment framework**. These techniques map to **MITRE ATT&CK TA0003 (Persistence)** and are commonly observed in real-world intrusions.

> 🛡️ **Defender Takeaway:** Security teams must monitor these locations using **EDR tools**, **SIEM alerts**, and **regular audits** to detect unauthorized persistence mechanisms.

---

<div align="center">

---

🔐 **Al Nafi Cybersecurity Training Platform**

*Empowering the Next Generation of Cyber Defenders*

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Red%20Team%20Operations-red?style=for-the-badge&logo=shield&logoColor=white)
![MITRE](https://img.shields.io/badge/MITRE%20ATT%26CK-TA0003%20Persistence-darkred?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-Simulation-0078D6?style=flat-square&logo=windows&logoColor=white)
![WMI](https://img.shields.io/badge/WMI-Event%20Subscription-8B0000?style=flat-square&logo=microsoft&logoColor=white)
![Registry](https://img.shields.io/badge/Registry-Run%20Keys-purple?style=flat-square&logo=microsoft&logoColor=white)

*© Al Nafi — For educational and authorized lab use only.*

</div>
