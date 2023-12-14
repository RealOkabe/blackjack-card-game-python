from Card import Card
from Deck import Deck
from Hand import Hand

class Game:
    def cardGame22(self):
        self.deck = Deck()
        self.deck.shuffle()
        startGame = False
        while not startGame:
            noOfPlayers = input("Welcome to the 22 Card Game. How many people will be playing? Please enter a number between 2 and 12: ")
            try:
                noOfPlayers = int(noOfPlayers)
                if noOfPlayers not in range(2, 13):
                    raise Exception("More than enough or not enough players")
                startGame = True
            except:
                continue
        hands = [Hand()] * noOfPlayers
        for i in range(0, noOfPlayers):
            hands[i].name = f"Player {i + 1}"
        


if __name__ == '__main__':
    game = Game()
    game.cardGame22()