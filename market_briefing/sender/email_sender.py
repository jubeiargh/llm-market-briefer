import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from market_briefing.config import EMAIL_PASS, EMAIL_SUBJECT, EMAIL_TO, EMAIL_USER


def send_daily_email(html_content: str):
    # Create MIME message
    msg = MIMEMultipart("alternative")
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_TO
    msg["Subject"] = EMAIL_SUBJECT

    # Attach HTML content
    msg.attach(MIMEText(html_content, "html"))

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)


if __name__ == "__main__":
    send_daily_email()
