# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'get_medicine.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1079, 621)
        Form.setStyleSheet("#Form{\n"
"    border-image: url(:/add/简约1.jpg);}")
        self.template_2 = QtWidgets.QWidget(Form)
        self.template_2.setGeometry(QtCore.QRect(0, 0, 1081, 741))
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
        self.label_7 = QtWidgets.QLabel(self.title)
        self.label_7.setGeometry(QtCore.QRect(30, 10, 978, 56))
        self.label_7.setStyleSheet("font: 22pt \"Arial\";")
        self.label_7.setObjectName("label_7")
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy)
        self.content.setObjectName("content")
        self.label = QtWidgets.QLabel(self.content)
        self.label.setGeometry(QtCore.QRect(270, 30, 608, 248))
        self.label.setStyleSheet("border-image: url(:/add/实验结果图.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = Label_Stir(self.content)
        self.label_2.setGeometry(QtCore.QRect(600, 300, 121, 41))
        self.label_2.setStyleSheet("font: 15pt \"楷体\";")
        self.label_2.setObjectName("label_2")
        self.mylabel = MyLabel(self.content)
        self.mylabel.setGeometry(QtCore.QRect(550, 350, 110, 129))
        self.mylabel.setStyleSheet("border-image: url(:/add/注射器.png);")
        self.mylabel.setText("")
        self.mylabel.setObjectName("mylabel")
        self.label_4 = QtWidgets.QLabel(self.content)
        self.label_4.setGeometry(QtCore.QRect(180, 280, 106, 208))
        self.label_4.setStyleSheet("border-image: url(:/add/广口瓶.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.content)
        self.label_5.setGeometry(QtCore.QRect(200, 494, 91, 31))
        self.label_5.setStyleSheet("font: 14pt \"楷体\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.content)
        self.label_6.setGeometry(QtCore.QRect(580, 490, 91, 31))
        self.label_6.setStyleSheet("font: 14pt \"楷体\";")
        self.label_6.setObjectName("label_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.content)
        self.textBrowser.setGeometry(QtCore.QRect(790, 220, 261, 131))
        self.textBrowser.setStyleSheet("border:none;\n"
"background-color: transparent;")
        self.textBrowser.setObjectName("textBrowser")
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.textBrowser.raise_()
        self.mylabel.raise_()
        self.verticalLayout_2.addWidget(self.content)
        self.verticalLayout.addWidget(self.section)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "                           苯 乙 烯 阴 离 子 聚 合 实 验"))
        self.label_2.setText(_translate("Form", "开始搅拌"))
        self.label_5.setText(_translate("Form", "苯乙烯"))
        self.label_6.setText(_translate("Form", "注射器"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">1. 点击开始搅拌</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">2. 取苯乙烯</span><span style=\" font-size:12pt;\">(将注射器拖到苯乙烯瓶中)</span></p></body></html>"))
from views.ui.MyLabel import Label_Stir, MyLabel
from views.images.add_reagent_rc import *