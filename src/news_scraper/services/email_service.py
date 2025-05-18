"""
Email service module for sending emails.
"""
import smtplib
from email.mime.text import MIMEText
from src.news_scraper.config import EMAIL_CONFIG

class EmailService:
    @staticmethod
    def send_email(recipient_email, subject, html_content):
        """
        Send an HTML email.
        
        Args:
            recipient_email (str): Email address of the recipient
            subject (str): Email subject
            html_content (str): HTML content of the email
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        message = MIMEText(html_content, "html")
        message["Subject"] = subject
        message["From"] = EMAIL_CONFIG["sender_email"]
        message["To"] = recipient_email

        try:
            with smtplib.SMTP_SSL(
                EMAIL_CONFIG["smtp_server"], 
                EMAIL_CONFIG["smtp_port"]
            ) as server:
                server.login(
                    EMAIL_CONFIG["sender_email"],
                    EMAIL_CONFIG["sender_password"]
                )
                server.sendmail(
                    EMAIL_CONFIG["sender_email"],
                    recipient_email,
                    message.as_string()
                )
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False 