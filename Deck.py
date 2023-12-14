from Card import Card
import random

# class for deck of cards
class Deck:

# constructor for deck class
  def __init__(self):
    self.cards = []   # list of cards
    for suit in range(4): # 4 suits
      for rank in range(1,14):
        self.cards.append(Card(suit,rank))

# string representation of deck
  def __str__(self):
    s = ""

    for i in range(len(self.cards)): 
      s = s + str(self.cards[i]) + "\n"  # add each card to string
    return s

# shuffle the deck
  def shuffle(self):
    n_cards = len(self.cards)
    for i in range(n_cards):
      j = random.randrange(0, n_cards)
      self.cards[i] , self.cards[j] = self.cards[j] , self.cards[i]   # swap cards

#  Remove and return the top card
  def pop_cards(self):
    return self.cards.pop()     # remove last card

# Check if deck is empty
  def is_empty(self):
    return len(self.cards) == 0   # return true if deck is empty

# Deal cards to hands
  def deal(self, hands, n_cards):
    n_players = len(hands)
    for i in hands:
      if self.is_empty():
        break
      for j in range(0, n_cards):
        i.add_card(self.pop_cards())