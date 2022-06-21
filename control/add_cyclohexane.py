import sys
import time

from PyQt5.Qt import *
import ctypes
from views.ui.add_cyclohexane import Ui_Form

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class MyThread(QThread):
    def __init__(self, qt_obj):
        super(MyThread, self).__init__()
        self.qt_obj = qt_obj
        self.__get_result__ = None

    def run(self):
        self.__get_result__ = self.qt_obj()

    def get_result(self):
        return self.__get_result__


class Add_cyclohexane(Ui_Form, QWidget):
    ensure_signal = pyqtSignal()

    def __init__(self, target):
        """
        :param target: 外界传入的参数,用来确定滴加环己烷的最终值
        """
        super(Add_cyclohexane, self).__init__()
        self.target = 10.0
        self.setupUi(self)
        self.setWindowTitle("高分物理实验")
        self.add_cyclohexane_start_btn.clicked.connect(self.start_add_lk)
        self.add_cyclohexane_stop_btn.clicked.connect(lambda: self.stop_add_lk(True))
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.mythread = MyThread(self.thread_fun)
        self.mythread.finished.connect(self.thread_end_target)
        self.mandatory_stop = False  # 人工点击暂停
        self.content.setEnabled(True)

    def start_add_lk(self):
        try:

            self.mythread.start()

        except:
            self.mythread = MyThread(self.thread_fun)
            self.mythread.start()



        finally:
            self.add_cyclohexane_start_btn.setStyleSheet("""
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
            self.add_cyclohexane_start_btn.setEnabled(False)
            self.add_cyclohexane_stop_btn.setStyleSheet("""
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
            self.add_cyclohexane_stop_btn.setEnabled(True)

    def stop_add_lk(self, check=False):
        """

        :param check: 用来和对是否为人为暂停
        :return: none
        """
        if check:
            self.mandatory_stop = True
        self.add_cyclohexane_start_btn.setStyleSheet("""
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
        self.add_cyclohexane_start_btn.setEnabled(True)
        self.add_cyclohexane_stop_btn.setStyleSheet("""
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
        self.add_cyclohexane_stop_btn.setEnabled(False)

    def thread_fun(self):
        """
        thread执行函数
        :return: 执行bool
        """
        times = 0
        self.mandatory_stop = False
        while True:
            times += 1
            time.sleep(0.1)
            self.label_2.setText("{}ml".format(str(times / 5)))
            print(self.label_2.text())
            if self.label_2.text() == str(self.target)+"ml" or self.mandatory_stop:
                return not self.mandatory_stop

    def thread_end_target(self):
        if self.mythread.get_result():
            QMessageBox.information(self, "通知", "滴加成功,请继续下步操作")
            self.ensure_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Add_cyclohexane(12.3)
    main.show()
    sys.exit(app.exec_())
