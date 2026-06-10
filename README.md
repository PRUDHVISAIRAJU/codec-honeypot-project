# 🛡️ Honeypot Security System

## 📌 Project Overview
This project is a Python-based Honeypot system designed to detect unauthorized connection attempts, log attacker IP addresses, and record timestamps for security monitoring and analysis.

It simulates a real-world vulnerable service to understand how attackers interact with exposed systems.

---

## 🎯 Objective
To design and implement a lightweight honeypot that captures connection attempts and demonstrates basic intrusion detection and logging techniques used in cybersecurity.

---

## 🧰 Tools & Technologies
- Python 3
- Socket Programming
- Linux Terminal
- Netcat (nc)

---

## ⚙️ Features
- Detects incoming network connections
- Logs attacker IP addresses
- Records timestamp of each connection
- Sends fake response (“Access Denied”)
- Lightweight and easy to deploy

---

## 📂 Project Structure
Codec_Honeypot_Project/
│
├── honeypot.py
├── logs/
│   └── connections.log
├── screenshots/
│   └── SS01_Honeypot_Connection.png
└── README.md

---

## 📸 Screenshots

### Honeypot Connection Detected
![Honeypot Connection](screenshots/SS01_Honeypot_Connection.png)

---

## 💻 Sample Output
Honeypot listening on port 2222...
Connection received from 127.0.0.1

---

## 📊 Sample Log Entry
2026-06-10 20:44:12 - 127.0.0.1

---

## 🔐 Security Insight
This project demonstrates how attackers probe open ports and how basic logging mechanisms can help in early threat detection.

---

## 🚀 Learning Outcomes
- Network socket programming
- Intrusion detection basics
- Log analysis
- Cybersecurity monitoring concepts

---

## 👨‍💻 Author
Prudhvisairaju Poranki
