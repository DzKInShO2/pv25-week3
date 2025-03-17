import sys

from random import randint

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel
)


class MovingLabel(QLabel):
    def __init__(self, text, parent):
        super().__init__(text, parent)

        # Variabel screenWidth dan screenHeight di pake untuk kalkulasi
        # batasan posisi random yang akan di produksi
        self.screenWidth = 640
        self.screenHeight = 640

        # Minimum Width di set supaya label ndak ke clip
        self.setMinimumWidth(72)
        self.setMouseTracking(True)

    # Setiap kali cursor bergerak ke atas label maka fokus dari widget Window
    # bakal berubah ke label. Jadi event mouseMoveEvent dari Window bakal
    # berhenti ke trigger dan event mouseMoveEvent dari label yang akan ke trigger.
    # Hal ini bisa di mamfaatkan untuk mendeteksi apakah cursor overlap dengan label.
    def mouseMoveEvent(self, e):
        x = randint(0, self.screenWidth - self.width())
        y = randint(0, self.screenHeight - self.height())

        self.move(x, y)


class MynWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.__init_ui()

    def __init_ui(self):
        self.setWindowTitle("Task Week 3 - (F1D02310110 - Dzakanov Inshoofi)")
        # self.setFixedSize(640, 640)
        self.setGeometry(0, 0, 640, 640)

        self.setMouseTracking(True)
        self.label = MovingLabel("x: 0 y: 0", self)

    # Gambar posisi cursor pada label
    def mouseMoveEvent(self, e):
        self.label.setText(f"x: {e.x()} y: {e.y()}")

    # Resize event digunakan untuk memperbarui batasan posisi random label
    # setelah window di resize.
    def resizeEvent(self, e):
        self.label.screenWidth = e.size().width()
        self.label.screenHeight = e.size().height()


if __name__ == "__main__":
    app = QApplication([])

    win = MynWindow()
    win.show()

    sys.exit(app.exec())
