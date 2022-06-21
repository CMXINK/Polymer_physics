from PyQt5.Qt import *
from views.ui.get_styrene import Ui_Form
import sys


class Get_styrene(Ui_Form, QWidget):
    ensure_signal = pyqtSignal()
    def __init__(self):
        super(Get_styrene, self).__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        # self.label_3.setParent(self.label)

        self.label_3.syringe_label_moved.connect(lambda pos: self.on_label_3_syringe_label_moved(pos))
        self.my_label_list = []
        self.last_pos = False
        self.label_8.resize(37, 37)
        self.label_8.move(self.label_8.x(), self.label_8.y() + 3)
        self.label_3.raise_()
        self.current_label_num = -1
        self.text = 0
    # 这里的检测放到set.text()中进行检测
    # def commit_lk(self):
    #     if self.qualified():
    #         self.ensure_signal.emit()
    #
    # def qualified(self):
    #     pass

    def on_label_3_syringe_label_moved(self, pos):
        def fun():
            if self.current_label_num >= len(self.my_label_list) - 1:
                label = QLabel(self.content)
                self.my_label_list.append(label)
                label.setStyleSheet("""
                                border-image: url(:/add/填充png.png);
                                """)
                label.resize(37, 37)
                try:

                    x = self.last_pos.x() + pos.x() / abs(pos.x()) * 1
                    y = self.last_pos.y() + pos.y() / abs(pos.y()) * 1
                    label_pos = QPoint(x, y)
                    label.move(label.mapToParent(label_pos))
                except:
                    x = self.label_8.x() + pos.x() / abs(pos.x()) * 1
                    y = self.label_8.y() + pos.y() / abs(pos.y()) * 1
                    label_pos = QPoint(x, y)
                    label.move(label.mapToParent(label_pos))
                self.last_pos = label.pos()
                label.raise_()
                label.show()
            else:
                self.my_label_list[self.current_label_num].show()

        if pos.x() > 1:
            for i in range(0, abs(pos.x())):
                fun()
                self.current_label_num += 1
        if pos.x() < -1:
            for i in range(0, abs(pos.x())):
                try:
                    self.my_label_list[self.current_label_num].hide()
                    self.current_label_num -= 1
                    self.label_3.raise_()
                except:
                    return

        if pos.x() == -1:
            try:
                self.my_label_list[self.current_label_num].hide()
                self.label_3.raise_()
                self.current_label_num -= 1
            except:
                return


        elif pos.x() == 1:
            fun()
            self.current_label_num += 1
        self.text += pos.x()
        self.label_6.setText(str(self.text) + "ml")
        if self.text < 0:
            self.label_6.setText("0ml")
        if self.text > 95:
            self.label_6.setText("95ml")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Get_styrene()
    main.show()
    app.exit(app.exec_())
