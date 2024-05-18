#!/usr/bin/python
# file: simple.py

"""
ZetCode PyQt6 tutorial

In this example, we create a simple
window in PyQt6.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QToolTip, QPushButton, QMessageBox, QMainWindow, QMenu
from PyQt6.QtGui import QFont, QAction, QIcon


class HelloWorld(QWidget):
    def __init__(self):
        super().__init__()
        self.initInterface()

    def initInterface(self):
        self.setGeometry(300, 300, 280, 80)
        self.setWindowTitle('Simple')
        helloMsg = QLabel("<h1>Hello, World!</h1>", parent=self)
        helloMsg.move(60, 15)
        self.show()


class ToolTip(QWidget):
    def __init__(self):
        super().__init__()
        self.initInterface()

    def initInterface(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


class QuitButton(QWidget):
    def __init__(self):
        super().__init__()
        self.initInterface()

    def initInterface(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())  # 这行代码可以不需要
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Quit button')
        self.show()


class MessageBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initInterface()

    def initInterface(self):
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


class CenterScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initInterface()

    def initInterface(self):
        self.resize(350, 250)
        self.setCenter()
        self.setWindowTitle('Center')
        self.show()

    def setCenter(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class StateBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initInterface()

    def initInterface(self):
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Statusbar')
        self.show()


class SimpleMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initInterface()

    def initInterface(self):
        exit_action = QAction(QIcon('exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(QApplication.instance().quit)  # 这里传入的是一个函数（quit）作为参数，而不是调用这个函数

        self.statusBar()

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_action)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Simple menu')
        self.show()


class SimpleSubMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initInterface()

    def initInterface(self):
        menu_bar = self.menuBar()
        fileMenu = menu_bar.addMenu('File')

        imp_menu = QMenu('Import', self)
        imp_action = QAction('Import mail', self)
        imp_menu.addAction(imp_action)

        new_action = QAction('New', self)
        fileMenu.addAction(new_action)
        fileMenu.addMenu(imp_menu)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Submenu')
        self.show()


class SimpleCheckMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.status_bar = self.statusBar()
        self.initInterface()

    def initInterface(self):
        self.status_bar.showMessage('Ready')

        menu_bar = self.menuBar()
        view_menu = menu_bar.addMenu('View')

        view_state_action = QAction('View statusbar', self, checkable=True)
        view_state_action.setStatusTip('View statusbar')
        view_state_action.setChecked(True)
        view_state_action.triggered.connect(self.toggleMenu)

        view_menu.addAction(view_state_action)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Check menu')
        self.show()

    def toggleMenu(self, state):
        if state:
            self.status_bar.show()
        else:
            self.status_bar.hide()


def main():
    app = QApplication(sys.argv)
    # hello = HelloWorld()
    # tool = ToolTip()
    # quit_button = QuitButton()
    # message_box = MessageBox()
    # center_screen = CenterScreen()
    # state_bar = StateBar()
    # simple = SimpleMenu()
    # simple_sub_ment = SimpleSubMenu()
    simple_check_menu = SimpleCheckMenu()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
