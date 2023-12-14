from Card import Card
import random

# class for deck of cards
class Deck:

# constructor for deck class
  def __init__(self,n_cards):
    self.cards = []   # list of cards
    for suit in range(4): # 4 suits
      for rank in range(1,14):
        self.cards.append(Card(suit,rank))

# string representation of deck
  def __str__(self):
    s = ""

    for i in range(len(self.cards)): 
      s = s + i* " " + str(self.cards[i]) + "\n"  # add each card to string
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
    for i in range(n_cards*2):
      if self.is_empty():   # if deck is empty,
        break            # break out of loop
      card = self.pop_cards()   # remove card from deck
      current_player = i % n_players
      hands[current_player].add_card(card)  # add card to hand