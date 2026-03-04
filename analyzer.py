import re
from collections import defaultdict

log_file = "sample_logs.txt"
report_file = open("soc_alert_report.txt", "w")

failed_login_pattern = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"
suspicious_commands = ["wget", "curl", "nc", "netcat"]

failed_attempts = defaultdict(int)

def alert(message):
    print(message)
    report_file.write(message + "\n")

with open(log_file, "r") as file:
    logs = file.readlines()

for line in logs:

    match = re.search(failed_login_pattern, line)

    if match:
        ip = match.group(1)
        failed_attempts[ip] += 1

    for cmd in suspicious_commands:
        if cmd in line:
            alert("\n[ALERT] Suspicious Command Detected")
            alert("MITRE Technique: T1059 (Command Execution)")
            alert("Log: " + line.strip())

for ip, attempts in failed_attempts.items():
    if attempts >= 3:
        alert("\n[ALERT] Possible Brute Force Attack")
        alert("MITRE Technique: T1110 (Brute Force)")
        alert("IP Address: " + ip)
        alert("Attempts: " + str(attempts))

report_file.close()
