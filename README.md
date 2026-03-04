# SOC Log Analyzer & Threat Detection Tool

This project simulates a basic Security Operations Center (SOC) detection tool that analyzes system log files and identifies suspicious activities such as brute force login attempts and malicious command execution.

The tool is built using Python and runs in a Linux environment.

---

## Features

• Detects multiple failed login attempts (possible brute-force attack)  
• Detects suspicious command executions (wget, curl, nc)  
• Generates SOC-style alert messages  
• Maps detected activities to MITRE ATT&CK techniques  
• Automatically generates a SOC alert report file  

---

## Technologies Used

Python  
Linux (Kali)  
Regular Expressions (Regex)  
MITRE ATT&CK Framework  

---

## MITRE ATT&CK Mapping

Brute Force Attack → T1110  
Command Execution → T1059  

---

## Project Structure

soc-log-analyzer
│
├── analyzer.py
├── sample_logs.txt
├── soc_alert_report.txt
├── execution.png
├── script.png
├── report.png

---

## How to Run

Run the following command in Linux terminal:

python3 analyzer.py

The tool will analyze the log file and generate alerts if suspicious activity is detected.

---

## Example Alerts

[ALERT] Suspicious Command Detected  
MITRE Technique: T1059 (Command Execution)

[ALERT] Possible Brute Force Attack  
MITRE Technique: T1110 (Brute Force)

---

## Author

Rokesh VJ  
Cybersecurity Enthusiast | SOC Analyst Aspirant
