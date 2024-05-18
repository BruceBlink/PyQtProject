import sys
from PyQt6.QtWidgets import QLabel, QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout


class AbsolutionPosition(QWidget):

    def __init__(self):
        super().__init__()
        self.initInterface()

    def initInterface(self):
        lbl1 = QLabel('ZetCode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Absolute')
        self.show()


class HVLayoutSample(QWidget):
    def __init__(self):
        super().__init__()
        self.initInterface()

    def initInterface(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Buttons')
        self.show()


class GridLayoutSample(QWidget):
    def __init__(self):
        super().__init__()
        self.initInterface()

    def initInterface(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


def main():
    app = QApplication(sys.argv)
    # absolution_position = AbsolutionPosition()
    # layout = HVLayoutSample()
    grid_layout = GridLayoutSample()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
