from enum import Enum

class Label(Enum):
    BIOLOGY = "Biology and genetics research"
    MEDICINE = "Medical and health sciences"
    SPORTS = "Football and sports journalism"
    ECONOMY = "Financial markets and investments"
    TECHNOLOGY = "Technology and artificial intelligence"
    SOCIETY = "Social and environmental issues"
    ACCIDENTS = "Accidents, disasters and emergencies"
    ENTERTAINMENT = "Entertainment and popular culture"

    @classmethod
    def values(cls):
        return [label.value for label in cls]
