# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logon.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(927, 500)
        Form.setMinimumSize(QtCore.QSize(927, 500))
        Form.setMaximumSize(QtCore.QSize(927, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logon/logon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 927, 500))
        self.widget.setMinimumSize(QtCore.QSize(927, 500))
        self.widget.setMaximumSize(QtCore.QSize(927, 500))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.widget.setFont(font)
        self.widget.setStyleSheet("#widget{\n"
"    border-image: url(:/logon/LOGON.png)\n"
"}")
        self.widget.setObjectName("widget")
        self.logon_safelogon_btn = QtWidgets.QPushButton(self.widget)
        self.logon_safelogon_btn.setEnabled(False)
        self.logon_safelogon_btn.setGeometry(QtCore.QRect(410, 460, 133, 31))
        self.logon_safelogon_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.logon_safelogon_btn.setStyleSheet("QPushButton{\n"
"    image: url(:/logon/logon_safe_yellow.jpg);\n"
"    font: 15pt \"方正舒体\";\n"
"color:rgb(117, 117, 117);\n"
"}\n"
"QPushButton:hover{\n"
"image: url(:/logon/logon_safe_yellow.jpg);\n"
"border-radius:10px;\n"
"color:rgb(117, 117, 117);\n"
"font: 16pt \"隶书\";}\n"
"QPushButton:pressed{\n"
"image: url(:/logon/logon_safe_yellow.jpg);\n"
"color:rgb(0, 170, 0);\n"
"font: 14pt \"隶书\";}\n"
"\n"
"\n"
"")
        self.logon_safelogon_btn.setObjectName("logon_safelogon_btn")
        self.layoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(180, 240, 641, 151))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_9.setStyleSheet("font: 15pt \"方正舒体\";\n"
"color: rgb(52, 52, 52);")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/logon/ico-password.png"))
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("方正舒体")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: 15pt \"方正舒体\";\n"
"color: rgb(52, 52, 52);")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/logon/ico-user.png"))
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.logon_password_lineedit = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.logon_password_lineedit.setFont(font)
        self.logon_password_lineedit.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"border-bottom:1px solid rgb(27, 27, 27);\n"
"font: 12pt \"微软雅黑\";")
        self.logon_password_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.logon_password_lineedit.setObjectName("logon_password_lineedit")
        self.gridLayout_2.addWidget(self.logon_password_lineedit, 1, 1, 1, 1)
        self.logon_username_lineedit = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.logon_username_lineedit.setFont(font)
        self.logon_username_lineedit.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"border-bottom:1px solid rgb(27, 27, 27);\n"
"font: 12pt \"微软雅黑\";")
        self.logon_username_lineedit.setText("")
        self.logon_username_lineedit.setObjectName("logon_username_lineedit")
        self.gridLayout_2.addWidget(self.logon_username_lineedit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(150, 60, 651, 61))
        self.label_2.setStyleSheet("font: 30pt \"华文行楷\";\n"
"color: rgb(56, 56, 56);\n"
"")
        self.label_2.setObjectName("label_2")
        self.logon_register_btn = QtWidgets.QPushButton(self.widget)
        self.logon_register_btn.setGeometry(QtCore.QRect(0, 460, 93, 28))
        self.logon_register_btn.setStyleSheet("color: rgb(161, 161, 161);\n"
"font: 12pt \"隶书\";\n"
"boder:none;\n"
"background-color: transparent;")
        self.logon_register_btn.setObjectName("logon_register_btn")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 400, 481, 36))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logon_showpassword_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        self.logon_showpassword_checkbox.setStyleSheet("font: 14pt \"隶书\";\n"
"color:rgb(45, 45, 45);")
        self.logon_showpassword_checkbox.setObjectName("logon_showpassword_checkbox")
        self.horizontalLayout.addWidget(self.logon_showpassword_checkbox)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.logon_rememberpassword_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        self.logon_rememberpassword_checkbox.setStyleSheet("font: 14pt \"隶书\";\n"
"color:rgb(45, 45, 45);")
        self.logon_rememberpassword_checkbox.setObjectName("logon_rememberpassword_checkbox")
        self.horizontalLayout.addWidget(self.logon_rememberpassword_checkbox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.logon_safelogon_btn.setText(_translate("Form", "安全登录"))
        self.logon_password_lineedit.setPlaceholderText(_translate("Form", "密码"))
        self.logon_username_lineedit.setPlaceholderText(_translate("Form", "账号"))
        self.label_2.setText(_translate("Form", "阴  离  子  聚  合  模  拟  实  验"))
        self.logon_register_btn.setText(_translate("Form", "配 置"))
        self.logon_showpassword_checkbox.setText(_translate("Form", "显示密码"))
        self.logon_rememberpassword_checkbox.setText(_translate("Form", "记住密码"))
from views.images.logon_rc import*
