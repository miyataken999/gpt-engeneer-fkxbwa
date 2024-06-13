from dataclasses import dataclass

@dataclass
class Card:
    """
    Google Chat card
    """
    header: str
    sections: list

    def to_dict(self):
        """
        Convert card to dictionary
        """
        return {
            'header': {'title': self.header},
            'sections': [{'widgets': [{'textParagraph': {'text': section}} for section in self.sections]}]
        }