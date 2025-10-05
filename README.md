# Log Security Analyzer

Ein einfaches Python-Tool, das Logdateien analysiert (z. B. `/var/log/auth.log`) und verdächtige Login-Versuche erkennt — wie z. B. **SSH-Brute-Force-Angriffe**.

---

##  Ziel des Projekts
Dieses Projekt soll zeigen, wie man mit **Python** und **Regex** sicherheitsrelevante Daten aus Logfiles extrahiert und Angriffe erkennt.

Du lernst dabei:
- Wie Logdateien aufgebaut sind
- Wie man verdächtige Muster erkennt (z. B. „Failed password“)
- Wie man IP-Adressen extrahiert und zählt
- Wie man einfache Regeln zur **Anomalie-Erkennung** implementiert

---

##  Features
-  Sucht nach fehlgeschlagenen Login-Versuchen (`Failed password`)
-  Zählt, welche IPs am häufigsten scheitern
-  Markiert verdächtige IPs (z. B. mehr als 5 Fehlversuche)
-  Erstellt JSON-Report mit Übersicht aller verdächtigen Aktivitäten
- (Optional) Prüft IPs über **AbuseIPDB API** auf bekannte Angreifer

---

## 🏗️ Projektstruktur
log-security-analyzer/
├── src/
│ └── analyze.py # Hauptskript
├── data/
│ └── auth.log # Beispiel-Logdatei
├── report/
│ └── report.json # Ausgabe (Bericht)
└── README.md
