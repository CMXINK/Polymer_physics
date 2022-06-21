from PyQt5.Qt import *
from views.ui.formula_calcualate_two import Ui_Form
import sys


class Formula_calculate_two(Ui_Form, QWidget):
    ensure_signal = pyqtSignal()

    def __init__(self, calculate_one_data: list):
        super(Formula_calculate_two, self).__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        #  这里按顺序传参就好
        # [i.setText(str(text)) for i, text in
        #  zip([self.label_4, self.label_5, self.label_6, self.label_7, self.label_8], calculate_one_data)]
        self.clacualate_two_submit_btn.clicked.connect(self.commit_lk)

    def commit_lk(self):
        if self.qualified():
            self.ensure_signal.emit()

    def qualified(self):
        return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Formula_calculate_two([1.2, 3.02, 12.21, 113.45, 24.09])
    main.show()
    app.exit(app.exec_())
