<!-- nav -->
[← Day 74](../Day74/lesson.md) | [🏠 Home](../../) | [Day 76 →](../Day76/lesson.md)

---
<!-- nav -->

# Day 75 – Email Automation with `smtplib`

## Learning Objectives
- Send plain-text and HTML emails with `smtplib` + `email`
- Add attachments with `MIMEMultipart`
- Store credentials safely in environment variables

---

## Basic Email Setup

```python
import smtplib
from email.mime.text import MIMEText
import os

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
USERNAME  = os.getenv("EMAIL_USER")
PASSWORD  = os.getenv("EMAIL_PASS")   # use an App Password for Gmail
```

---

## Sending a Plain-Text Email

```python
msg = MIMEText("Hello from Python!", "plain")
msg["Subject"] = "Test Email"
msg["From"]    = USERNAME
msg["To"]      = "recipient@example.com"

with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
    server.ehlo()
    server.starttls()          # encrypt the connection
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, [msg["To"]], msg.as_string())
print("Email sent!")
```

---

## HTML Email

```python
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart("alternative")
msg["Subject"] = "HTML Email"
msg["From"]    = USERNAME
msg["To"]      = "recipient@example.com"

html = "<h1>Hello!</h1><p>This is <b>bold</b>.</p>"
msg.attach(MIMEText(html, "html"))
```

---

## Adding an Attachment

```python
from email.mime.base import MIMEBase
from email import encoders

part = MIMEBase("application", "octet-stream")
with open("report.csv", "rb") as f:
    part.set_payload(f.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", 'attachment; filename="report.csv"')
msg.attach(part)
```

---

## Key Takeaways
- Use `starttls()` to encrypt — never send credentials over plain SMTP
- Gmail requires an **App Password** (2FA must be enabled); never use your real password
- Store credentials in `.env` / environment variables — never in source code

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 74](../Day74/lesson.md) | [Day 76 →](../Day76/lesson.md)
<!-- nav -->
