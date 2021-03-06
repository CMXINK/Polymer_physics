# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'install_instrument.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1091, 709)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(1091, 16777215))
        Form.setStyleSheet("#Form{\n"
"    \n"
"    border-image: url(:/experiment/e7c07976538683163ef460b0adf0b00c.jpeg);\n"
"    \n"
"}")
        self.template_2 = QtWidgets.QWidget(Form)
        self.template_2.setGeometry(QtCore.QRect(0, 0, 1161, 791))
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
        self.label_15 = QtWidgets.QLabel(self.title)
        self.label_15.setGeometry(QtCore.QRect(30, 10, 978, 56))
        self.label_15.setStyleSheet("font: 22pt \"Arial\";")
        self.label_15.setObjectName("label_15")
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
        self.content.setStyleSheet("QComboBox{\n"
"    border:none;\n"
"    border-radius:8px;    \n"
"    font: 14pt \"????????????\";    \n"
"    background-color: rgb(255, 85, 0);\n"
"    color:rgb(255, 255, 255);\n"
"    border-left:none;\n"
"}\n"
"QComboBox:clicked{\n"
"    border:none;\n"
"    border-radius:8px;    \n"
"    font: 14pt \"????????????\";    \n"
"    background-color: rgb(255, 85, 0);\n"
"    color: rgb(255, 85, 0);\n"
"}\n"
"QComboBox::drop-down{\n"
"    width:30px;\n"
"    border-radius:8px;        \n"
"    image: url(:/experiment/checkbox_drop-down.png);\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"    background-color:rgb(255, 170, 127);\n"
"}\n"
"QLabel {\n"
"    font: 14pt \"??????\";\n"
"}")
        self.content.setObjectName("content")
        self.label = QtWidgets.QLabel(self.content)
        self.label.setGeometry(QtCore.QRect(30, 30, 141, 31))
        self.label.setStyleSheet("font: 20pt \"??????\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.content)
        self.label_2.setGeometry(QtCore.QRect(220, 80, 601, 131))
        self.label_2.setStyleSheet("border-image: url(:/experiment/?????????.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.content)
        self.label_5.setGeometry(QtCore.QRect(64, 429, 138, 59))
        self.label_5.setStyleSheet("border-image: url(:/experiment/???????????????.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.content)
        self.label_6.setGeometry(QtCore.QRect(814, 339, 42, 153))
        self.label_6.setStyleSheet("border-image: url(:/experiment/????????????.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.content)
        self.label_7.setGeometry(QtCore.QRect(654, 419, 25, 73))
        self.label_7.setStyleSheet("border-image: url(:/experiment/?????????.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.content)
        self.label_8.setGeometry(QtCore.QRect(1004, 379, 30, 112))
        self.label_8.setStyleSheet("border-image: url(:/experiment/?????????.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_17 = QtWidgets.QLabel(self.content)
        self.label_17.setGeometry(QtCore.QRect(464, 429, 52, 61))
        self.label_17.setStyleSheet("border-image:url(:/experiment/????????????.png)")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.content)
        self.label_18.setGeometry(QtCore.QRect(254, 449, 100, 41))
        self.label_18.setStyleSheet("border-image: url(:/experiment/????????????.png);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.comboBox = QtWidgets.QComboBox(self.content)
        self.comboBox.setGeometry(QtCore.QRect(66, 564, 91, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.content)
        self.comboBox_2.setGeometry(QtCore.QRect(254, 564, 91, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setStyleSheet("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.content)
        self.comboBox_3.setGeometry(QtCore.QRect(444, 564, 91, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setStyleSheet("")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.content)
        self.comboBox_4.setGeometry(QtCore.QRect(614, 564, 91, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setStyleSheet("")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.content)
        self.comboBox_5.setGeometry(QtCore.QRect(794, 564, 91, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        self.comboBox_5.setStyleSheet("")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(self.content)
        self.comboBox_6.setGeometry(QtCore.QRect(964, 564, 91, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy)
        self.comboBox_6.setStyleSheet("")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.label_3 = QtWidgets.QLabel(self.content)
        self.label_3.setGeometry(QtCore.QRect(153, 90, 81, 171))
        self.label_3.setStyleSheet("border:2px solid red;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.content)
        self.label_4.setGeometry(QtCore.QRect(820, 90, 81, 171))
        self.label_4.setStyleSheet("border:2px solid red;")
        self.label_4.setObjectName("label_4")
        self.label_29 = QtWidgets.QLabel(self.content)
        self.label_29.setGeometry(QtCore.QRect(260, 130, 81, 171))
        self.label_29.setStyleSheet("border:2px solid red;")
        self.label_29.setObjectName("label_29")
        self.label_33 = QtWidgets.QLabel(self.content)
        self.label_33.setGeometry(QtCore.QRect(490, 310, 211, 81))
        self.label_33.setStyleSheet("border:2px solid red;")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.content)
        self.label_34.setGeometry(QtCore.QRect(540, 250, 121, 61))
        self.label_34.setStyleSheet("border:2px solid red;")
        self.label_34.setObjectName("label_34")
        self.install_instrument_submit_btn = QtWidgets.QPushButton(self.content)
        self.install_instrument_submit_btn.setGeometry(QtCore.QRect(950, 100, 91, 41))
        self.install_instrument_submit_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"????????????\";\n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(255, 255, 255);\n"
"    width:91px;\n"
"    height:41px;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"????????????\";    \n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(31, 117, 213);\n"
"}")
        self.install_instrument_submit_btn.setObjectName("install_instrument_submit_btn")
        self.label_9 = QtWidgets.QLabel(self.content)
        self.label_9.setGeometry(QtCore.QRect(75, 520, 120, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.content)
        self.label_10.setGeometry(QtCore.QRect(280, 520, 48, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.content)
        self.label_11.setGeometry(QtCore.QRect(444, 519, 96, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.content)
        self.label_12.setGeometry(QtCore.QRect(624, 519, 72, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.content)
        self.label_13.setGeometry(QtCore.QRect(794, 519, 96, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.content)
        self.label_14.setGeometry(QtCore.QRect(964, 519, 72, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.widget = QtWidgets.QWidget(self.content)
        self.widget.setGeometry(QtCore.QRect(560, 220, 81, 51))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_31 = QtWidgets.QLabel(self.widget)
        self.label_31.setStyleSheet("border:2px solid red;\n"
"border-bottom:none;")
        self.label_31.setObjectName("label_31")
        self.verticalLayout_3.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.widget)
        self.label_32.setStyleSheet("border:2px dotted red;\n"
"border-top:none;")
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.verticalLayout_3.addWidget(self.label_32)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)
        self.widget.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.comboBox_3.raise_()
        self.comboBox_4.raise_()
        self.comboBox_5.raise_()
        self.comboBox_6.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_29.raise_()
        self.label_33.raise_()
        self.label_18.raise_()
        self.label_17.raise_()
        self.label_34.raise_()
        self.install_instrument_submit_btn.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.verticalLayout_2.addWidget(self.content)
        self.verticalLayout.addWidget(self.section)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_15.setText(_translate("Form", "                           ??? ??? ??? ??? ??? ??? ??? ??? ??? ???"))
        self.label.setText(_translate("Form", "????????????"))
        self.comboBox.setItemText(0, _translate("Form", "??? ???"))
        self.comboBox.setItemText(1, _translate("Form", "??????1"))
        self.comboBox.setItemText(2, _translate("Form", "??????2"))
        self.comboBox.setItemText(3, _translate("Form", "??????3"))
        self.comboBox.setItemText(4, _translate("Form", "??????4"))
        self.comboBox.setItemText(5, _translate("Form", "??????5"))
        self.comboBox.setItemText(6, _translate("Form", "??????6"))
        self.comboBox_2.setItemText(0, _translate("Form", "??? ???"))
        self.comboBox_2.setItemText(1, _translate("Form", "??????1"))
        self.comboBox_2.setItemText(2, _translate("Form", "??????2"))
        self.comboBox_2.setItemText(3, _translate("Form", "??????3"))
        self.comboBox_2.setItemText(4, _translate("Form", "??????4"))
        self.comboBox_2.setItemText(5, _translate("Form", "??????5"))
        self.comboBox_2.setItemText(6, _translate("Form", "??????6"))
        self.comboBox_3.setItemText(0, _translate("Form", "??? ???"))
        self.comboBox_3.setItemText(1, _translate("Form", "??????1"))
        self.comboBox_3.setItemText(2, _translate("Form", "??????2"))
        self.comboBox_3.setItemText(3, _translate("Form", "??????3"))
        self.comboBox_3.setItemText(4, _translate("Form", "??????4"))
        self.comboBox_3.setItemText(5, _translate("Form", "??????5"))
        self.comboBox_3.setItemText(6, _translate("Form", "??????6"))
        self.comboBox_4.setItemText(0, _translate("Form", "??? ???"))
        self.comboBox_4.setItemText(1, _translate("Form", "??????1"))
        self.comboBox_4.setItemText(2, _translate("Form", "??????2"))
        self.comboBox_4.setItemText(3, _translate("Form", "??????3"))
        self.comboBox_4.setItemText(4, _translate("Form", "??????4"))
        self.comboBox_4.setItemText(5, _translate("Form", "??????5"))
        self.comboBox_4.setItemText(6, _translate("Form", "??????6"))
        self.comboBox_5.setItemText(0, _translate("Form", "??? ???"))
        self.comboBox_5.setItemText(1, _translate("Form", "??????1"))
        self.comboBox_5.setItemText(2, _translate("Form", "??????2"))
        self.comboBox_5.setItemText(3, _translate("Form", "??????3"))
        self.comboBox_5.setItemText(4, _translate("Form", "??????4"))
        self.comboBox_5.setItemText(5, _translate("Form", "??????5"))
        self.comboBox_5.setItemText(6, _translate("Form", "??????6"))
        self.comboBox_6.setItemText(0, _translate("Form", "??? ???"))
        self.comboBox_6.setItemText(1, _translate("Form", "??????1"))
        self.comboBox_6.setItemText(2, _translate("Form", "??????2"))
        self.comboBox_6.setItemText(3, _translate("Form", "??????3"))
        self.comboBox_6.setItemText(4, _translate("Form", "??????4"))
        self.comboBox_6.setItemText(5, _translate("Form", "??????5"))
        self.comboBox_6.setItemText(6, _translate("Form", "??????6"))
        self.label_3.setText(_translate("Form", "?????????"))
        self.label_4.setText(_translate("Form", "?????????"))
        self.label_29.setText(_translate("Form", "?????????"))
        self.label_33.setText(_translate("Form", "     ?????????"))
        self.label_34.setText(_translate("Form", "  ?????????"))
        self.install_instrument_submit_btn.setText(_translate("Form", "??? ???"))
        self.label_9.setText(_translate("Form", "???????????????"))
        self.label_10.setText(_translate("Form", "??????"))
        self.label_11.setText(_translate("Form", "????????????"))
        self.label_12.setText(_translate("Form", "?????????"))
        self.label_13.setText(_translate("Form", "????????????"))
        self.label_14.setText(_translate("Form", "?????????"))
        self.label_31.setText(_translate("Form", "?????????"))
from views.images.designer_experiment_rc import *
