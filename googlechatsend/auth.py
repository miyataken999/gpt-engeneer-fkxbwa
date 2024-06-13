import os
import json
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

class Authenticator:
    def __init__(self, config):
        self.config = config
        self.creds = None
        self.token_file = config.TOKEN_FILE

    def authenticate(self):
        # Load credentials from file
        if os.path.exists(self.token_file):
            with open(self.token_file, 'r') as f:
                self.creds = json.load(f)
        # If not, authenticate using OAuth 2.0 flow
        if not self.creds or not self.creds.get('token'):
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json',
                scopes=['https://www.googleapis.com/auth/chat.serviceagent']
            )
            self.creds = flow.run_local_server(port=0)
            with open(self.token_file, 'w') as f:
                json.dump(self.creds, f)