import sys

from random import randint

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel
)


class MovingLabel(QLabel):
    def __init__(self, parent):
        super().__init__(parent)

        self.screenWidth = 640
        self.screenHeight = 640
        self.setMouseTracking(True)

    def mouseMoveEvent(self, e):
        x = randint(0, self.screenWidth - 50)
        y = randint(10, self.screenHeight - 10)

        self.move(x, y)


class MynWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.__init_ui()

    def __init_ui(self):
        self.setWindowTitle("Task Week 3 - (F1D02310110 - Dzakanov Inshoofi)")
        self.setFixedSize(640, 640)
        # self.setGeometry(0, 0, 640, 640)

        self.setMouseTracking(True)
        self.label = MovingLabel(self)
        self.label.setText("x: 10 y: 10 Starting Point")
        self.label.move(10, 10)

    def mouseMoveEvent(self, e):
        self.label.setText(f"x: {e.x()} y: {e.y()}")

    def resizeEvent(self, e):
        self.label.screenWidth = e.size().width()
        self.label.screenHeight = e.size().height()


if __name__ == "__main__":
    app = QApplication([])

    win = MynWindow()
    win.show()

    sys.exit(app.exec())
