import sys
from views.ui.logon import Ui_Form
from PyQt5.Qt import *
import ctypes  # 需要用到的库
from pickle import dump, load

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class Logon(QMainWindow, Ui_Form):
    logon_register_btn_signal = pyqtSignal()
    logon_safelogon_btn_signal = pyqtSignal()
    """
    logon_safelogon_btn_signal:
        int : 登录账号的grade
        bool: 第一个， 用来检测自动登录按钮的状态
        bool: 第二个， 用来检测记住密码按钮的状态
    """

    def __init__(self, parent=None, *args, **kwargs):
        super(Logon, self).__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowTitle("高分子物理实验")
        self.logon_username_lineedit.setFocus()
        self.logon_safelogon_btn.setEnabled(True)
        self.logon_showpassword_checkbox.clicked.connect(self.showpassward)
        self.logon_safelogon_btn.clicked.connect(self.safe_logon)
        try:
            self.logon_username_lineedit.setText(self.check_remember(data=[], isfirst=True)[0])
            self.logon_password_lineedit.setText(self.check_remember(data=[], isfirst=True)[1])
        except:
            pass

    def check_remember(self, data: list, check=False, isfirst=False):
        """
        :param check: 检测本次是否需要记住密码(在登录信号发送时才调用被本函数)
        :return: data
        """
        with open("resource/check_remember.txt", "rb") as f_remember:
            try:
                if load(f_remember)[0] and isfirst:
                    self.logon_rememberpassword_checkbox.setChecked(True)
                    return self.read_remember_password(data, remember=True)
            except:
                pass
        if check:
            self.read_remember_password(data)
        with open("resource/check_remember.txt", "wb") as w_remember:
            dump([check], w_remember)

    def read_remember_password(self, data: list, remember=False):
        """
        检测是否勾选了或者是否要记住密码并自动返回对应数据 \n
        :param remember:  判断是否第一次进行检测(即是否是登录界面第一次打开对账号密码的查询)
        :param data: 需要传入的数据 data[user, password]
        :return: list [user, password]
        """
        with open("resource/check_up.txt", "rb") as f_u:
            if remember:
                return load(f_u)
        with open("resource/check_up.txt", "wb") as f_u:
            dump(data, f_u)

    def showpassward(self):
        if self.logon_showpassword_checkbox.isChecked():
            self.logon_password_lineedit.setEchoMode(QLineEdit.Normal)
        else:
            self.logon_password_lineedit.setEchoMode(QLineEdit.Password)

    def safe_logon(self):
        if self.logon_password_lineedit.text() and self.logon_username_lineedit.text():
            if self.logon_rememberpassword_checkbox.isChecked():
                self.check_remember([self.logon_username_lineedit.text(), self.logon_password_lineedit.text()], True)
            else:
                self.check_remember([self.logon_username_lineedit.text(), self.logon_password_lineedit.text()], False)
            print("安全登录")
            self.logon_safelogon_btn_signal.emit()
        else:
            QMessageBox.critical(self, '错误', '请输入正确的用户名和密码')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Logon()
    main.show()
    sys.exit(app.exec_())
