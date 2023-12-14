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

    def check22(self, hands):
        winners = []
        for i in hands:
            if self.getCardsSum(i) == 22:
                winners.append(i)
        return winners

    def checkWinner(self, hands):
        sums = {}
        for i in hands:
            sums[i] = self.getCardsSum(i)
        maxHand = max(sums.values())
        return [x for x in sums.keys() if sums[x] == maxHand]


        


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
        firstTurn = True
        winners = []
        while not self.deck.is_empty() and not winners:
            if firstTurn:
                self.deck.deal(self.hands, 2)
                firstTurn = False
                i = 0
                while i < len(self.hands):
                    print(self.hands[i])
                    if self.eliminatePlayer(self.hands[i]):
                        print(f"{self.hands[i].name} has been eliminated because their total exceeded 22")
                        self.hands.pop(i)
                        i = i - 1
                    i = i + 1
                winners = self.check22(self.hands)
            if winners:
                break
            passCount = 0
            turnNumber = 0
            while turnNumber < len(self.hands):
                passOrPick = input(f"It\'s {self.hands[turnNumber].name}\'s turn now. {self.hands[turnNumber].name} would you like to pick a card? Answer \'yes\' or \'no\': ").lower()
                if passOrPick == 'no':
                    passCount = passCount + 1
                elif passOrPick == 'yes':
                    self.deck.deal(self.hands[turnNumber:turnNumber + 1], 1)
                    print(self.hands[turnNumber])
                    if self.eliminatePlayer(self.hands[turnNumber]):
                        print(f"{self.hands[turnNumber].name} has been eliminated because their total exceeded 22")
                        self.hands.pop(turnNumber)
                        turnNumber = turnNumber - 1
                    winners = self.check22(self.hands)
                else:
                    continue
                if passCount == len(self.hands):
                    winners = self.checkWinner(self.hands)
                if len(self.hands) == 1:
                    winners = self.hands
                    break
                turnNumber = turnNumber + 1

        print("Someone has won the game")

if __name__ == '__main__':
    game = Game()
    game.cardGame22()
