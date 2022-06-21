from PyQt5.Qt import *
from views.ui.formula_calculate_one import Ui_Form
import sys


class Formula_calculate_one(Ui_Form, QWidget):
    ensure_signal = pyqtSignal()

    def __init__(self):
        super(Formula_calculate_one, self).__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowTitle("高分子物理实验")
        self.calculate_one_submit_btn.clicked.connect(self.submit)
        self.calculate_one_submit_btn.clicked.connect(self.commit_lk)

    def commit_lk(self):
        if self.qualified():
            self.ensure_signal.emit()

    def qualified(self):
        return True

    def submit(self):
        object_lineedit = [self.LineEdit, self.LineEdit_2, self.LineEdit_3, self.LineEdit_4, self.tHFLineEdit]
        if False in list(map(lambda i: i.text() if i.text() else False, [i for i in object_lineedit])):
            QMessageBox.warning(self, "警告", "所有列不能为空,请重新输入")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Formula_calculate_one()
    main.show()
    app.exit(app.exec_())
