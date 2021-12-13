import sys, random
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QPainterPath, QBrush, QPen
from PyQt5.QtCore import Qt


class Shape():
    def __init__(self, length, position, color, parent=None):
        self.color = color
        self.position = position
        self.length = length
        self.connections = {}

    def paint(self, painter):
        pass


class Ellipse(Shape):
    def paint(self, painter):
        painter.setPen(QPen(self.color,  2, Qt.SolidLine))
        painter.setBrush(QBrush(self.color))
        x, y = self.position.x(), self.position.y()
        painter.drawEllipse(x, y, self.length*2, self.length)
        self.connections.update({"Up": [], "Down": []})

    def get_area(self):
        x_end = self.position.x() + self.length*2
        y_end = self.position.y() + self.length
        area = [self.position.x(), self.position.y(), x_end, y_end]
        return area


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.shapes = []

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        for shape in self.shapes:
            shape.paint(painter)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            pos = QtCore.QPoint(event.pos().x()-45, event.pos().y()-25)
            length = 50
            color = QtGui.QColor(100, 100, 100)
            new_shape = Ellipse(length, pos, color)
            self.shapes.append(new_shape)

        elif event.button() == Qt.RightButton:
            x = event.pos().x()
            y = event.pos().y()
            for i in range(len(self.shapes)):
                area = self.shapes[i].get_area()
                if area[0] <= x <= area[2] and area[1] <= y <= area[3]:
                    self.shapes.pop(i)
                    break
        self.update()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())



