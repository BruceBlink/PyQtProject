from PyQt6.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication)
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


def main():
    app = QApplication(sys.argv)
    ex = InputDialogSample()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
