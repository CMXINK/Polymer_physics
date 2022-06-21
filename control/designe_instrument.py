import random
import sys
import time

from PyQt5.Qt import *
import ctypes
from views.ui.designe_instrument import Ui_Form

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
from threading import Thread


class MyThread(QThread):
    def __init__(self, Qt_class):
        super(MyThread, self).__init__()
        self.qt_class = Qt_class

    def run(self):
        self.result = self.qt_class.mythread()

    def get_result(self):
        return self.result


class Designe_instrument(Ui_Form, QWidget):
    ensure_signal = pyqtSignal()
    def __init__(self):
        super(Designe_instrument, self).__init__()
        self.Mythread = MyThread(self)  # 此线程用于进行压强的变化
        self.Mythread.finished.connect(self.complate_lk)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowTitle("高分子物理实验")
        self.btn_color_remember_data = {
            self.design_instrument_btn1: False,
            self.design_instrument_btn2: False,
            self.design_instrument_btn3: False,
            self.design_instrument_btn4: False,
            self.design_instrument_btn5: False
        }
        self.design_instrument_btn1.clicked.connect(lambda: self.reverse_btn(self.design_instrument_btn1))
        self.design_instrument_btn2.clicked.connect(lambda: self.reverse_btn(self.design_instrument_btn2))
        self.design_instrument_btn3.clicked.connect(lambda: self.reverse_btn(self.design_instrument_btn3))
        self.design_instrument_btn4.clicked.connect(lambda: self.reverse_btn(self.design_instrument_btn4))
        self.design_instrument_btn5.clicked.connect(lambda: self.reverse_btn(self.design_instrument_btn5))
        self.designe_instrument_start_btn.clicked.connect(lambda: self.start_btn_lk())
        self.design_instrument_stop_btn_2.clicked.connect(lambda: self.stop_btn_lk(True))
        self.label_8.hide()
        self.mandatory_stop = False  # 强制终止(人为点击了终止)
        self.setMaximumSize(self.size())  # 禁止全屏

    # 反转按钮点击后的颜色
    def reverse_btn(self, object_btn):
        """
        用来反转按钮点击后的颜色 \n
        :param object_btn: 当前点击的按钮对象
        :return: none
        """
        if not self.btn_color_remember_data.get(object_btn):
            object_btn.setStyleSheet("border:12px solid green;border-radius:12;")
            self.btn_color_remember_data[object_btn] = True

        else:
            object_btn.setStyleSheet("border:12px solid red;border-radius:12;")
            self.btn_color_remember_data[object_btn] = False

    # 点击start要做的事
    def start_btn_lk(self):
        """
        开始净化以及通话入氮气前先进行验证, 验证的答案现在暂未给出
        :return: none
        """
        # 判断是否是通入氮气操作
        if self.designe_instrument_start_btn.text() == "通入氮气":
            if self.btn_color_remember_data != {
                self.design_instrument_btn1: True,
                self.design_instrument_btn2: False,
                self.design_instrument_btn3: True,
                self.design_instrument_btn4: False,
                self.design_instrument_btn5: True
            }:
                return QMessageBox.information(self, "通知", "您的组装有误,请修正后再开始通氮气操作")
            else:
                self.ensure_signal.emit()
        # 不是通入氮气操作,是净化操作
        else:
            self.label_5.setText("0")
            if self.btn_color_remember_data != {
                self.design_instrument_btn1: True,
                self.design_instrument_btn2: False,
                self.design_instrument_btn3: True,
                self.design_instrument_btn4: False,
                self.design_instrument_btn5: True}:
                QMessageBox.information(self, "通知", "您的组装有误,请修正后再开始")
            else:
                self.designe_instrument_start_btn.setStyleSheet("""
                        QPushButton{
            	border:none;
            	border-radius:7px;	
            	font: 13pt "微软雅黑";
            	background-color: gray;
            	color:rgb(255, 255, 255);
            	width:91px;
            	height:41px;
            }
            QPushButton:pressed{
            	border:none;
            	border-radius:7px;	
            	font: 13pt "微软雅黑";	
            	background-color: gray;
            	color:gray;
            }
                        """)
                self.designe_instrument_start_btn.setEnabled(False)
                self.design_instrument_stop_btn_2.setStyleSheet("""
            QPushButton{
            	border:none;
            	border-radius:7px;	
            	font: 13pt "微软雅黑";
            	background-color: red;
            	color:rgb(255, 255, 255);
            	width:91px;
            	height:41px;
            }
            QPushButton:pressed{
            	border:none;
            	border-radius:7px;	
            	font: 13pt "微软雅黑";	
            	background-color: red;
            	color:red;
            }
                        """)
                self.design_instrument_stop_btn_2.setEnabled(True)
                [i.setEnabled(False) for i in self.btn_color_remember_data.keys()]
                try:
                    self.Mythread.start()

                except:
                    self.Mythread = MyThread(self)
                    self.Mythread.finished.connect(self.complate_lk)
                    self.Mythread.start()

    def complate_lk(self):
        if self.Mythread.get_result():
            QMessageBox.information(self, "通知", "净化成功,请修改开关以完成氮气操作")
            self.label_5.hide()
            self.label_8.show()
            self.label_4.hide()
            self.label_6.hide()
            self.designe_instrument_start_btn.setText("通入氮气")
            self.design_instrument_stop_btn_2.hide()

    #  点击stop按钮时要做的事
    def stop_btn_lk(self, check=False):
        if check:
            self.mandatory_stop = True
        self.designe_instrument_start_btn.setStyleSheet("""
                    QPushButton{
	border:none;
	border-radius:7px;	
	font: 13pt "微软雅黑";
	background-color: green;
	color:rgb(255, 255, 255);
	width:91px;
	height:41px;
}
QPushButton:pressed{
	border:none;
	border-radius:7px;	
	font: 13pt "微软雅黑";	
	background-color: green;
	color:green;
}
        """)
        self.designe_instrument_start_btn.setEnabled(True)
        self.design_instrument_stop_btn_2.setStyleSheet("""
                    QPushButton{
	border:none;
	border-radius:7px;	
	font: 13pt "微软雅黑";
	background-color: gray;
	color:rgb(255, 255, 255);
	width:91px;
	height:41px;
}
QPushButton:pressed{
	border:none;
	border-radius:7px;	
	font: 13pt "微软雅黑";	
	background-color: gray;
	color:gray;
}
        """)
        self.design_instrument_stop_btn_2.setEnabled(False)
        [i.setEnabled(True) for i in self.btn_color_remember_data.keys()]

    def mythread(self):
        self.mandatory_stop = False
        end_time = str(random.randrange(241, 299))
        print(end_time)
        times = 0
        while True:
            if self.label_5.text() == "-" + end_time or self.mandatory_stop:
                self.stop_btn_lk(check=False)
                return not self.mandatory_stop
            time.sleep(0.01)
            times += 1
            self.label_5.setText("-" + str(int(times)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Designe_instrument()
    main.show()
    sys.exit(app.exec_())
