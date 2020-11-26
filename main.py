import sys
import random

from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor, QPolygon
from PyQt5.QtWidgets import QMainWindow, QApplication

SCREEN_SIZE = [800, 600]


class Circles(QMainWindow):
    def __init__(self):
        super(Circles, self).__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.create_circle.clicked.connect(self.do_paint_True)

    def do_paint_True(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        brush = QBrush(QColor('yellow'))
        r = random.randrange(1, (SCREEN_SIZE[0] - 200) // 2)
        x = random.randrange(50, SCREEN_SIZE[0] - 50)
        y = random.randrange(50, SCREEN_SIZE[1] - 50)
        qp.setBrush(brush)
        qp.drawEllipse(x - r // 2, y - r // 2, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Circles()
    wnd.show()
    sys.exit(app.exec())
