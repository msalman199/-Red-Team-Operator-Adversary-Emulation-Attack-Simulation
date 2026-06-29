# 🎭 Build Decoy Server to Confuse Defenders

<div align="center">

# 🛡️ Red Team Adversary Simulation 

### **Build, Deploy, Automate, and Evaluate a Decoy Server**

![Platform](https://img.shields.io/badge/Platform-Linux-blue?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Red%20Team-red?style=for-the-badge)
![Language](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge)

</div>

---

# 📖 Overview

Modern red team operations often rely on deception to delay investigations, consume defender resources, and simulate realistic environments during authorized security assessments. One effective technique is deploying **decoy infrastructure** that appears to be a legitimate production service while generating convincing operational activity.

In this lab, students build a realistic **decoy web server**, automate its deployment, generate believable traffic, monitor activity, and evaluate the effectiveness of deception using Python automation.

The objective is to understand the concepts behind deception technology and infrastructure simulation in **authorized cybersecurity training environments**.

---

# 🎯 Learning Objectives

After completing this lab, you will be able to:

* ✅ Deploy a realistic decoy web server
* ✅ Build convincing business web content
* ✅ Generate realistic background traffic
* ✅ Automate decoy deployment using Python
* ✅ Analyze server logs
* ✅ Monitor decoy infrastructure
* ✅ Measure deception effectiveness
* ✅ Apply automation techniques for security operations

---

# 🛠 Technology Stack

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge\&logo=flask)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-E95420?style=for-the-badge\&logo=ubuntu\&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Operating%20System-FCC624?style=for-the-badge\&logo=linux\&logoColor=black)
![Nginx](https://img.shields.io/badge/Nginx-Web%20Server-009639?style=for-the-badge\&logo=nginx)
![JSON](https://img.shields.io/badge/JSON-Configuration-black?style=for-the-badge\&logo=json)
![Bash](https://img.shields.io/badge/Bash-Scripting-4EAA25?style=for-the-badge\&logo=gnubash)
![HTTP](https://img.shields.io/badge/HTTP-Networking-blue?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge\&logo=git)
![VS Code](https://img.shields.io/badge/VSCode-Editor-007ACC?style=for-the-badge\&logo=visualstudiocode)

</p>

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

* 🐧 Basic Linux command-line skills
* 🌐 Understanding of TCP/IP networking
* 🐍 Python programming fundamentals
* 🌍 Familiarity with HTTP and web servers
* 📄 Basic knowledge of system logging
* 💻 Ubuntu/Linux environment

---

# 🖥 Lab Environment

The lab environment includes:

* ✅ Ubuntu 22.04 LTS
* ✅ Python 3.10+
* ✅ Flask
* ✅ Requests
* ✅ psutil
* ✅ Nginx Light
* ✅ Curl
* ✅ Netcat
* ✅ Nano & Vim
* ✅ Pre-configured dependencies

---

# 📚 Lab Tasks

---

# 🚩 Task 1 — Build the Decoy Server

### 🎯 Goal

Create a realistic enterprise web server that mimics a legitimate organization.

### ✅ Step 1.1

📁 Create the project directory structure.

---

### ✅ Step 1.2

📦 Install all required system and Python dependencies.

---

### ✅ Step 1.3

🌐 Design convincing business web pages including:

* Home page
* Admin portal
* Login interface

---

### ✅ Step 1.4

🐍 Develop the Flask application featuring:

* Visitor logging
* Fake login handling
* Status API
* Health endpoint
* Administrative portal
* Activity logging

---

### ✅ Step 1.5

🧪 Test the web server using HTTP requests.

---

# 🚩 Task 2 — Generate Realistic Traffic

### 🎯 Goal

Produce believable user activity that makes the server appear active.

### ✅ Step 2.1

🚦 Develop the Traffic Obfuscator.

Features include:

* Normal user traffic
* Browser simulation
* Random timing
* Login attempts
* Reconnaissance simulation

---

### ✅ Step 2.2

📊 Build automated log analysis tools.

Analyze:

* Requests
* User agents
* Login attempts
* IP addresses
* Traffic patterns

---

### ✅ Step 2.3

🧪 Execute the traffic generator and verify realistic activity.

---

# 🚩 Task 3 — Automate Deployment

### 🎯 Goal

Deploy the complete decoy infrastructure automatically.

### ✅ Step 3.1

⚙️ Create a deployment automation script.

Responsibilities include:

* Dependency checks
* Service startup
* Process management
* Graceful shutdown

---

### ✅ Step 3.2

📝 Build a JSON configuration file.

Store:

* Server settings
* Logging options
* Traffic intervals
* Runtime configuration

---

### ✅ Step 3.3

🚀 Deploy and validate the entire environment.

---

# 🚩 Task 4 — Measure Decoy Effectiveness

### 🎯 Goal

Evaluate how convincing the deployed decoy appears.

### ✅ Step 4.1

📡 Monitor:

* Active connections
* Requests
* Live logs
* Server activity

---

### ✅ Step 4.2

📈 Calculate effectiveness metrics including:

* Believability score
* Traffic realism
* User-agent diversity
* Activity consistency

---

### ✅ Step 4.3

📊 Generate the final effectiveness report.

---

# 📁 Project Structure

```text
decoy-server-lab/
│
├── configs/
│   └── decoy_config.json
│
├── logs/
│   └── decoy-server.log
│
├── scripts/
│   ├── decoy_server.py
│   ├── traffic_obfuscator.py
│   ├── analyze_logs.py
│   ├── deploy_decoy.py
│   ├── monitor_decoy.py
│   └── effectiveness_metrics.py
│
└── web-content/
    ├── index.html
    └── admin.html
```

---

# 🎓 Learning Outcomes

Upon successful completion, students will have learned how to:

* ✅ Build realistic decoy web infrastructure
* ✅ Create convincing enterprise web content
* ✅ Generate automated background traffic
* ✅ Deploy services using Python automation
* ✅ Monitor infrastructure activity
* ✅ Analyze operational logs
* ✅ Evaluate deception effectiveness
* ✅ Apply automation to security operations

---

# 📂 Deliverables

Students will produce:

* 🐍 Flask decoy server
* 🌐 Enterprise website
* 📈 Traffic generation engine
* 📊 Log analyzer
* 🚀 Deployment automation
* 📡 Monitoring utilities
* ⚙️ Configuration files
* 📑 Effectiveness reports

---

# 💡 Skills Gained

* Linux Administration
* Python Automation
* Flask Development
* HTTP Fundamentals
* Network Monitoring
* Log Analysis
* Process Automation
* Infrastructure Deployment
* Configuration Management
* Security Operations

---

# ⚠️ Ethical Notice

This lab is intended **only for authorized cybersecurity education, red team exercises, and controlled environments**. Always obtain proper authorization before deploying or testing security infrastructure on any network or system.

---

# 🏁 Conclusion

This lab provides practical experience in building and managing a realistic decoy server while exploring concepts of infrastructure simulation, automation, monitoring, and log analysis. By completing the exercises, students gain hands-on experience with Python-based automation, web service deployment, and operational monitoring in a controlled training environment.

---

<div align="center">

### ⭐ Happy Learning & Happy Ethical Hacking! ⭐

**Build • Automate • Monitor • Analyze • Learn**

</div>
