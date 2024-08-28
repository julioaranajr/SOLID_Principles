"""
Dependency Inversion Principle

Dependency should be on abstractions not concretions
A. High-level modules should not depend upon low-level modules.
Both should depend upon abstractions.
B. Abstractions should not depend on details. Details should depend
upon abstractions.
"""

class GmailClient:
    def send_email(self, recipient, subject, body):
        # Logic to send email using Gmail API

class EmailService:
    def __init__(self):
        self.gmail_client = GmailClient()

    def send_email(self, recipient, subject, body):
        self.gmail_client.send_email(recipient, subject, body)
