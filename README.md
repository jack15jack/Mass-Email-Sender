# Bulk Email Sender

A lightweight Python script for sending personalized emails to a list of recipients stored in a CSV file.
This project is ideal for sending announcements, invitations, newsletters, or other personalized messages without relying on third-party mailing services.

---

## Features

- Send personalized emailsusing Gmail SMTP
- Load recipients from a CSV file
- Automatically personalize each email with the recipient's name
- Configurable delay between emails to reduce spam detection
- Graceful error handling so one failed email doesn't stop the rest
- Simple configuration with no external dependencies

## Project Structure

- massemailsender.py    # Main script
- recipients.csv        # Recipient list
- README.md

## Requirements
- Python 3.8+
- Gmail account
- Gmail App Password (recommended)

This project only uses Python's standard library, so no additional packages need to be installed.

---

## Setup
```bash
git clone https://github.com/yourusername/bulk-email-sender.git
cd bulk-email-sender
```

---

### 2. Enable Gmail App Passwords

Google no longer allows normal account passwords for SMTP access.

1. Enable **2-Step Verification** on your Google account.
2. Navigate to **Google Account → Security → App Passwords**.
3. Generate a new App Password for **Mail**.
4. Copy the generated 16-character password.

---

### 3. Configure the script

Edit the configuration section near the top of `bulk_email.py`.

```python
CSV_FILE = "recipients.csv"

SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SUBJECT = "Example Subject"

BODY_TEMPLATE = """\
Hello {name},

Thank you for your interest!

Best,
Your Name
"""

DELAY_BETWEEN_EMAILS = 2
```

---

## Recipient CSV Format

Create a file named `recipients.csv`.

Example:

```csv
name,email
John Doe,john@example.com
Jane Smith,jane@example.com
Alice Johnson,alice@example.com
```

### Required Columns

| Column | Description |
|----------|-------------|
| `name` | Recipient's name used for personalization |
| `email` | Recipient email address |

---

## Personalization

The email body supports Python string formatting.

Example:

```python
BODY_TEMPLATE = """
Hello {name},

Thank you for attending our event!

Sincerely,
Example Company
"""
```

For a recipient named **John**, the email becomes:

```
Hello John,

Thank you for attending our event!

Sincerely,
Example Company
```

---

## Running

Execute the script from the command line:

```bash
python bulk_email.py
```

Example output:

```
Sent to john@example.com
Sent to jane@example.com
Sent to alice@example.com
```

If an email fails:

```
Error sending to bob@example.com: Authentication failed
```

The script will continue sending to the remaining recipients.

---

## How It Works

1. Load all recipients from `recipients.csv`
2. Loop through each recipient
3. Personalize the email body
4. Connect securely to Gmail's SMTP server
5. Send the email
6. Wait for the configured delay
7. Repeat until complete

---

## Configuration Options

| Variable | Description |
|-----------|-------------|
| `CSV_FILE` | Path to recipient CSV |
| `SENDER_EMAIL` | Gmail address used to send emails |
| `SENDER_PASSWORD` | Gmail App Password |
| `SMTP_SERVER` | SMTP server hostname |
| `SMTP_PORT` | SMTP server port (587 for TLS) |
| `SUBJECT` | Email subject |
| `BODY_TEMPLATE` | Email body template |
| `DELAY_BETWEEN_EMAILS` | Delay (seconds) between emails |

---

## Security

**Never commit your Gmail credentials to GitHub.**

Instead of storing credentials directly in the script, consider using environment variables:

```python
import os

SENDER_EMAIL = os.getenv("EMAIL")
SENDER_PASSWORD = os.getenv("EMAIL_PASSWORD")
```

Then set them before running:

**Windows**

```powershell
set EMAIL=your_email@gmail.com
set EMAIL_PASSWORD=your_app_password
```

**Linux / macOS**

```bash
export EMAIL="your_email@gmail.com"
export EMAIL_PASSWORD="your_app_password"
```

This is significantly more secure than hardcoding credentials.

---

## Current Limitations

- Gmail SMTP only
- Plain-text emails only
- No attachments
- No HTML formatting
- No CC/BCC support
- No retry mechanism for failed sends

---

## Possible Future Improvements

- HTML email support
- Attachments
- Multiple email templates
- Logging to a file
- Email validation
- Progress bar
- Retry failed emails
- Support for Outlook and other SMTP providers
- Command-line arguments
- Environment variable configuration by default
- Rate limiting based on provider recommendations

---

## License

This project is available under the MIT License.

---

## Disclaimer

Use this project responsibly. Sending large volumes of unsolicited email may violate your email provider's terms of service or applicable laws. Always obtain permission from recipients before sending bulk emails.
