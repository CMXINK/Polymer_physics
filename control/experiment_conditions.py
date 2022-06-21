import sys

from PyQt5 import QtGui

from views.ui.experiment_conditions import Ui_Form
from PyQt5.Qt import *

import ctypes  # 需要用到的库

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class Experiment_conditions(Ui_Form, QWidget):
    ensure_signal = pyqtSignal()

    def __init__(self):
        super(Experiment_conditions, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("高分子物理实验")
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.conditions_temperature_two_btn.clicked.connect(
            lambda: self.selected(self.conditions_temperature_two_btn, False)),
        self.conditions_temperature_one_btn.clicked.connect(
            lambda: self.selected(self.conditions_temperature_one_btn, False)),
        self.conditions_temperature_three_btn.clicked.connect(
            lambda: self.selected(self.conditions_temperature_three_btn, False)),
        self.conditions_humidity_one_btn.clicked.connect(lambda: self.selected(self.conditions_humidity_one_btn, True))
        self.conditions_humidity_two_btn.clicked.connect(lambda: self.selected(self.conditions_humidity_two_btn, True))
        self.conditions_humidity_three_btn.clicked.connect(
            lambda: self.selected(self.conditions_humidity_three_btn, True))

        self.conditions_submit_btn.clicked.connect(self.commit_lk)
        self.humidity_obj = object
        self.tempeature_obj = object

    def commit_lk(self):
        # self.qualified()用来检测数据是否可以进入下一个界面
        if self.qualified():
            self.ensure_signal.emit()

    def qualified(self):

        if self.humidity_obj == self.conditions_humidity_three_btn and self.tempeature_obj == self. \
                conditions_temperature_two_btn:
            return True

    def selected(self, object_btn, humidity: bool):
        if humidity:
            self.conditions_checked_humidity_label.setText(object_btn.text())
            self.humidity_obj = object_btn
        else:
            self.conditions_checked_tempeature_label.setText(object_btn.text())
            self.tempeature_obj = object_btn
        print(self.conditions_checked_humidity_label.text(), self.conditions_checked_tempeature_label.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Experiment_conditions()
    main.show()
    sys.exit(app.exec_())
