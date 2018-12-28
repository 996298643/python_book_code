from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow)  :
    def __init__(self, *args, **kwargs) :
       
       super().__init__(*args, **kwargs)
       
       self.setWindowTitle("第一个python qt")
       
       label = QLabel("weicome")
       label.setAlignment(Qt.AlignCenter)
       self.setCentralWidget(label)


app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec_()