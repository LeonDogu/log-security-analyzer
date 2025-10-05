import json
import re
import os
from collections import Counter

logfile = 'data/auth.log'
reportfile = 'suspicious_ips.txt'

def extract_ip(line):
    match = re.search(r'Failed password.*from ([\d.]+)', line)
    if match:
        return match.group(1)
    return None


def main():
    ip_list=[]
    with open (logfile, 'r', encoding='utf-8') as f:
        for line in f:
            if 'Failed password' in line.lower():
                ip = extract_ip(line)
                if ip:
                    ip_list.append(ip)
    ip_counter = Counter(ip_list)
    suspicious_ips = {ip: count for ip, count in ip_counter.items() if count >= 3}

    # 🔹 3. Debug-Ausgaben einfügen, um zu sehen, ob es klappt
    print("Zeilen mit 'Failed password':", len(ip_list))
    print("Einzigartige IPs:", len(ip_counter))
    print("Verdächtige IPs (>=3):", suspicious_ips)

    
    report = {
    "total_failed": len(ip_list),
    "unique_ips": len(ip_counter),
    "suspicious_ips": suspicious_ips
}
    os.makedirs("report", exist_ok=True)

    
    with open("report/report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)  


    print("Report erstellt unter report/report.json")


if __name__ == "__main__":
    main()

