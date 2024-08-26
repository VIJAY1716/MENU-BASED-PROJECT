import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_bulk_emails(subject, body, to_addresses, smtp_server, smtp_port, smtp_user, smtp_password, attachment_path=None):
    """
    Send bulk emails with optional attachments.

    Parameters:
    - subject: Email subject
    - body: Email body content
    - to_addresses: List of recipient email addresses
    - smtp_server: SMTP server address
    - smtp_port: SMTP server port
    - smtp_user: SMTP username (email address)
    - smtp_password: SMTP password
    - attachment_path: Path to attachment file (optional)
    """
    try:
        # Set up the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)

        for to_address in to_addresses:
            # Create a MIMEMultipart object
            msg = MIMEMultipart()
            msg['From'] = smtp_user
            msg['To'] = to_address
            msg['Subject'] = subject

            # Attach the body
            msg.attach(MIMEText(body, 'plain'))

            # Attach a file if specified
            if attachment_path:
                with open(attachment_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename={attachment_path.split("/")[-1]}',
                    )
                    msg.attach(part)

            # Send the email
            server.send_message(msg)
            print(f"Email sent to {to_address}")

        # Quit the server
        server.quit()

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    subject = "Bulk Email Test"
    body = "This is a test email sent in bulk using Python."
    to_addresses = ['2022bcaaidsvijay11316@poornima.edu.in', 'coolvijay3716@gmail.com']
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'vijayaganesh1617@gmail.com'
    smtp_password = 'dmvz ddff dkyx jedp'
    

    send_bulk_emails(subject, body, to_addresses, smtp_server, smtp_port, smtp_user, smtp_password)
