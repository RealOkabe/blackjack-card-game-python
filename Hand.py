from Deck import Deck

# Inherits from Deck class
class Hand(Deck):

# constructor for Hand class
  def __init__(self, name = ""):
    self.cards = []
    self.name = name

# add card to hand
  def add_card(self, card):
    self.cards.append(card)

# string representation of hand
  def __str__(self):

    s = ("Hand of ") + self.name

    if self.is_empty():
      return s + " is empty"

    s += " contains \n" + Deck.__str__(self)
    return s

