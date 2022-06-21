import sys
from PyQt5.Qt import *
from views.ui.get_medicine import Ui_Form
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class Get_medicine(Ui_Form, QWidget):
    ensure_signal = pyqtSignal()

    def __init__(self):
        super(Get_medicine, self).__init__()
        self.setupUi(self)
        self.mouse_pos = QPoint(0, 0)
        self.setAttribute(Qt.WA_StyledBackground, True)
        # 这里的x,y是自定义label传入的释放时的按钮坐标
        self.mylabel.mouseReleased.connect(self.labelmouseReleased)
        self.label_2.pressed_signal.connect(lambda: self.label_2.setText("正在搅拌"))

    def labelmouseReleased(self):
        self.label_6.hide()
        self.label_4.setParent(self.mylabel.parent())
        x = self.mylabel.x()
        y = self.mylabel.y() + self.mylabel.height()
        t_x = self.label_4.x()
        t_y = self.label_4.y()
        if x in range(t_x, t_x + self.label_4.width()) and y in range(t_y, t_y + self.label_4.height()):
            if self.label_2.text() != "正在搅拌":
                QMessageBox.information(self, "通知", "请先进行搅拌")
                return
            else:
                QMessageBox.information(self, "通知", "进入下一步")
                self.ensure_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Get_medicine()
    main.show()
    sys.exit(app.exec_())
