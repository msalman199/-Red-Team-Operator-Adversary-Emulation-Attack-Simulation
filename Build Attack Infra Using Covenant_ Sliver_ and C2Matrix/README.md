<div align="center">

# ⚔️ Build Attack Infrastructure Using Covenant, Sliver & C2Matrix

<img src="https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Lab-blue?style=for-the-badge&logo=shield&logoColor=white"/>
<img src="https://img.shields.io/badge/Difficulty-Advanced-red?style=for-the-badge&logo=target&logoColor=white"/>
<img src="https://img.shields.io/badge/Lab%20Type-Hands--On-green?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/Domain-Red%20Team%20Operations-darkred?style=for-the-badge&logo=hackthebox&logoColor=white"/>

---

[![Covenant](https://img.shields.io/badge/Covenant-C2%20Framework-1a1a2e?style=flat-square&logo=dotnet&logoColor=white)](https://github.com/cobbr/Covenant)
[![Sliver](https://img.shields.io/badge/Sliver-Stealth%20C2-4a4a8a?style=flat-square&logo=go&logoColor=white)](https://github.com/BishopFox/sliver)
[![C2Matrix](https://img.shields.io/badge/C2Matrix-Infrastructure%20Manager-FF6B35?style=flat-square&logo=django&logoColor=white)](https://github.com/Coalfire-Research/C2Matrix)
[![.NET](https://img.shields.io/badge/.NET%20SDK-6.0-512BD4?style=flat-square&logo=dotnet&logoColor=white)](https://dotnet.microsoft.com)
[![Go](https://img.shields.io/badge/Go-Runtime-00ADD8?style=flat-square&logo=go&logoColor=white)](https://go.dev)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-Web%20Framework-092E20?style=flat-square&logo=django&logoColor=white)](https://djangoproject.com)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04%20LTS-E95420?style=flat-square&logo=ubuntu&logoColor=white)](https://ubuntu.com)
[![Docker](https://img.shields.io/badge/Docker-Container%20Runtime-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)
[![Bash](https://img.shields.io/badge/Bash-Automation%20Scripts-4EAA25?style=flat-square&logo=gnubash&logoColor=white)](https://gnu.org/software/bash)

> ⚠️ **Authorized Use Only** — All activities must be performed exclusively within the Al Nafi controlled lab environment for educational purposes.

</div>

---

## 📋 Table of Contents

- [🎯 Objectives](#-objectives)
- [✅ Prerequisites](#-prerequisites)
- [🖥️ Lab Environment](#️-lab-environment)
- [🏰 Task 1 — Set Up Covenant for C2 Operations](#-task-1--set-up-covenant-for-c2-operations)
- [🐍 Task 2 — Configure Sliver for Stealth C2](#-task-2--configure-sliver-for-stealth-c2)
- [🗺️ Task 3 — Integrate Infrastructure with C2Matrix](#️-task-3--integrate-infrastructure-with-c2matrix)
- [✔️ Task 4 — Verification and Testing](#️-task-4--verification-and-testing)
- [✅ Expected Outcomes](#-expected-outcomes)
- [🛠️ Troubleshooting Tips](#️-troubleshooting-tips)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Objectives

> By the end of this lab, students will be able to:

| # | Objective |
|---|-----------|
| 1️⃣ | Install and configure **Covenant C2** framework for command and control operations |
| 2️⃣ | Set up **Sliver** for advanced stealth C2 communications |
| 3️⃣ | Deploy **C2Matrix** for centralized infrastructure management |
| 4️⃣ | Create a comprehensive **red team infrastructure** on a single Linux machine |
| 5️⃣ | Understand **operational security** considerations for C2 infrastructure |
| 6️⃣ | Generate and manage **implants** for adversary emulation scenarios |

---

## ✅ Prerequisites

| Skill | Level |
|-------|-------|
| 🐧 Linux Command Line | Basic |
| 🌐 Networking Concepts (TCP/IP, Ports, Protocols) | Familiar |
| 🔐 Cybersecurity Fundamentals | Understanding |
| ⚔️ Red Team Operations & Adversary Emulation | Basic |
| 🐳 Docker Containers | Basic Experience |
| 🌍 Web Interfaces & REST APIs | Familiar |

---

## 🖥️ Lab Environment

<div align="center">

[![Al Nafi Cloud](https://img.shields.io/badge/Platform-Al%20Nafi%20Cloud%20Lab-blue?style=for-the-badge&logo=cloud&logoColor=white)]()
[![Ubuntu](https://img.shields.io/badge/OS-Ubuntu%2022.04%20LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)]()
[![Docker](https://img.shields.io/badge/Docker-Pre--Installed-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![Resources](https://img.shields.io/badge/Resources-Multi--C2%20Capable-green?style=for-the-badge&logo=server&logoColor=white)]()

</div>

Al Nafi provides **pre-configured Linux-based cloud machines** for this lab. Click **▶️ Start Lab** to access your dedicated environment with:

- ✅ Ubuntu 22.04 LTS with all necessary dependencies
- ✅ Docker and Docker Compose pre-installed
- ✅ Required network configurations
- ✅ Sufficient resources for running multiple C2 frameworks

---

## 🏰 Task 1 — Set Up Covenant for C2 Operations

---

### 📦 Subtask 1.1 — Install Prerequisites and Dependencies

[![apt](https://img.shields.io/badge/apt-Package%20Manager-E95420?style=flat-square&logo=ubuntu&logoColor=white)]()
[![.NET](https://img.shields.io/badge/.NET%20SDK-6.0-512BD4?style=flat-square&logo=dotnet&logoColor=white)]()
[![build-essential](https://img.shields.io/badge/build--essential-Compiler%20Tools-4EAA25?style=flat-square&logo=gnubash&logoColor=white)]()

```bash
# 📦 Update system packages
sudo apt update && sudo apt upgrade -y

# 🔧 Install required dependencies
sudo apt install -y git curl wget unzip build-essential

# 📥 Install .NET SDK (required for Covenant)
wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt update
sudo apt install -y dotnet-sdk-6.0

# ✅ Verify .NET installation
dotnet --version
```

---

### 🏗️ Subtask 1.2 — Clone and Build Covenant

[![Covenant](https://img.shields.io/badge/Covenant-Clone%20%26%20Build-1a1a2e?style=flat-square&logo=github&logoColor=white)]()
[![.NET](https://img.shields.io/badge/dotnet-Build%20Tool-512BD4?style=flat-square&logo=dotnet&logoColor=white)]()
[![Git](https://img.shields.io/badge/git-Submodules-F05032?style=flat-square&logo=git&logoColor=white)]()

```bash
# 📂 Create working directory
mkdir -p ~/redteam-lab
cd ~/redteam-lab

# 📥 Clone Covenant repository (with submodules)
git clone --recurse-submodules https://github.com/cobbr/Covenant.git
cd Covenant/Covenant

# 🔨 Build Covenant
dotnet build
```

---

### 🗄️ Subtask 1.3 — Configure Covenant Database

[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat-square&logo=sqlite&logoColor=white)]()
[![JSON](https://img.shields.io/badge/JSON-Config%20File-000000?style=flat-square&logo=json&logoColor=white)]()
[![Entity Framework](https://img.shields.io/badge/EF%20Core-Database%20ORM-512BD4?style=flat-square&logo=dotnet&logoColor=white)]()

```bash
# 📂 Navigate to Covenant directory
cd ~/redteam-lab/Covenant/Covenant

# 📝 Create appsettings.json configuration
cat > appsettings.json << 'EOF'
{
  "ConnectionStrings": {
    "DefaultConnection": "Data Source=Data/covenant.db"
  },
  "CovenantUrl": "https://0.0.0.0:7443",
  "CovenantBindUrl": "0.0.0.0",
  "CovenantPort": 7443,
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft": "Warning",
      "Microsoft.Hosting.Lifetime": "Information"
    }
  }
}
EOF

# 🗄️ Initialize database
dotnet ef database update
```

---

### 🚀 Subtask 1.4 — Start Covenant Server

[![Covenant](https://img.shields.io/badge/Covenant-Start%20Server-1a1a2e?style=flat-square&logo=dotnet&logoColor=white)]()
[![Port](https://img.shields.io/badge/Port-7443%20HTTPS-red?style=flat-square&logo=cloudflare&logoColor=white)]()

```bash
# 🚀 Start Covenant server
cd ~/redteam-lab/Covenant/Covenant
dotnet run &

# ⏳ Wait for server to start
sleep 30

# ✅ Check if Covenant is running
netstat -tlnp | grep 7443
```

---

### 🌐 Subtask 1.5 — Access Covenant Web Interface

[![HTTPS](https://img.shields.io/badge/Web%20UI-https%3A%2F%2Flocalhost%3A7443-1a1a2e?style=flat-square&logo=googlechrome&logoColor=white)]()
[![Bash](https://img.shields.io/badge/Bash-Setup%20Script-4EAA25?style=flat-square&logo=gnubash&logoColor=white)]()

```bash
# 📝 Create initial admin user script
cat > ~/redteam-lab/setup_covenant_user.sh << 'EOF'
#!/bin/bash
echo "🌐 Covenant is accessible at https://localhost:7443"
echo "🔐 Initial setup requires creating an admin user via the web interface"
echo "📋 Use the following credentials for this lab:"
echo "   Username : admin"
echo "   Password : CovenantAdmin123!"
echo "   Email    : admin@redteam.lab"
EOF

chmod +x ~/redteam-lab/setup_covenant_user.sh
~/redteam-lab/setup_covenant_user.sh
```

---

## 🐍 Task 2 — Configure Sliver for Stealth C2

---

### 📥 Subtask 2.1 — Download and Install Sliver

[![Sliver](https://img.shields.io/badge/Sliver-Download%20Release-4a4a8a?style=flat-square&logo=go&logoColor=white)]()
[![GitHub](https://img.shields.io/badge/GitHub-Releases%20API-181717?style=flat-square&logo=github&logoColor=white)]()
[![Go](https://img.shields.io/badge/Go-Binary-00ADD8?style=flat-square&logo=go&logoColor=white)]()

```bash
# 📂 Create Sliver directory
mkdir -p ~/redteam-lab/sliver
cd ~/redteam-lab/sliver

# 🔍 Fetch latest Sliver version tag
SLIVER_VERSION=$(curl -s https://api.github.com/repos/BishopFox/sliver/releases/latest | grep '"tag_name"' | cut -d'"' -f4)

# 📥 Download server and client binaries
wget "https://github.com/BishopFox/sliver/releases/download/${SLIVER_VERSION}/sliver-server_linux" -O sliver-server
wget "https://github.com/BishopFox/sliver/releases/download/${SLIVER_VERSION}/sliver-client_linux" -O sliver-client

# 🔧 Make executables
chmod +x sliver-server sliver-client

# 🔗 Create symbolic links for easier access
sudo ln -sf $(pwd)/sliver-server /usr/local/bin/sliver-server
sudo ln -sf $(pwd)/sliver-client /usr/local/bin/sliver-client
```

---

### ⚙️ Subtask 2.2 — Initialize Sliver Server

[![Sliver](https://img.shields.io/badge/Sliver-Server%20Init-4a4a8a?style=flat-square&logo=go&logoColor=white)]()
[![Daemon](https://img.shields.io/badge/Mode-Daemon%20Process-9B59B6?style=flat-square&logo=linux&logoColor=white)]()

```bash
# 🔧 Initialize Sliver server
cd ~/redteam-lab/sliver
./sliver-server unpack --force

# 🚀 Start Sliver server in daemon mode
./sliver-server daemon &

# ⏳ Wait for server initialization
sleep 15

# ✅ Verify Sliver server is running
ps aux | grep sliver-server
```

---

### 🔌 Subtask 2.3 — Configure Sliver Client

[![Sliver](https://img.shields.io/badge/Sliver-Client%20Config-4a4a8a?style=flat-square&logo=go&logoColor=white)]()
[![gRPC](https://img.shields.io/badge/gRPC-Operator%20Protocol-244c5a?style=flat-square&logo=grpc&logoColor=white)]()

```bash
# 🔑 Generate operator configuration
cd ~/redteam-lab/sliver
./sliver-server operator --name redteam-operator --lhost 127.0.0.1 --save redteam-operator.cfg

# 📥 Import operator configuration
./sliver-client import redteam-operator.cfg

# ✅ Test client connection
echo "exit" | ./sliver-client
```

---

### 📡 Subtask 2.4 — Create Sliver HTTP Listener

[![HTTP](https://img.shields.io/badge/Listener-HTTP%20%3A8080-2CA5E0?style=flat-square&logo=http&logoColor=white)]()
[![HTTPS](https://img.shields.io/badge/Listener-HTTPS%20%3A8443-28a745?style=flat-square&logo=letsencrypt&logoColor=white)]()
[![Bash](https://img.shields.io/badge/Bash-Listener%20Script-4EAA25?style=flat-square&logo=gnubash&logoColor=white)]()

```bash
# 📝 Create Sliver listener setup script
cat > ~/redteam-lab/sliver/setup_listeners.sh << 'EOF'
#!/bin/bash
echo "📡 Starting Sliver client and setting up listeners..."

./sliver-client << 'SLIVER_COMMANDS'
http --lport 8080 --domain localhost
https --lport 8443 --domain localhost --cert /tmp --key /tmp
jobs
exit
SLIVER_COMMANDS
EOF

chmod +x ~/redteam-lab/sliver/setup_listeners.sh
```

---

### 🧬 Subtask 2.5 — Generate Sliver Implants

[![Implants](https://img.shields.io/badge/Sliver-Generate%20Implants-4a4a8a?style=flat-square&logo=go&logoColor=white)]()
[![Linux](https://img.shields.io/badge/Target-Linux%20amd64-FCC624?style=flat-square&logo=linux&logoColor=black)]()
[![Bash](https://img.shields.io/badge/Bash-Implant%20Generator-4EAA25?style=flat-square&logo=gnubash&logoColor=white)]()

```bash
# 📝 Create implant generation script
cat > ~/redteam-lab/sliver/generate_implants.sh << 'EOF'
#!/bin/bash
echo "🧬 Generating Sliver implants..."

./sliver-client << 'SLIVER_COMMANDS'
generate --http localhost:8080 --os linux --arch amd64 --format executable --save /tmp/
generate --https localhost:8443 --os linux --arch amd64 --format executable --save /tmp/
implants
exit
SLIVER_COMMANDS

echo "✅ Implants generated in /tmp/ directory"
ls -la /tmp/*.exe 2>/dev/null || echo "📂 Check /tmp/ for generated implants"
EOF

chmod +x ~/redteam-lab/sliver/generate_implants.sh
```

---

## 🗺️ Task 3 — Integrate Infrastructure with C2Matrix

---

### 📦 Subtask 3.1 — Install C2Matrix

[![C2Matrix](https://img.shields.io/badge/C2Matrix-Clone%20%26%20Install-FF6B35?style=flat-square&logo=github&logoColor=white)]()
[![Django](https://img.shields.io/badge/Django-Web%20Framework-092E20?style=flat-square&logo=django&logoColor=white)]()
[![pip](https://img.shields.io/badge/pip-Python%20Packages-3776AB?style=flat-square&logo=pypi&logoColor=white)]()

```bash
# 📥 Clone C2Matrix repository
cd ~/redteam-lab
git clone https://github.com/Coalfire-Research/C2Matrix.git
cd C2Matrix

# 📦 Install Python dependencies in virtual environment
sudo apt install -y python3-pip python3-venv
python3 -m venv c2matrix-env
source c2matrix-env/bin/activate
pip install -r requirements.txt
```

---

### 🗄️ Subtask 3.2 — Configure C2Matrix Database

[![Django](https://img.shields.io/badge/Django-Database%20Migrations-092E20?style=flat-square&logo=django&logoColor=white)]()
[![SQLite](https://img.shields.io/badge/SQLite-Backend%20DB-003B57?style=flat-square&logo=sqlite&logoColor=white)]()
[![Python](https://img.shields.io/badge/Python-Admin%20Script-3776AB?style=flat-square&logo=python&logoColor=white)]()

```bash
# 📂 Ensure we're in the C2Matrix environment
cd ~/redteam-lab/C2Matrix
source c2matrix-env/bin/activate

# 🔄 Initialize database migrations
python manage.py makemigrations
python manage.py migrate

# 👤 Create superuser for C2Matrix
cat > create_superuser.py << 'EOF'
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'C2Matrix.settings')
django.setup()

from django.contrib.auth.models import User

# ✅ Create superuser if it doesn't exist
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@c2matrix.lab', 'C2MatrixAdmin123!')
    print("✅ Superuser created successfully")
else:
    print("ℹ️  Superuser already exists")
EOF

python create_superuser.py
```

---

### 🔗 Subtask 3.3 — Configure C2 Framework Integration

[![Python](https://img.shields.io/badge/Python-Framework%20Config-3776AB?style=flat-square&logo=python&logoColor=white)]()
[![Django ORM](https://img.shields.io/badge/Django%20ORM-Model%20Setup-092E20?style=flat-square&logo=django&logoColor=white)]()
[![gRPC](https://img.shields.io/badge/gRPC-Sliver%20Protocol-244c5a?style=flat-square&logo=grpc&logoColor=white)]()

```python
# 📄 File: configure_frameworks.py
# 📂 Path: ~/redteam-lab/C2Matrix/

import os           # 🔧 For environment variables
import django       # 🌐 For ORM access
import json         # 📊 For serialization
from datetime import datetime  # 🕒 For timestamps

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'C2Matrix.settings')
django.setup()

from c2matrix.models import Framework, Server

# 🏰 Add Covenant framework
covenant_framework, created = Framework.objects.get_or_create(
    name='Covenant',
    defaults={
        'description': 'Covenant C2 Framework',          # 📋 Framework description
        'version': '0.7',                                  # 🏷️ Framework version
        'documentation_url': 'https://github.com/cobbr/Covenant'  # 🔗 Docs URL
    }
)

# 🖥️ Add Covenant server entry
covenant_server, created = Server.objects.get_or_create(
    framework=covenant_framework,
    name='Covenant-Local',
    defaults={
        'host': '127.0.0.1',         # 🌐 Bind host
        'port': 7443,                 # 🔌 HTTPS port
        'protocol': 'https',          # 🔒 Protocol
        'status': 'active',           # ✅ Server status
        'description': 'Local Covenant C2 Server'
    }
)

# 🐍 Add Sliver framework
sliver_framework, created = Framework.objects.get_or_create(
    name='Sliver',
    defaults={
        'description': 'Sliver C2 Framework',             # 📋 Framework description
        'version': '1.5',                                  # 🏷️ Framework version
        'documentation_url': 'https://github.com/BishopFox/sliver'  # 🔗 Docs URL
    }
)

# 🖥️ Add Sliver server entry
sliver_server, created = Server.objects.get_or_create(
    framework=sliver_framework,
    name='Sliver-Local',
    defaults={
        'host': '127.0.0.1',         # 🌐 Bind host
        'port': 31337,                # 🔌 gRPC port
        'protocol': 'grpc',           # 📡 Protocol
        'status': 'active',           # ✅ Server status
        'description': 'Local Sliver C2 Server'
    }
)

print("✅ Framework configuration completed")
print(f"🏰 Covenant Framework ID : {covenant_framework.id}")
print(f"🐍 Sliver Framework ID   : {sliver_framework.id}")
```

```bash
# 🚀 Run the configuration script
python configure_frameworks.py
```

---

### 🌐 Subtask 3.4 — Start C2Matrix Web Interface

[![Django](https://img.shields.io/badge/Django-Dev%20Server-092E20?style=flat-square&logo=django&logoColor=white)]()
[![Port](https://img.shields.io/badge/Port-8000%20HTTP-2CA5E0?style=flat-square&logo=http&logoColor=white)]()

```bash
# 🚀 Start C2Matrix development server
cd ~/redteam-lab/C2Matrix
source c2matrix-env/bin/activate

# ▶️ Run C2Matrix server
python manage.py runserver 0.0.0.0:8000 &

# ⏳ Wait for server to start
sleep 10

# ✅ Verify C2Matrix is running
netstat -tlnp | grep 8000
```

---

### 📊 Subtask 3.5 — Create Infrastructure Management Dashboard

[![Bash](https://img.shields.io/badge/Bash-Status%20Dashboard-4EAA25?style=flat-square&logo=gnubash&logoColor=white)]()
[![netstat](https://img.shields.io/badge/netstat-Port%20Monitor-0E83CD?style=flat-square&logo=linux&logoColor=white)]()
[![top](https://img.shields.io/badge/top-Resource%20Monitor-FCC624?style=flat-square&logo=linux&logoColor=black)]()

```bash
# 📝 Create dashboard monitoring script
cat > ~/redteam-lab/infrastructure_status.sh << 'EOF'
#!/bin/bash

echo "⚔️  === Red Team Infrastructure Status ==="
echo "📅 Date: $(date)"
echo ""

echo "🏰 === Covenant Status ==="
if netstat -tlnp | grep -q 7443; then
    echo "  ✅ Covenant Server : RUNNING (Port 7443)"
    echo "  🌐 URL             : https://localhost:7443"
else
    echo "  ❌ Covenant Server : NOT RUNNING"
fi
echo ""

echo "🐍 === Sliver Status ==="
if pgrep -f sliver-server > /dev/null; then
    echo "  ✅ Sliver Server   : RUNNING"
    echo "  📡 gRPC Port       : 31337"
    netstat -tlnp | grep -q 8080 && echo "  ✅ HTTP Listener   : Port 8080"
    netstat -tlnp | grep -q 8443 && echo "  ✅ HTTPS Listener  : Port 8443"
else
    echo "  ❌ Sliver Server   : NOT RUNNING"
fi
echo ""

echo "🗺️  === C2Matrix Status ==="
if netstat -tlnp | grep -q 8000; then
    echo "  ✅ C2Matrix Dashboard : RUNNING (Port 8000)"
    echo "  🌐 URL                : http://localhost:8000"
else
    echo "  ❌ C2Matrix Dashboard : NOT RUNNING"
fi
echo ""

echo "📊 === System Resources ==="
echo "  🖥️  CPU    : $(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)%"
echo "  💾 Memory : $(free | grep Mem | awk '{printf("%.1f%%", $3/$2 * 100.0)}')"
echo "  💿 Disk   : $(df -h / | awk 'NR==2{printf "%s", $5}')"
echo ""

echo "🔌 === Active Listening Ports ==="
netstat -tlnp | grep -E "(7443|8000|8080|8443|31337)" | while read line; do
    echo "  📡 $line"
done
EOF

chmod +x ~/redteam-lab/infrastructure_status.sh
```

---

## ✔️ Task 4 — Verification and Testing

---

### 🔬 Subtask 4.1 — Verify All Services

[![curl](https://img.shields.io/badge/curl-API%20Test-073551?style=flat-square&logo=curl&logoColor=white)]()
[![netstat](https://img.shields.io/badge/netstat-Port%20Check-0E83CD?style=flat-square&logo=linux&logoColor=white)]()
[![Bash](https://img.shields.io/badge/Bash-Health%20Check-4EAA25?style=flat-square&logo=gnubash&logoColor=white)]()

```bash
# 📊 Run infrastructure status check
~/redteam-lab/infrastructure_status.sh

# 🏰 Test Covenant API endpoint
curl -k -s https://localhost:7443/api/users 2>/dev/null \
  && echo "✅ Covenant API accessible" \
  || echo "❌ Covenant API not accessible"

# 🗺️ Test C2Matrix web interface
curl -s http://localhost:8000 | grep -q "C2Matrix" \
  && echo "✅ C2Matrix web interface accessible" \
  || echo "❌ C2Matrix web interface not accessible"
```

---

### ⚙️ Subtask 4.2 — Create Operational Scripts

[![Bash](https://img.shields.io/badge/Bash-Start%20%26%20Stop%20Scripts-4EAA25?style=flat-square&logo=gnubash&logoColor=white)]()
[![nohup](https://img.shields.io/badge/nohup-Background%20Processes-FCC624?style=flat-square&logo=linux&logoColor=black)]()

```bash
# 📝 Create start-all infrastructure script
cat > ~/redteam-lab/start_infrastructure.sh << 'EOF'
#!/bin/bash
echo "🚀 Starting Red Team Infrastructure..."

# 🏰 Start Covenant
cd ~/redteam-lab/Covenant/Covenant
nohup dotnet run > covenant.log 2>&1 &
echo "  🏰 Covenant starting..."

# 🐍 Start Sliver
cd ~/redteam-lab/sliver
nohup ./sliver-server daemon > sliver.log 2>&1 &
echo "  🐍 Sliver starting..."

# 🗺️ Start C2Matrix
cd ~/redteam-lab/C2Matrix
source c2matrix-env/bin/activate
nohup python manage.py runserver 0.0.0.0:8000 > c2matrix.log 2>&1 &
echo "  🗺️  C2Matrix starting..."

sleep 15
echo "✅ Startup complete. Run ./infrastructure_status.sh to verify."
EOF

chmod +x ~/redteam-lab/start_infrastructure.sh

# 📝 Create stop-all infrastructure script
cat > ~/redteam-lab/stop_infrastructure.sh << 'EOF'
#!/bin/bash
echo "🛑 Stopping Red Team Infrastructure..."

pkill -f "dotnet run"          # 🏰 Stop Covenant
pkill -f "sliver-server"       # 🐍 Stop Sliver
pkill -f "manage.py runserver" # 🗺️ Stop C2Matrix

echo "✅ All infrastructure services stopped."
EOF

chmod +x ~/redteam-lab/stop_infrastructure.sh
```

---

### 📄 Subtask 4.3 — Document Access Information

[![Markdown](https://img.shields.io/badge/Markdown-Access%20Docs-000000?style=flat-square&logo=markdown&logoColor=white)]()
[![Reference](https://img.shields.io/badge/Reference-Lab%20Credentials-28a745?style=flat-square&logo=shield&logoColor=white)]()

```bash
# 📝 Create access information document
cat > ~/redteam-lab/ACCESS_INFO.md << 'EOF'
# ⚔️ Red Team Infrastructure Access Information

## 🏰 Covenant C2 Framework
- **URL**      : https://localhost:7443
- **Username** : admin
- **Password** : CovenantAdmin123!
- **Email**    : admin@redteam.lab

## 🐍 Sliver C2 Framework
- **Server**          : Running on localhost
- **Client**          : `./sliver-client` from ~/redteam-lab/sliver/
- **HTTP Listener**   : Port 8080
- **HTTPS Listener**  : Port 8443

## 🗺️ C2Matrix Dashboard
- **URL**      : http://localhost:8000
- **Username** : admin
- **Password** : C2MatrixAdmin123!

## 🔧 Useful Commands
- Check status : `~/redteam-lab/infrastructure_status.sh`
- Start all    : `~/redteam-lab/start_infrastructure.sh`
- Stop all     : `~/redteam-lab/stop_infrastructure.sh`

## 📋 Log Files
- Covenant  : ~/redteam-lab/Covenant/Covenant/covenant.log
- Sliver    : ~/redteam-lab/sliver/sliver.log
- C2Matrix  : ~/redteam-lab/C2Matrix/c2matrix.log
EOF

echo "✅ Access information saved to ~/redteam-lab/ACCESS_INFO.md"
```

---

## 🛠️ Troubleshooting Tips

<details>
<summary>🏰 Covenant Fails to Start — Database Errors</summary>

| Problem | Solution |
|---------|----------|
| ❌ DB corruption | Remove and reinitialize `covenant.db` |
| ❌ Migration error | Re-run `dotnet ef database update` |

```bash
cd ~/redteam-lab/Covenant/Covenant
rm -rf Data/covenant.db
dotnet ef database update
```

</details>

<details>
<summary>🐍 Sliver Client Cannot Connect to Server</summary>

| Problem | Solution |
|---------|----------|
| ❌ Auth failure | Regenerate operator config |
| ❌ Config mismatch | Re-import config file |

```bash
cd ~/redteam-lab/sliver
./sliver-server operator --name redteam-operator --lhost 127.0.0.1 --save redteam-operator.cfg
./sliver-client import redteam-operator.cfg
```

</details>

<details>
<summary>🗺️ C2Matrix Shows Database Errors</summary>

| Problem | Solution |
|---------|----------|
| ❌ Missing migrations | Re-run `makemigrations` |
| ❌ Schema mismatch | Apply all pending migrations |

```bash
cd ~/redteam-lab/C2Matrix
source c2matrix-env/bin/activate
python manage.py makemigrations
python manage.py migrate
```

</details>

<details>
<summary>🔌 Port Conflicts</summary>

| Problem | Solution |
|---------|----------|
| ❌ Port already in use | Check for conflicting services |
| ❌ Permission denied | Verify firewall and binding rules |

> Identify and modify port configurations in the respective `appsettings.json` or listener setup files.

</details>

<details>
<summary>⚡ Performance Optimization</summary>

| Tip | Action |
|-----|--------|
| 📊 Monitor resources | Run `infrastructure_status.sh` regularly |
| ⚙️ Tune listeners | Adjust config based on operational requirements |
| 📋 Log rotation | Enable log rotation for long-running sessions |
| 🔒 Firewall rules | Apply rules before production deployments |

</details>

---

## ✅ Expected Outcomes

> After completing this lab, students should have:

| # | Outcome |
|---|---------|
| ✅ | Functional **Covenant C2** with web interface and database |
| ✅ | Running **Sliver C2** with HTTP/HTTPS listeners and generated implants |
| ✅ | **C2Matrix dashboard** managing both frameworks centrally |
| ✅ | Automation scripts for **start, stop, and status** monitoring |
| ✅ | Understanding of **multi-framework C2 coordination** |
| ✅ | Practical experience with **red team infrastructure** deployment |

---

## 🏁 Conclusion

In this comprehensive lab, you successfully built a complete red team infrastructure using three powerful open-source C2 frameworks.

### 🏆 Key Accomplishments

| Framework | Achievement |
|-----------|-------------|
| 🏰 **Covenant C2** | Deployed a .NET-based C2 framework with interactive web interface |
| 🐍 **Sliver C2** | Configured an advanced Go-based C2 with stealth multi-protocol comms |
| 🗺️ **C2Matrix** | Integrated a centralized management dashboard for both frameworks |

### 🧠 Technical Skills Developed

| # | Skill |
|---|-------|
| 🔧 | C2 framework **deployment and configuration** |
| 🔗 | **Infrastructure integration** and management |
| 🔒 | **Operational security** considerations for red team ops |
| 🤖 | **Automation scripting** for infrastructure management |
| 📡 | **Multi-framework coordination** and monitoring |

### 🌍 Real-World Applications

- 🎭 **Adversary Emulation** — Simulating real-world attack scenarios
- ⚔️ **Red Team Operations** — Conducting authorized penetration testing
- 🔬 **Security Research** — Testing defensive capabilities and detection
- 🎓 **Training Environments** — Hands-on experience with professional-grade tools

### ➡️ Next Steps

- 🔌 Explore advanced features of each C2 framework
- 🔒 Implement additional **operational security** measures
- 🔗 Integrate with other security tools (SIEM, logging platforms)
- 📚 Study **MITRE ATT&CK** adversary emulation plans

---

<div align="center">

[![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cloud%20Learning%20Platform-blue?style=for-the-badge&logo=cloud&logoColor=white)](https://alnafi.com)
[![Red Team](https://img.shields.io/badge/Domain-Red%20Team%20Operations-darkred?style=for-the-badge&logo=hackthebox&logoColor=white)]()
[![Ethics](https://img.shields.io/badge/Use-Authorized%20Lab%20Environment%20Only-critical?style=for-the-badge&logo=shield&logoColor=white)]()

**Built with ❤️ for the next generation of cybersecurity professionals**

*© Al Nafi — Cybersecurity Training Program*

</div>
