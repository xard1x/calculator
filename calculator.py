from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication([])
win = QWidget()
win.setWindowTitle('Калькулятор') 
win.setMinimumSize(300, 350)
win.setMaximumSize(300, 450)

main_layout = QVBoxLayout()

global label
label = QLabel('')
label.setFont(QFont('Arial', 30))
lay1 = QHBoxLayout()
lay1.addWidget(label, alignment= Qt.AlignLeft)
main_layout.addLayout(lay1)

but_proc = QPushButton('%')
but_proc.setFont(QFont('Arial', 15))
but_c = QPushButton('C')
but_c.setFont(QFont('Arial', 15))
but_del = QPushButton('DEL')
but_del.setFont(QFont('Arial', 15))
lay2 = QHBoxLayout()
lay2.addWidget(but_proc)
lay2.addWidget(but_c)
lay2.addWidget(but_del)
main_layout.addLayout(lay2)

but_x2 = QPushButton('x^2')
but_x2.setFont(QFont('Arial', 15))
but_kor = QPushButton('√x')
but_kor.setFont(QFont('Arial', 15))
but_razdel = QPushButton('÷')
but_razdel.setFont(QFont('Arial', 15))
lay3 = QHBoxLayout()
lay3.addWidget(but_x2)
lay3.addWidget(but_kor)
lay3.addWidget(but_razdel)
main_layout.addLayout(lay3)

but_7 = QPushButton('7')
but_7.setFont(QFont('Arial', 15))
but_8 = QPushButton('8')
but_8.setFont(QFont('Arial', 15))
but_9 = QPushButton('9')
but_9.setFont(QFont('Arial', 15))
but_umn = QPushButton('×')
but_umn.setFont(QFont('Arial', 15))
lay4 = QHBoxLayout()
lay4.addWidget(but_7)
lay4.addWidget(but_8)
lay4.addWidget(but_9)
lay4.addWidget(but_umn)
main_layout.addLayout(lay4)

but_4 = QPushButton('4')
but_4.setFont(QFont('Arial', 15))
but_5 = QPushButton('5')
but_5.setFont(QFont('Arial', 15))
but_6 = QPushButton('6')
but_6.setFont(QFont('Arial', 15))
but_minus = QPushButton('-')
but_minus.setFont(QFont('Arial', 15))
lay5 = QHBoxLayout()
lay5.addWidget(but_4)
lay5.addWidget(but_5)
lay5.addWidget(but_6)
lay5.addWidget(but_minus)
main_layout.addLayout(lay5)

but_1 = QPushButton('1')
but_1.setFont(QFont('Arial', 15))
but_2 = QPushButton('2')
but_2.setFont(QFont('Arial', 15))
but_3 = QPushButton('3')
but_3.setFont(QFont('Arial', 15))
but_plus = QPushButton('+')
but_plus.setFont(QFont('Arial', 15))
lay6 = QHBoxLayout()
lay6.addWidget(but_1)
lay6.addWidget(but_2)
lay6.addWidget(but_3)
lay6.addWidget(but_plus)
main_layout.addLayout(lay6)

but_nt = QPushButton('NXT')
but_nt.setFont(QFont('Arial', 15))
but_0 = QPushButton('0')
but_0.setFont(QFont('Arial', 15))
but_ravno = QPushButton('=')
but_ravno.setFont(QFont('Arial', 15))
lay7 = QHBoxLayout()
lay7.addWidget(but_nt)
lay7.addWidget(but_0)
lay7.addWidget(but_ravno)
main_layout.addLayout(lay7)

global num1
num1 = '' 

global num2
num2 = '' 

global phase
phase = 1

global action
action = ''

def number(a):
    global phase
    global label
    global num1
    global num2
    if phase == 1:    
        if num1 == '':
            num1 = a
            label.setText(str(num1))
        else:
            num1 += a
            label.setText(str(num1))
            if len(num1) >= 7:
                num1 = num1[:-1]
                label.setText(str(num1))
    if phase == 2:    
        if num2 == '':
            num2 = a
            label.setText(str(num2))
        else:
            num2 += a
            label.setText(str(num2))
            if len(num2) >= 7:
                num2 = num2[:-1]
                label.setText(str(num2))
