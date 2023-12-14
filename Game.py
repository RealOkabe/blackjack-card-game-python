from Card import Card
from Deck import Deck
from Hand import Hand
import copy

class Game:
    def eliminatePlayer(self, hand):
        sum = 0
        for i in hand.cards:
            if i.rank == "Jack":
                sum = sum + 11
            elif i.rank == "Queen":
                sum = sum + 12
            elif i.rank == "King":
                sum = sum + 13
            elif i.rank == "Ace":
                sum = sum + 1
            else:
                sum = sum + int(i.rank)
        if sum > 22:
            return True
        return False

    def cardGame22(self):
        self.deck = Deck()
        self.deck.shuffle()
        startGame = False
        while not startGame:
            self.noOfPlayers = input("Welcome to the 22 Card Game. How many people will be playing? Please enter a number between 2 and 12: ")
            try:
                self.noOfPlayers = int(self.noOfPlayers)
                if self.noOfPlayers not in range(2, 13):
                    raise Exception("More than enough or not enough players")
                startGame = True
            except:
                continue
        self.hands = [Hand() for _ in range(self.noOfPlayers)]
        for i in range(0, self.noOfPlayers):
            self.hands[i].name = f"Player {i + 1}"
        winner = None
        firstTurn = True
        while not self.deck.is_empty() and not winner:
            if firstTurn:
                self.deck.deal(self.hands, 2)
                for i in self.hands:
                    print(i)
                for i in self.hands:
                    if self.eliminatePlayer(i):
                        print(f"{i.name} has been eliminated because their total exceeded 22")
                        hands.pop(i)
            winner = True

        


if __name__ == '__main__':
    game = Game()
    game.cardGame22()