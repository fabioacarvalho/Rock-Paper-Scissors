import sys
import random
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui


ppt = ['Rock', 'Paper', 'Scissors']

game = []

def aChoice():
    esc = random.choice(ppt)
    game.append(esc)


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.windowStart.setPixmap(QtGui.QPixmap('./img/pptHome.png'))

        #self.stackedWidget.setCurrentWidget(self.page_1)
        #self.btnAddRegiao.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))

        self.btnRestart.clicked.connect(self.restart)
        self.btnRock.clicked.connect(self.rock)
        self.btnPaper.clicked.connect(self.paper)
        self.btnScissors.clicked.connect(self.scissors)
    
    def restart(self):
        self.stackedWidget.setCurrentWidget(self.page_1)
        game.clear()
        self.computador.setPixmap(QtGui.QPixmap(''))
        self.player.setPixmap(QtGui.QPixmap(''))
        self.infoText.setText('')
    
    

    def rock(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.player.setPixmap(QtGui.QPixmap('./img/rock.png'))

        game.append('Rock')
        aChoice()

        if game[1] == 'Rock':
            self.computador.setPixmap(QtGui.QPixmap('./img/rock.png'))
            self.infoText.setText('Nobody won, play again.')
        if game[1] == 'Paper':
            self.computador.setPixmap(QtGui.QPixmap('./img/paper.png'))
            self.infoText.setText('You lost, try again :(')
            self.infoText.setStyleSheet('color: #ffaa00; font: 20pt \"MS Shell Dlg 2\";\n')
        if game[1] == 'Scissors':
            self.computador.setPixmap(QtGui.QPixmap('./img/scissors.png'))
            self.infoText.setText('You win, congratulations!!! :)')
            self.infoText.setStyleSheet('color: rgb(85, 255, 127); font: 20pt \"MS Shell Dlg 2\";\n')

    def paper(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.player.setPixmap(QtGui.QPixmap('./img/paper.png'))

        game.append('Paper')
        aChoice()

        if game[1] == 'Paper':
            self.computador.setPixmap(QtGui.QPixmap('./img/paper.png'))
            self.infoText.setText('Nobody won, play again.')
        if game[1] == 'Scissors':
            self.computador.setPixmap(QtGui.QPixmap('./img/scissors.png'))
            self.infoText.setText('You lost, try again :(')
            self.infoText.setStyleSheet('color: #ffaa00; font: 20pt \"MS Shell Dlg 2\";\n')
        if game[1] == 'Rock':
            self.computador.setPixmap(QtGui.QPixmap('./img/rock.png'))
            self.infoText.setText('You win, congratulations!!! :)')
            self.infoText.setStyleSheet('color: rgb(85, 255, 127); font: 20pt \"MS Shell Dlg 2\";\n')

    def scissors(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.player.setPixmap(QtGui.QPixmap('./img/scissors.png'))

        game.append('Scissors')
        aChoice()

        if game[1] == 'Scissors':
            self.computador.setPixmap(QtGui.QPixmap('./img/scissors.png'))
            self.infoText.setText('Nobody won, play again.')
        if game[1] == 'Rock':
            self.computador.setPixmap(QtGui.QPixmap('./img/rock.png'))
            self.infoText.setText('You lost, try again :(')
            self.infoText.setStyleSheet('color: #ffaa00; font: 20pt \"MS Shell Dlg 2\";\n')
        if game[1] == 'Paper':
            self.computador.setPixmap(QtGui.QPixmap('./img/paper.png'))
            self.infoText.setText('You win, congratulations!!! :)')
            self.infoText.setStyleSheet('color: rgb(85, 255, 127); font: 20pt \"MS Shell Dlg 2\";\n')



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
