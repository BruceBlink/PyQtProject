from PyQt6.QtWidgets import QApplication, QWidget

import sys

app = QApplication(sys.argv)
# app = QApplication([])
window = QWidget()
window.show()
app.exec()