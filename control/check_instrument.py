import os
import sys
from PyQt5.Qt import *
import ctypes  # 需要用到的库

from views.ui.check_instrument import Ui_Form

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class Check_instrument(Ui_Form, QWidget):
    ensure_signal = pyqtSignal()

    def __init__(self):
        super(Check_instrument, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("实验仪器")
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.checkBox.stateChanged['int'].connect(lambda: self.instrument_check_lk(self.checkBox))
        self.checkBox_3.stateChanged['int'].connect(lambda: self.instrument_check_lk(self.checkBox_3))
        self.checkBox_26.stateChanged['int'].connect(lambda: self.instrument_check_lk(self.checkBox_26))
        self.checkBox_4.stateChanged['int'].connect(lambda: self.instrument_check_lk(self.checkBox_4))
        self.checkBox_17.stateChanged['int'].connect(lambda: self.instrument_check_lk(self.checkBox_17))
        self.checkBox_54.stateChanged['int'].connect(lambda: self.instrument_check_lk(self.checkBox_54))
        self.checkBox_53.stateChanged['int'].connect(lambda: self.instrument_check_lk(self.checkBox_53))
        self.checkBox_25.stateChanged['int'].connect(lambda: self.instrument_check_lk(self.checkBox_25))
        self.checkBox_48.stateChanged['int'].connect(lambda: self.instrument_check_lk(self.checkBox_48))
        self.checkBox_49.stateChanged['int'].connect(lambda: self.instrument_check_lk(self.checkBox_49))
        self.checkBox_5.stateChanged['int'].connect(lambda: self.instrument_check_lk(self.checkBox_5))
        self.checkBox_50.stateChanged['int'].connect(lambda: self.instrument_check_lk(self.checkBox_50))
        self.checkBox_51.stateChanged['int'].connect(lambda: self.instrument_check_lk(self.checkBox_51))
        self.checkBox_6.stateChanged['int'].connect(lambda: self.instrument_check_lk(self.checkBox_6))
        self.checkBox_52.stateChanged['int'].connect(lambda: self.instrument_check_lk(self.checkBox_52))
        self.pushButton.clicked.connect(self.commit_lk)  # 确认按钮
        self.checked_name = []

    def commit_lk(self):
        # self.qualified()用来检测数据是否可以进入下一个界面
        if self.qualified():
            self.ensure_signal.emit()

    def qualified(self):
        answer = [
            "温度计", "厚壁乳胶管", "加料管", "氮气瓶", "注射器", "电磁搅拌器", "双排管系统",
            "抽真空装置", "两口烧瓶", "铁架台", "计泡器", "恒温水箱"
        ]
        if len(self.checked_name) == len(answer):

            for i in answer:
                if i not in self.checked_name:
                    return
            else:
                return True



    def instrument_check_lk(self, object_checkbox):
        if object_checkbox.isChecked():
            self.checked_name.append(object_checkbox.text())
        else:
            self.checked_name.remove(object_checkbox.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Check_instrument()
    main.show()
    sys.exit(app.exec_())
