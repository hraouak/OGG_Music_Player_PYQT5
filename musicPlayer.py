from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import os
import sys
from mainWindow import Ui_Dialog
global song_played


pygame.init()
pygame.mixer.init()

directory = os.getcwd()
os.chdir(directory)
song_list = os.listdir()


def Clicked():
    global song_played
    _translate = QtCore.QCoreApplication.translate
    Dialog.setWindowTitle(_translate("Dialog", ui.listWidget.currentItem().text()))
    pygame.mixer.music.load(ui.listWidget.currentItem().text()+".ogg")
    song_played = False

def play():
    global song_played
    if song_played == False:
        pygame.mixer.music.play()
        song_played = True
    else:
        pygame.mixer.music.unpause()

def stop():
    pygame.mixer.music.stop()
    song_played = False

def pause():
    pygame.mixer.music.pause()

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

for item in song_list:
    if item.endswith(".ogg"):
        ui.listWidget.addItem(os.path.splitext(item)[0])
    ui.listWidget.sortItems()

ui.listWidget.itemClicked.connect(Clicked)
ui.Play.clicked.connect(play)
ui.Pause.clicked.connect(pause)
ui.Stop.clicked.connect(stop)

sys.exit(app.exec_())
