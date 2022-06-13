import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)
        btn1 = QPushButton('BIG', self)
        btn2 = QPushButton('SMALL', self)

        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)



        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)
        btn1.clicked.connect(self.resizeBig)
        btn2.clicked.connect(self.resizeSmall)


        self.setGeometry(100, 100, 200, 300)
        self.show()

    def resizeBig(self):
        self.resize(400, 400)


    def resizeSmall(self):
        self.resize(150, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())