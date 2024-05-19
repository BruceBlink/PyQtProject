from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication, QFrame, QColorDialog)
import sys


class InputDialogSample(QWidget):

    def __init__(self):
        super().__init__()
        self.le = None
        self.btn = None
        self.initInterface()

    def initInterface(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')
        if ok:
            self.le.setText(str(text))


class ColorDialogSample(QWidget):
    def __init__(self):
        super().__init__()

        self.frm = None
        self.btn = None
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.frm.setGeometry(130, 22, 200, 200)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())


def main():
    app = QApplication(sys.argv)
    # ex = InputDialogSample()
    # color = ColorDialogSample()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
