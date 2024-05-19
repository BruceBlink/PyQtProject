from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = True
        self.setWindowTitle("My app")

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)

        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)
        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
