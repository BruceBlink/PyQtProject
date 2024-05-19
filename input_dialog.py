from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication, QFrame, QColorDialog, QLabel, QFontDialog, QSizePolicy,
                             QVBoxLayout)
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


class FontDialogSample(QWidget):
    def __init__(self):
        super().__init__()

        self.lbl = None
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.lbl.setFont(font)


def main():
    app = QApplication(sys.argv)
    # ex = InputDialogSample()
    # color = ColorDialogSample()
    font = FontDialogSample()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
