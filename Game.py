from Card import Card
from Deck import Deck
from Hand import Hand
import copy

class Game:

    def getCardsSum(self, hand):
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
        return sum
    
    def eliminatePlayer(self, hand):
        return self.getCardsSum(hand) > 22

    # def checkWinner(self, hands):


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
                firstTurn = False
                for i in self.hands:
                    print(i)
                    if self.eliminatePlayer(i):
                        print(f"{i.name} has been eliminated because their total exceeded 22")
                        self.hands.pop(i)
            for i in range(0, self.noOfPlayers):
                passOrPick = input(f"It\'s {self.hands[i].name}\'s turn now. {self.hands[i].name} would you like to pick a card? Answer \'yes\' or \'no\': ").lower()
                if passOrPick == 'no':
                    continue
                elif passOrPick == 'yes':
                    self.deck.deal(self.hands[i:i + 1], 1)
                    print(self.hands[i])
                    if self.eliminatePlayer(self.hands[i]):
                        print(f"{self.hands[i].name} has been eliminated because their total exceeded 22")
                        self.hands.pop(self.hands[i])
                else:
                    break

        


if __name__ == '__main__':
    game = Game()
    game.cardGame22()