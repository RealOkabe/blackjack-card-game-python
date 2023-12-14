import random

# class for single card
class Card:
  
  suit_list = ["♧", "♢", "♡", "♤"] # Four suits in a deck
  rank_list = ["None","Ace","2", "3","4","5","6","7","8","9","10","Jack","Queen","King"] # 13 ranks in a deck

# constructor for card class
  def __init__(self,suit=0, rank = 2):
    self.suit = suit 
    self.rank = rank

# string representation of card
  def __str__(self):
    cardRank = "|" + self.rank_list[self.rank].ljust(9) + self.rank_list[self.rank].rjust(9) + "|"
    return f"""
    +------------------+
    {cardRank}
    |{self.suit_list[self.suit]}                {self.suit_list[self.suit]}|
    |                  |
    |                  |
    |                  |
    |                  |
    |                  |
    |                  |
    |                  |
    |{self.suit_list[self.suit]}                {self.suit_list[self.suit]}|
    {cardRank}
    +------------------+
    """
    # return (self.rank_list[self.rank] + " of " + self.suit_list[self.suit])

# compare two cards for equality
  def __eq__(self, other) -> bool:
    return (self.rank == other.rank and self.suit == other.suit)

# compare two cards for greater than
  def __gt__(self, other):

    # First check if the suits are same or grater and then check for rank
    if self.suit > other.suit:
      return True

    elif self.suit == other.suit:
      if self.rank > other.rank:
        return True

    return False
  