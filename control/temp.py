import sys

from PyQt5.Qt import *
from PyQt5.QtWidgets import *


class MyLabel(QLabel):

    def __init__(self, parent):
        super(MyLabel, self).__init__()
        self.pressed_pos = object
        self.setParent(parent)

    movedSiganl = pyqtSignal([object])

    def mousePressEvent(self, e):
        super(MyLabel, self).mousePressEvent(e)
        self.pressed_pos = e.pos()

    def mouseMoveEvent(self, e):
        super(MyLabel, self).mouseMoveEvent(e)
        x = e.pos().x() - self.pressed_pos.x()
        y = e.pos().y() - self.pressed_pos.y()
        self.move(self.mapToParent(QPoint(x, y)))
        self.movedSiganl[object].emit(e.pos())


class MyUi(QWidget):
    def __init__(self):
        super(MyUi, self).__init__()
        self.setupUI()
        self.resize(1000, 1000)
        self.label = 0
        self.label_list = []

    def setupUI(self):
        label = MyLabel(self)
        label.setStyleSheet("""
        background-color:red;
        """)
        label.resize(50, 50)
        label.move(100, 100)
        label.movedSiganl.connect(lambda pos: self.moved_lk(pos))

    def moved_lk(self, pos):
        label = QLabel(str(self.label + 1), self)

        self.label_list.append(label)
        label.setStyleSheet("""
        background-color:green;
        """)
        label.resize(25, 25)
        # label.show()
        # label.move(label.mapToParent(QPoint(self.label * 25, self.label * 25)))
        self.label += 1

    def mouseReleaseEvent(self, e):
        self.label_list[0].raise_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyUi()
    main.show()
    sys.exit(app.exec_())
