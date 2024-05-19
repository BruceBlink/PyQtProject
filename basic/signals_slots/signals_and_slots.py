from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My app")
        button = QPushButton("Press Me!")
        button.setChecked(True)
        # 给clicked 的signal添加slot the_button_was_clicked
        # 点击button后控制台会输出'Clicked'
        button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
