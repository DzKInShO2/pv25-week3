import sys
import random

from PyQt5.QtCore import Qt;

from PyQt5.QtWidgets import (
    QApplication,
    QWidget
)


class MynWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Week 3 - (F1D02310110 - Dzakanov Inshoofi)")
        self.setFixedSize(640, 640)


if __name__ == "__main__":
    app = QApplication([])

    win = MynWindow()
    win.show()

    sys.exit(app.exec())
