import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication, QGridLayout, QLabel)


class SignalSlotExample(QWidget):

    def __init__(self):
        super().__init__()
        self.initInterface()

    def initInterface(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Orientation.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Signal and slot')
        self.show()


class EventHandleSample(QWidget):
    def __init__(self):
        super().__init__()
        self.initInterface()

    def initInterface(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape.value:
            self.close()


class MouseEventSample(QWidget):
    def __init__(self):
        super().__init__()
        self.text = None
        self.label = None
        self.initInterface()

    def initInterface(self):
        grid = QGridLayout()

        x = 0
        y = 0

        self.text = f'x: {x},  y: {y}'
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignmentFlag.AlignTop)

        self.setMouseTracking(True)
        self.setLayout(grid)

        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self, event):
        x = int(event.position().x())
        y = int(event.position().y())

        text = f'x:{x}, y:{y}'
        self.label.setText(text)


def main():
    app = QApplication(sys.argv)
    # ex = SignalSlotExample()
    # event = EventHandleSample()
    mouse = MouseEventSample()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
