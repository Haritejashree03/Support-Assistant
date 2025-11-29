import csv
from datetime import datetime
import os

TICKET_FILE = "tickets.csv"

def log_ticket(query: str, status: str, confidence: float):
    file_exists = os.path.isfile(TICKET_FILE)

    with open(TICKET_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "query", "status", "confidence"])
        writer.writerow([datetime.now().isoformat(), query, status, f"{confidence:.4f}"])
