import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class GoogleChat:
    """
    Google Chat API client
    """
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        self.service = self._create_service()

    def _create_service(self):
        """
        Create a Google Chat service client
        """
        credentials = service_account.Credentials.from_service_account_file(
            'path/to/service_account_key.json',
            scopes=['https://www.googleapis.com/auth/chat.bot']
        )
        return build('chat', 'v1', credentials=credentials)

    def send_message(self, message):
        """
        Send a message to Google Chat
        """
        try:
            response = self.service.spaces().messages().create(
                parent=self.webhook_url,
                body={'text': message}
            ).execute()
            print(f'Message sent: {response.get("name")}')
        except HttpError as error:
            print(f'Error sending message: {error}')