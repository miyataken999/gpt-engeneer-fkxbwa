import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class GoogleChatClient:
    def __init__(self, config, auth):
        self.config = config
        self.auth = auth
        self.service = build('chat', 'v1', credentials=self.auth.creds)

    def send_message(self, message):
        try:
            response = self.service.spaces().messages().create(
                parent=f'spaces/{self.config.SPACE_ID}',
                body={'text': message}
            ).execute()
            print(f'Message sent: {response.get("name")}')
        except HttpError as error:
            print(f'Error sending message: {error}')