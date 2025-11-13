import json
import re
import os
from collections import Counter

LOGFILE = "data/auth.log"


def extract_ip(line: str):
    """Extrahiert IP aus 'Failed password'-Zeilen."""
    match = re.search(r"Failed password.*from ([\d.]+)", line)
    if match:
        return match.group(1)
    return None


def main():

    #Logfile lesen
    if not os.path.exists(LOGFILE):
        print(f"Logfile '{LOGFILE}' wurde nicht gefunden.")
        return

    with open(LOGFILE, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    #IPs extrahieren
    ips = []

    for line in lines:
        ip = extract_ip(line)
        if ip:
            ips.append(ip)

    #IPs Zählen
    ip_counts = Counter(ips)

    #verdächtige IPs (mehr als 3 Fehler)
    suspicious_ips = {ip: count for ip, count in ip_counts.items() if count > 3}

    #Report vorbereiten
    report = {
        "total_failed_attempts": sum(ip_counts.values()),
        "unique_ips": len(ip_counts),
        "top_ips": ip_counts.most_common(10),
        "suspicious_ips": suspicious_ips
    }

    #Ordner erstellen
    os.makedirs("report", exist_ok=True)

    #JSON schreiben
    with open("report/report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("Report erstellt unter report/report.json")


if __name__ == "__main__":
    main()
