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
        return self.getCardsSum(hand) >21

    def check21(self, hands):
        winners = []
        for i in hands:
            if self.getCardsSum(i) == 21:
                winners.append(i)
        return winners

    def checkWinner(self, hands):
        sums = {}
        for i in hands:
            sums[i] = self.getCardsSum(i)
            print(f"{i.name} has a score of {sums[i]}")
        maxHand = max(sums.values())
        return [x for x in sums.keys() if sums[x] == maxHand]


        


    def cardGameBlackjack(self):
        self.deck = Deck()
        self.deck.shuffle()
        startGame = False
        while not startGame:
            self.noOfPlayers = input("How many people will be playing? Please enter a number between 2 and 16: ")
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
        passCount = 0
        while not self.deck.is_empty() and not winners:
            if firstTurn:
                self.deck.deal(self.hands, 2)
                firstTurn = False
                i = 0
                while i < len(self.hands):
                    print(self.hands[i])
                    if self.eliminatePlayer(self.hands[i]):
                        print(f"{self.hands[i].name} has been eliminated because their total exceeded 21")
                        self.hands.pop(i)
                        i = i - 1
                    i = i + 1
                winners = self.check21(self.hands)
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
                        print(f"{self.hands[turnNumber].name} has been eliminated because their total exceeded 21")
                        self.hands.pop(turnNumber)
                        turnNumber = turnNumber - 1
                    winners = self.check21(self.hands)
                else:
                    continue
                if passCount == len(self.hands):
                    winners = self.checkWinner(self.hands)
                if len(self.hands) == 1:
                    winners = self.hands
                    break
                turnNumber = turnNumber + 1

        if len(self.hands) == 1:
            print(f"{self.hands[0].name} has won this round of Blackjack by default")
        elif passCount == len(self.hands):
            for i in winners:
                print(f"{i.name} has won this round of Blackjack for having the highest score")
        else:
            for i in winners:
                print(f"{i.name} has won this round of Blackjack because of having a score of 21")

if __name__ == '__main__':
    game = Game()
    playAgain = ""
    toPlay = True
    while toPlay:
        playerConsent = input(f"""Hello and welcome to Blackjack.
Here is an overview of the game:
1. You will be dealt two cards each when the game begins.
2. If the total of your cards\' ranks exceeds 21, you are eliminated from the game. If the total is 21, you win the game.
3. If no one has cards whose ranks total 21, then the game continues.
4. Everyone will be asked if they want to pick a card from the deck or pass.
5. If someone picks a card and their new total exceeds 21, they get eliminated.
6. If everyone passes a turn, then the winner is decided by comparing the total of ranks. The highest total wins.
7. If someone manages to get a total of 21 by picking a card, they win.
8. If everyone gets eliminated and one player remains, the remaining player wins by default.
Would you like to play{playAgain}? Answer \'Yes\' or \'No\': """)
        if playerConsent.lower() == 'yes':
            game.cardGameBlackjack()
        elif playerConsent.lower() == 'no':
            print("Thank you. This game was brought to you by Anmol Agrawal.")
            exit(0)
        else:
            continue
        playAgain = " again"
