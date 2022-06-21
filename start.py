import sys

from settings import ShowWidget
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ShowWidget()
    app.exit(app.exec_())
