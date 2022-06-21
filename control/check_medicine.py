import sys
from PyQt5.Qt import *
import ctypes
from views.ui.check_medicine import Ui_Form

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class Check_medicine(Ui_Form, QWidget):
    ensure_signal = pyqtSignal()

    def __init__(self):
        super(Check_medicine, self).__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowTitle("选择药品")
        self.__cname__ = "Check_medicine"
        self.medicine_alcohol_checkbox.stateChanged['int'].connect(
            lambda: self.object_checkbox_lk(self.medicine_alcohol_checkbox))
        self.medicine_oil_checkbox.stateChanged['int'].connect(
            lambda: self.object_checkbox_lk(self.medicine_oil_checkbox))
        self.medicine_peroxide_checkbox.stateChanged['int'].connect(
            lambda: self.object_checkbox_lk(self.medicine_peroxide_checkbox))
        self.medicine_acrylonitrile_checkbox.stateChanged['int'].connect(
            lambda: self.object_checkbox_lk(self.medicine_acrylonitrile_checkbox))
        self.medicine_styrene_checkbox.stateChanged['int'].connect(
            lambda: self.object_checkbox_lk(self.medicine_styrene_checkbox))
        self.medicine_azodiisobutyronitrile_checkbox.stateChanged['int'].connect(
            lambda: self.object_checkbox_lk(self.medicine_azodiisobutyronitrile_checkbox))
        self.medicine_tetrahydrofuran_checkbox.stateChanged['int'].connect(
            lambda: self.object_checkbox_lk(self.medicine_tetrahydrofuran_checkbox))
        self.medicine_lithium_checkbox.stateChanged['int'].connect(
            lambda: self.object_checkbox_lk(self.medicine_lithium_checkbox))
        self.medicine_cyclohexane_checkbox.stateChanged['int'].connect(
            lambda: self.object_checkbox_lk(self.medicine_cyclohexane_checkbox))
        self.medicine_submit_btn.clicked.connect(self.commit_lk)
        self.checked_name = []

    def commit_lk(self):
        # self.qualified()用来检测数据是否可以进入下一个界面
        if self.qualified():
            self.ensure_signal.emit()

    def qualified(self):
        if len(self.checked_name) == 5:
            for i in ["medicine_styrene_checkbox", "medicine_cyclohexane_checkbox",
                      "medicine_lithium_checkbox", "medicine_tetrahydrofuran_checkbox",
                      "medicine_alcohol_checkbox"]:
                if i not in self.checked_name:
                    return
            else:
                print(111)
                return True

    # 勾选上后拿到对应的空间的名字
    def object_checkbox_lk(self, object_checkbox):
        if object_checkbox.isChecked():
            self.checked_name.append(object_checkbox.objectName())
        else:
            self.checked_name.remove(object_checkbox.objectName())
        print(self.checked_name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Check_medicine()
    main.show()
    sys.exit(app.exec_())
