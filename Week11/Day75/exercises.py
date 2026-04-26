# Day 75 – Email Automation with smtplib
# NOTE: To actually send emails you need valid SMTP credentials.
# These exercises show the setup and message-building steps.
# Exercise 1–3 are runnable without credentials; Exercise 4 requires them.

import smtplib, os
from email.mime.text      import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base      import MIMEBase
from email                import encoders


# Exercise 1: Build a plain-text email and print it as a string (no sending).

# Solution:
msg = MIMEText("Hello! This is a test email from Python.", "plain")
msg["Subject"] = "Day 75 Test"
msg["From"]    = "sender@example.com"
msg["To"]      = "recipient@example.com"
print("Plain text email:")
print(msg.as_string()[:300])


# Exercise 2: Build an HTML email with a greeting.

# Solution:
html_msg = MIMEMultipart("alternative")
html_msg["Subject"] = "Python HTML Email"
html_msg["From"]    = "sender@example.com"
html_msg["To"]      = "recipient@example.com"
html = "<h2>Hello from Python!</h2><p>This email was built with <b>MIMEMultipart</b>.</p>"
html_msg.attach(MIMEText(html, "html"))
print("\nHTML email Content-Type:", html_msg.get_content_type())


# Exercise 3: Build an email with a CSV attachment.

# Solution:
import csv, io

# create CSV in memory
buf = io.StringIO()
csv.writer(buf).writerows([["name","score"],["Alice","95"],["Bob","82"]])
csv_bytes = buf.getvalue().encode()

attach_msg = MIMEMultipart()
attach_msg["Subject"] = "Report Attached"
attach_msg["From"]    = "sender@example.com"
attach_msg["To"]      = "recipient@example.com"
attach_msg.attach(MIMEText("See attached report.", "plain"))

part = MIMEBase("application", "octet-stream")
part.set_payload(csv_bytes)
encoders.encode_base64(part)
part.add_header("Content-Disposition", 'attachment; filename="report.csv"')
attach_msg.attach(part)
print("\nEmail with attachment parts:", len(attach_msg.get_payload()))


# Exercise 4: (Requires valid credentials — skipped in auto-run)
# To actually send:
# USERNAME = os.getenv("EMAIL_USER")
# PASSWORD = os.getenv("EMAIL_PASS")
# with smtplib.SMTP("smtp.gmail.com", 587) as server:
#     server.ehlo()
#     server.starttls()
#     server.login(USERNAME, PASSWORD)
#     server.sendmail(USERNAME, [msg["To"]], msg.as_string())
print("\nExercise 4: Set EMAIL_USER and EMAIL_PASS env vars, then uncomment the send code.")
