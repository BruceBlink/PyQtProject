from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = False
        self.setWindowTitle("My app")
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        # 给clicked 的signal添加slot the_button_was_clicked
        # 点击button后控制台会输出'Clicked'
        # button.clicked.connect(self.the_button_was_clicked)
        # 添加 toggled的信号槽传递checked状态
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)
        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(self.button_is_checked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
