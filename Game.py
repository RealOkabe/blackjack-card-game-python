# from PyQt5 import QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import sys

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "22 Card Game"
        self.initUi()

    def initUi(self):
        # Create a window for everything
        self.setGeometry(400,400,500,500)
        self.setWindowTitle("22 Card Game") 
        
        # The label will prompt to enter the number of players
        self.label = QLabel(self)
        self.label.setText("Welcome to the 22 Card Game. How many people will be playing? ")
        self.label.adjustSize()
        self.label.move(20, 20)

        # The textbox will take input for the number of players
        self.textbox = QLineEdit(self)
        self.textbox.resize(70, 30)
        self.textbox.move(20, 50)

        # The button will confirm the prompt
        self.button = QPushButton("Confirm", self)
        self.button.move(10, 90)
        self.button.clicked.connect(self.getNumberOfPlayers)
        self.show()

    def getNumberOfPlayers(self):
        self.textBoxValue = self.textbox.text()
        self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    sys.exit(app.exec_())

# main() 