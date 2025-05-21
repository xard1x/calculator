from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication([]) # создание окна
win = QWidget()
win.setWindowTitle('Калькулятор') 
win.setMinimumSize(300, 500)
win.setMaximumSize(300, 500)

win.show()
app.exec()