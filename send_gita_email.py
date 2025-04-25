import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
import json
import os

# Load verses
with open("bhagavad_gita_verses.json", "r", encoding="utf-8") as f:
    verses = json.load(f)

# Get today’s verses
today = date.today()
day_index = (today - date(2025, 1, 1)).days
start = (day_index * 2) % len(verses)
selected = verses[start:start+2]

# Compose email
body = ""
for v in selected:
    body += f"<b>{v['chapter']} – {v['title']} | Verse {v['verse']}</b><br>"
    body += f"<p>{v['text']}</p><hr>"

msg = MIMEMultipart("alternative")
msg["Subject"] = "Your Daily Bhagavad Gita Dose 🌞"
msg["From"] = os.getenv("EMAIL_USER")
msg["To"] = os.getenv("EMAIL_USER")
msg.attach(MIMEText(body, "html"))

# Send email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
    server.sendmail(os.getenv("EMAIL_USER"), os.getenv("EMAIL_USER"), msg.as_string())
