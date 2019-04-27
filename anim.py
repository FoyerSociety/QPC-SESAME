#-*-coding: utf-8 -*-
# __author__ Gaetan Jonathan

from PyQt5.QtCore import (Qt, QSize,QByteArray, pyqtSlot, pyqtSignal, QThread)
from PyQt5.QtGui import (QMovie)
from PyQt5.QtWidgets import (QApplication, QWidget,QSizePolicy,QVBoxLayout, QPushButton, QLabel, QGridLayout)

import threading
import time
import sys
import Interface

verification = False

class ImagePlayer(QWidget):
    def __init__(self, filename, parent=None):
        QWidget.__init__(self, parent)

        # charger le fichier dans QMovie
        self.movie = QMovie(filename, QByteArray(), self)

        size = self.movie.scaledSize()
        self.setGeometry(600, 340, size.width(), size.height())
        self.move(350, 125)
        self.setWindowTitle("QPC SESAME")

        self.movie_screen = QLabel()
        # mettre le label du gif 
        self.movie_screen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.movie_screen.setAlignment(Qt.AlignCenter)

        # Creation des layout 
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.movie_screen)

        self.setLayout(main_layout)

        # Add the QMovie object to the label
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.movie_screen.setMovie(self.movie)
        self.movie.start()  #  lancer le gif 


    def mousePressEvent(self, event):  #  fonction d evenement de touche de souris 
        if event.button() == Qt.LeftButton:  #  si  l evenement du click est click gauche
            
            thread_1.app.quit()   #  arrete l application 
        

    
class Launch(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        self.app = QApplication(sys.argv)
        gif = "load.gif"
        player = ImagePlayer(gif)
        player.show()
        sys.exit(self.app.exec_()) 



        
thread_1 = Launch()

thread_1.start()

time.sleep(20)
thread_1.app.quit()

 