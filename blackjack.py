import random

#CARD CLASS
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return(f"{self.value} of {self.suit}")

#DECK CLASS
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [] 
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

#HAND CLASS






""" CARD CLASS TESTING """
# card = Card("Hearts", 10)
# print(card)