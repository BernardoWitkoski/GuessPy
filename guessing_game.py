import random
import speech_recognition as sr
from PyQt5 import QtCore, QtGui, QtWidgets

class GuessingGame(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
        self.setWindowIcon(QtGui.QIcon('icone.png'))
        pixmap = QtGui.QPixmap('fundo.png')
        background = QtWidgets.QLabel(self)
        background.setPixmap(pixmap)
        background.setGeometry(0, 0, self.width(), self.height())
        
        self.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: black;
            }
            QPushButton {
                background-color: #00bfff;
                color: white;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
            }
            QLineEdit {
                font-size: 18px;
                font-weight: bold;
                background-color: #e6e6e6;
                border-radius: 5px;
                padding: 5px;
                color: black;
            }
        """)


    def initUI(self):
        self.setWindowTitle('Jogo de Adivinhação')
        self.setGeometry(200, 200, 600, 400)

        self.label = QtWidgets.QLabel('Pense em um número de 0 a 100', self)
        self.label.setGeometry(QtCore.QRect(133, 20, 400, 30))

        self.button = QtWidgets.QPushButton('Falar', self)
        self.button.setGeometry(QtCore.QRect(250, 60, 100, 30))
        self.button.clicked.connect(self.speak)

        self.textbox = QtWidgets.QLineEdit(self)
        self.textbox.setGeometry(QtCore.QRect(250, 100, 100, 30))
        self.textbox.setReadOnly(True)

        self.show()

    def speak(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                guess = int(r.recognize_google(audio, language='pt-BR'))
                if guess < self.number:
                    self.label.setText('O número é maior')
                elif guess > self.number:
                    self.label.setText('O número é menor')
                else:
                    self.label.setText('Você acertou!')
                self.textbox.setText(str(guess))
            except:
                self.label.setText('Não entendi, tente novamente')
                self.label.setGeometry(QtCore.QRect(130, 20, 200, 30))
                self.label.setStyleSheet("border: 1px solid black;")

    def start_game(self):
        self.number = random.randint(0, 100)
        self.label.setText('Pense em um número de 0 a 100')
        self.textbox.clear()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    game = GuessingGame()
    game.start_game()
    app.exec_()
