import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return(f"{self.value} of {self.suit}")








""" CARD CLASS TESTING """
# card = Card("Hearts", 10)
# print(card)