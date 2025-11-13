import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

#---------------CONFIG-----------------------
CSV_FILE = "recipients.csv"

#script must have authorization to send the emails (uses gmail app password)
SENDER_EMAIL = "user@gmail.com"
SENDER_PASSWORD = "aaaa aaaa aaaa aaaa"

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587                                 # modern standard

SUBJECT = "Example Subject"
BODY_TEMPLATE = """\
GREETING {name},
BODY
SIGNOFF,
NAME
"""

DELAY_BETWEEN_EMAILS = 2

#parses through the given csv file and returns a list of recipients
def load_recipients(filename):
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

#given the config information, puts together and sends the email
def send_email(recipient):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient['email']
    msg["Subject"] = SUBJECT

    body = BODY_TEMPLATE.format(name=recipient.get("get", "there"))
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        print(f"Sent to {recipient['email']}")

#get recipients
#for each recipient, try to send and email
def main():
    recipients = load_recipients(CSV_FILE)
    for recipient in recipients:
        try:
            send_email(recipient)
        except Exception as e:
            print(f"Error sending to {recipient['email']}: {e}")
        time.sleep(DELAY_BETWEEN_EMAILS)

if __name__ == "__main__":
    main()