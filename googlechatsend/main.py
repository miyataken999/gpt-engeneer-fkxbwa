from googlechatsend.config import WEBHOOK_URL
from googlechatsend.google_chat import GoogleChat
from googlechatsend.card import Card

def main():
    """
    Main function
    """
    chat = GoogleChat(WEBHOOK_URL)
    card = Card('Hello from Python!', ['Line 1', 'Line 2', 'Line 3'])
    chat.send_message({'cards': [card.to_dict()]})

if __name__ == '__main__':
    main()