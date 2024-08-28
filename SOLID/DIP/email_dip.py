"""
In this example, the EmailService class directly depends on the GmailClient class,
a low-level module that implements the details of sending emails using the Gmail API.

This violates the DIP because the high-level EmailService module is tightly coupled to
the low-level GmailClient module.

To adhere to the DIP, we can introduce an abstraction (interface) for email clients.
"""

class EmailClient:
    def send_email(self, recipient, subject, body):
         raise NotImplementedError

class GmailClient(EmailClient):
    def send_email(self, recipient, subject, body):
        # Logic to send email using Gmail API

class OutlookClient(EmailClient):
    def send_email(self, recipient, subject, body):
        # Logic to send email using Outlook API

class EmailService:
    def __init__(self, email_client):
        self.email_client = email_client

    def send_email(self, recipient, subject, body):
        self.email_client.send_email(recipient, subject, body)


# Usage
gmail_client = GmailClient()
email_service = EmailService(gmail_client)
email_service.send_email("recipient@example.com", "Subject", "Email Body")

"""
Now, we can see that EmailService class depends on the EmailClient abstraction,
and the low-level email client implementations (GmailClient and OutlookClient)
depend of the abstraction.
"""