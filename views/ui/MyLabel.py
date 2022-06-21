import sys
import time

from PyQt5.QtWidgets import QLabel
from PyQt5.Qt import *


class MyLabel(QLabel):
    mouseReleased = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)
        self.iniDragCor = [0, 0]

    def mousePressEvent(self, e):
        # print("ppp", e.pos())
        self.iniDragCor[0] = e.x()
        self.iniDragCor[1] = e.y()

    def mouseMoveEvent(self, e):
        x = e.x() - self.iniDragCor[0]
        y = e.y() - self.iniDragCor[1]
        # print(self.iniDragCor[0], self.iniDragCor[1])
        cor = QPoint(x, y)
        # self.move(cor)
        self.move(self.mapToParent(cor))  # 需要maptoparent一下才可以的,否则只是相对位置。

        # print('drag button event,', time.time(), e.pos(), e.x(), e.y())

    def mouseReleaseEvent(self, e):
        self.mouseReleased.emit()


class syringe_label(MyLabel):
    def __init__(self, parent):
        super(syringe_label, self).__init__(parent)
        self.old_pos = False

    syringe_label_moved = pyqtSignal([object])

    def mouseMoveEvent(self, e):
        x = e.x() - self.iniDragCor[0]
        y = e.y() - self.iniDragCor[1]
        if self.old_pos.x() >= self.pos().x() and x < 0:
            e.ignore()
            return
        if self.pos().x() >= 730 and x > 0:
            e.ignore()
            return
        if x > 0 and y < 0:
            distance = abs(x) if abs(x) < abs(y) else abs(y)

            distance = QPoint(distance, -distance)

            self.move(self.mapToParent(distance))
            self.syringe_label_moved.emit(distance)
        if x < 0 and y > 0:
            distance = abs(x) if abs(x) < abs(y) else abs(y)

            distance = QPoint(-distance, distance)

            self.syringe_label_moved.emit(distance)
            self.move(self.mapToParent(distance))

    def mousePressEvent(self, e):
        super(syringe_label, self).mousePressEvent(e)
        if not self.old_pos:
            self.old_pos = self.pos()


class Label_Stir(MyLabel):
    pressed_signal = pyqtSignal()

    def mousePressEvent(self, e):
        self.pressed_signal.emit()

    def mouseMoveEvent(self, e):
        pass


class My_Ui(QWidget):
    def __init__(self):
        super(My_Ui, self).__init__()
        self.setupUI()
        self.resize(800, 800)

    def setupUI(self):
        label = MyLabel(self)
        label.setStyleSheet("""
        background-color:red;
        """)
        label.resize(50, 50)
        self.setWindowTitle("Click or Move")
        self.setGeometry(300, 300, 280, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = My_Ui()
    main.show()
    sys.exit(app.exec_())
