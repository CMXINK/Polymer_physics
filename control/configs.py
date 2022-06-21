import sys

from PyQt5.Qt import *
from PyQt5.QtWidgets import QWidget, QApplication
from views.ui.configs import Ui_Form


class Configs(QWidget, Ui_Form):

    def __init__(self):
        super(Configs, self).__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowTitle("配置")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Configs()
    main.show()
    sys.exit(app.exec_())
