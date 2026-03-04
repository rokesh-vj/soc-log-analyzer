SOC Log Analyzer & Threat Detection Tool

Overview

The SOC Log Analyzer is a Python-based security tool that analyzes Linux log files and detects suspicious activities such as brute force login attempts and malicious command execution.

This project simulates a basic Security Operations Center (SOC) detection workflow and maps detected activities to MITRE ATT&CK techniques.

The tool reads log files, identifies suspicious patterns, and generates a SOC-style alert report.

---

Features

- Detects multiple failed login attempts (possible brute force attack)
- Detects suspicious command executions (wget, curl, nc)
- Maps detected activities to MITRE ATT&CK techniques
- Generates SOC-style alert messages
- Automatically creates a SOC alert report file

---

Technologies Used

- Python
- Linux Logs
- MITRE ATT&CK Framework

---

Project Structure

soc-log-analyzer/
│
├── analyzer.py              # Main SOC detection script
├── sample_logs.txt          # Sample log file for testing
├── soc_alert_report.txt     # Generated alert report
│
├── screenshots/
│   ├── script.png
│   ├── execution.png
│   └── report.png
│
└── README.md

---

How to Run

1. Clone the repository

git clone https://github.com/rokesh-vj/soc-log-analyzer.git

2. Navigate to the project folder

cd soc-log-analyzer

3. Run the analyzer

python3 analyzer.py

The tool will analyze the log file and generate alerts if suspicious activity is detected.

---

Tool Execution

Script

"Script" (script.png)

Execution Output

"Execution" (execution.png)

Generated Report

"Report" (report.png)

---

Example Alerts

[ALERT] Suspicious Command Detected
MITRE Technique: T1059 (Command Execution)

[ALERT] Possible Brute Force Attack
MITRE Technique: T1110 (Brute Force)

---

Future Improvements

- Real-time log monitoring
- Integration with SIEM platforms
- Email or Slack alert notifications
- IP reputation checking using threat intelligence APIs

---

Author

Rokesh Kumar V
Cybersecurity Enthusiast | SOC Analyst Aspirant