def one():
    number('1')
def two():
    number('2')
def three():
    number('3')
def four():
    number('4')
def five():
    number('5')
def six():
    number('6')
def seven():
    number('7')
def eight():
    number('8')
def nine():
    number('9')
def zero():
    number('0')
def delete():
    global phase
    global label
    global num1
    global num2
    if phase == 1:    
        num1 = num1[:-1]
        label.setText(str(num1))
    if phase == 2:
        num2 = num2[:-1]
        label.setText(str(num1))    
def plus():
    global phase
    phase = 2
    global action
    action = 'plus'
    label.setText('')
def ravno():
    global num2
    global num1
    global phase
    global result
    phase = 1
    if action == 'plus':
        if num1 == '': 
            num1 = 0
        if num2 == '': 
            num2 = 0
        result = int(num1) + int(num2)
        label.setText(str(result))
        num1 = ''
        num2 = ''
    if action == 'minus':
        if num1 == '': 
            num1 = 0
        if num2 == '': 
            num2 = 0
        result = int(num1) - int(num2)
        label.setText(str(result))
        num1 = ''
        num2 = ''
    if action == 'umnojenie':
        if num1 == '': 
            num1 = 0
        if num2 == '': 
            num2 = 0
        result = int(num1) * int(num2)
        label.setText(str(result))
        num1 = ''
        num2 = ''
    if action == 'delenie':
        if num1 == '': 
            num1 = 0
        if num2 == '': 
            num2 = 1
        if num2 == '0': 
            num2 = 1
        result = int(num1) / int(num2)
        label.setText(str(result))
        num1 = ''
        num2 = ''
    if action == 'stepen':
        if num1 == '': 
            num1 = 0
        result = int(num1) ** 2
        label.setText(str(result))
        num1 = ''
    if action == 'koren':
        if num1 == '': 
            num1 = 0
        if int(num1) < 0:
            num1 = int(num1) * -1
        num1 = int(num1) ** 0.5
        label.setText(str(num1))
    if action == 'procent':
        if num1 == '': 
            num1 = 0
        if num2 == '': 
            num2 = 0
        result = (int(num1) * int(num2)) / 100
        label.setText(str(result))
        num1 = ''
        num2 = ''

def minus():
    global phase
    phase = 2
    global action
    action = 'minus'
    label.setText('')
def umnojenie():
    global phase
    phase = 2
    global action
    action = 'umnojenie'
    label.setText('')       
def delenie():
    global phase
    phase = 2
    global action
    action = 'delenie'
    label.setText('') 
def stepen():
    global action
    action = 'stepen'
    ravno()
def koren():
    global action
    action = 'koren'
    ravno()
def nxt():
    global result
    global num1
    num1 = result
    label.setText(str(num1))
    
    
def c():
    global num1
    global num2
    global phase
    num1 = ''
    num2 = ''
    phase = 1 
    label.setText('')
def procent():
    global phase
    phase = 2
    global action
    action = 'procent'
    label.setText('')
    

but_1.clicked.connect(one)
but_2.clicked.connect(two)
but_3.clicked.connect(three)
but_4.clicked.connect(four)
but_5.clicked.connect(five)
but_6.clicked.connect(six)
but_7.clicked.connect(seven)
but_8.clicked.connect(eight)
but_9.clicked.connect(nine)
but_0.clicked.connect(zero)
but_del.clicked.connect(delete)
but_plus.clicked.connect(plus)
but_minus.clicked.connect(minus)
but_umn.clicked.connect(umnojenie)
but_razdel.clicked.connect(delenie)
but_x2.clicked.connect(stepen)
but_kor.clicked.connect(koren)
but_nt.clicked.connect(nxt)
but_c.clicked.connect(c)
but_proc.clicked.connect(procent)
but_ravno.clicked.connect(ravno)

win.setLayout(main_layout)
win.show()
app.exec()