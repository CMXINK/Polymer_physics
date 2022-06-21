# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_cyclohexane.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1091, 742)
        Form.setStyleSheet("#Form{\n"
"    border-image: url(:/add/bj3.jpeg);\n"
"    }\n"
"")
        self.template_2 = QtWidgets.QWidget(Form)
        self.template_2.setGeometry(QtCore.QRect(0, 0, 1091, 741))
        self.template_2.setObjectName("template_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.template_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QWidget(self.template_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setStyleSheet("")
        self.title.setObjectName("title")
        self.label_5 = QtWidgets.QLabel(self.title)
        self.label_5.setGeometry(QtCore.QRect(130, 10, 978, 56))
        self.label_5.setStyleSheet("font: 22pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.title)
        self.section = QtWidgets.QWidget(self.template_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.section.sizePolicy().hasHeightForWidth())
        self.section.setSizePolicy(sizePolicy)
        self.section.setObjectName("section")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.section)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.content = QtWidgets.QWidget(self.section)
        self.content.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy)
        self.content.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    font: 16pt \"Arial\";\n"
"}\n"
"*{\n"
"    border-image:none;\n"
"}\n"
"")
        self.content.setObjectName("content")
        self.label = QtWidgets.QLabel(self.content)
        self.label.setGeometry(QtCore.QRect(540, 30, 505, 594))
        self.label.setStyleSheet("border-image: url(:/add/加入环己烷.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.content)
        self.label_2.setGeometry(QtCore.QRect(930, 320, 71, 31))
        self.label_2.setStyleSheet("background-color: red;\n"
"font: 14pt \"楷体\";\n"
"color:rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.add_cyclohexane_tips_plaintextedit = QtWidgets.QTextEdit(self.content)
        self.add_cyclohexane_tips_plaintextedit.setEnabled(False)
        self.add_cyclohexane_tips_plaintextedit.setGeometry(QtCore.QRect(110, 100, 291, 181))
        self.add_cyclohexane_tips_plaintextedit.setStyleSheet("color:rgb(0, 0, 0);\n"
"border:none;\n"
"background-color:transparent;")
        self.add_cyclohexane_tips_plaintextedit.setObjectName("add_cyclohexane_tips_plaintextedit")
        self.label_3 = QtWidgets.QLabel(self.content)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(50, 20, 171, 51))
        self.label_3.setStyleSheet("font: 20pt \"Agency FB\";\n"
"color: rgb(0, 0, 0)")
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.content)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 420, 93, 144))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(60)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.add_cyclohexane_start_btn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_cyclohexane_start_btn.sizePolicy().hasHeightForWidth())
        self.add_cyclohexane_start_btn.setSizePolicy(sizePolicy)
        self.add_cyclohexane_start_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color: cyan;\n"
"    color:rgb(255, 255, 255);\n"
"    width:91px;\n"
"    height:41px;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";    \n"
"    background-color: lightblue;\n"
"    color:green;\n"
"}")
        self.add_cyclohexane_start_btn.setObjectName("add_cyclohexane_start_btn")
        self.verticalLayout_3.addWidget(self.add_cyclohexane_start_btn)
        self.add_cyclohexane_stop_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.add_cyclohexane_stop_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_cyclohexane_stop_btn.sizePolicy().hasHeightForWidth())
        self.add_cyclohexane_stop_btn.setSizePolicy(sizePolicy)
        self.add_cyclohexane_stop_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color: lightgray;\n"
"    color:rgb(255, 255, 255);\n"
"    width:91px;\n"
"    height:41px;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";    \n"
"    background-color: lightgray;\n"
"    color:gray;\n"
"}")
        self.add_cyclohexane_stop_btn.setObjectName("add_cyclohexane_stop_btn")
        self.verticalLayout_3.addWidget(self.add_cyclohexane_stop_btn)
        self.verticalLayout_2.addWidget(self.content)
        self.verticalLayout.addWidget(self.section)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "                      苯 乙 烯 阴 离 子 聚 合 实 验"))
        self.label_2.setText(_translate("Form", "0  ml"))
        self.add_cyclohexane_tips_plaintextedit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'隶书\'; font-size:14pt;\"> 点击“</span><span style=\" font-family:\'隶书\'; font-size:14pt; color:#ff0000;\">开始</span><span style=\" font-family:\'隶书\'; font-size:14pt;\">”加入环己烷，达到</span><span style=\" font-family:\'隶书\'; font-size:14pt; color:#ff0000;\">cmx</span><span style=\" font-family:\'隶书\'; font-size:14pt;\">后点击请点击停止</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'隶书\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'隶书\'; font-size:14pt;\"> 在</span><span style=\" font-family:\'隶书\'; font-size:14pt; color:#ff0000;\">cmx*1.1</span><span style=\" font-family:\'隶书\'; font-size:14pt;\">至</span><span style=\" font-family:\'隶书\'; font-size:14pt; color:#ff0000;\">cmx*0.9</span><span style=\" font-family:\'隶书\'; font-size:14pt;\">范内数值有效</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "滴加环己烷"))
        self.add_cyclohexane_start_btn.setText(_translate("Form", "开 始"))
        self.add_cyclohexane_stop_btn.setText(_translate("Form", "停 止"))
from views.images.add_cyclohexane_rc import *