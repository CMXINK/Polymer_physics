import sys
from PyQt5.Qt import *
import ctypes
from views.ui.install_instrument import Ui_Form

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class Install_instrument(Ui_Form, QWidget):
    ensure_signal = pyqtSignal()

    def __init__(self):
        super(Install_instrument, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("组装仪器")
        self.setMaximumSize(self.size())
        self.setAttribute(Qt.WA_StyledBackground, True)
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft, newTop)

        self.remember_combobox_data = {}
        self.comboBox.currentIndexChanged.connect(lambda: self.get_object_combobox(self.comboBox))
        self.comboBox_2.currentIndexChanged.connect(lambda: self.get_object_combobox(self.comboBox_2))
        self.comboBox_3.currentIndexChanged.connect(lambda: self.get_object_combobox(self.comboBox_3))
        self.comboBox_4.currentIndexChanged.connect(lambda: self.get_object_combobox(self.comboBox_4))
        self.comboBox_5.currentIndexChanged.connect(lambda: self.get_object_combobox(self.comboBox_5))
        self.comboBox_6.currentIndexChanged.connect(lambda: self.get_object_combobox(self.comboBox_6))

        self.install_instrument_submit_btn.clicked.connect(self.submit_lk)

    def get_object_combobox(self, obj):
        """
        获取combobox 当前的的文本并记录
        :param obj:
        :return:
        """
        self.remember_combobox_data[obj] = obj.currentIndex()

    def submit_lk(self):
        """
        :return: none
        """
        if self.remember_combobox_data != {self.comboBox: 6, self.comboBox_2: 5, self.comboBox_3: 4, self.comboBox_4: 3,
                                           self.comboBox_5: 2, self.comboBox_6: 1}:
            QMessageBox.information(self, "通知", "您的选择有误,请重新选择")

        else:
            self.ensure_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Install_instrument()
    main.show()
    sys.exit(app.exec_())
