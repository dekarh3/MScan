# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mNote_win.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(798, 953)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_3 = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QtCore.QSize(500, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.leFilter = QtWidgets.QLineEdit(self.frame)
        self.leFilter.setMinimumSize(QtCore.QSize(150, 0))
        self.leFilter.setObjectName("leFilter")
        self.horizontalLayout_3.addWidget(self.leFilter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pbPeopleFilter = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbPeopleFilter.sizePolicy().hasHeightForWidth())
        self.pbPeopleFilter.setSizePolicy(sizePolicy)
        self.pbPeopleFilter.setMinimumSize(QtCore.QSize(110, 0))
        self.pbPeopleFilter.setObjectName("pbPeopleFilter")
        self.horizontalLayout_3.addWidget(self.pbPeopleFilter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.cbStatus = QtWidgets.QComboBox(self.frame)
        self.cbStatus.setMinimumSize(QtCore.QSize(150, 0))
        self.cbStatus.setObjectName("cbStatus")
        self.horizontalLayout_3.addWidget(self.cbStatus)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cbLinkFrom = QtWidgets.QComboBox(self.frame)
        self.cbLinkFrom.setObjectName("cbLinkFrom")
        self.horizontalLayout_2.addWidget(self.cbLinkFrom)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cbLinkTo = QtWidgets.QComboBox(self.frame)
        self.cbLinkTo.setObjectName("cbLinkTo")
        self.horizontalLayout_2.addWidget(self.cbLinkTo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cbPeopleFrom = QtWidgets.QComboBox(self.frame)
        self.cbPeopleFrom.setObjectName("cbPeopleFrom")
        self.horizontalLayout.addWidget(self.cbPeopleFrom)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cbPeopleTo = QtWidgets.QComboBox(self.frame)
        self.cbPeopleTo.setObjectName("cbPeopleTo")
        self.horizontalLayout.addWidget(self.cbPeopleTo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 34))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.chb_mar = QtWidgets.QCheckBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chb_mar.sizePolicy().hasHeightForWidth())
        self.chb_mar.setSizePolicy(sizePolicy)
        self.chb_mar.setObjectName("chb_mar")
        self.horizontalLayout_9.addWidget(self.chb_mar)
        self.chb_dist = QtWidgets.QCheckBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chb_dist.sizePolicy().hasHeightForWidth())
        self.chb_dist.setSizePolicy(sizePolicy)
        self.chb_dist.setObjectName("chb_dist")
        self.horizontalLayout_9.addWidget(self.chb_dist)
        self.chb_child = QtWidgets.QCheckBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chb_child.sizePolicy().hasHeightForWidth())
        self.chb_child.setSizePolicy(sizePolicy)
        self.chb_child.setObjectName("chb_child")
        self.horizontalLayout_9.addWidget(self.chb_child)
        self.chb_home = QtWidgets.QCheckBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chb_home.sizePolicy().hasHeightForWidth())
        self.chb_home.setSizePolicy(sizePolicy)
        self.chb_home.setObjectName("chb_home")
        self.horizontalLayout_9.addWidget(self.chb_home)
        self.chb_edu = QtWidgets.QCheckBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chb_edu.sizePolicy().hasHeightForWidth())
        self.chb_edu.setSizePolicy(sizePolicy)
        self.chb_edu.setObjectName("chb_edu")
        self.horizontalLayout_9.addWidget(self.chb_edu)
        self.chb_baryg = QtWidgets.QCheckBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chb_baryg.sizePolicy().hasHeightForWidth())
        self.chb_baryg.setSizePolicy(sizePolicy)
        self.chb_baryg.setObjectName("chb_baryg")
        self.horizontalLayout_9.addWidget(self.chb_baryg)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_2 = QtWidgets.QFrame(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pbReLogin = QtWidgets.QPushButton(self.frame_2)
        self.pbReLogin.setObjectName("pbReLogin")
        self.horizontalLayout_4.addWidget(self.pbReLogin)
        self.pbRefresh = QtWidgets.QPushButton(self.frame_2)
        self.pbRefresh.setObjectName("pbRefresh")
        self.horizontalLayout_4.addWidget(self.pbRefresh)
        self.pbScan = QtWidgets.QPushButton(self.frame_2)
        self.pbScan.setObjectName("pbScan")
        self.horizontalLayout_4.addWidget(self.pbScan)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.cbHTML = QtWidgets.QComboBox(self.frame_2)
        self.cbHTML.setObjectName("cbHTML")
        self.horizontalLayout_4.addWidget(self.cbHTML)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pbGetHTML = QtWidgets.QPushButton(self.frame_2)
        self.pbGetHTML.setObjectName("pbGetHTML")
        self.horizontalLayout_4.addWidget(self.pbGetHTML)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.horizontalLayout_5.addWidget(self.widget_2)
        self.textEdit = QtWidgets.QTextEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_5.addWidget(self.textEdit)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.frame_3 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 380))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 380))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 360))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_6.addWidget(self.tableWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.cbLink = QtWidgets.QComboBox(self.frame_3)
        self.cbLink.setObjectName("cbLink")
        self.horizontalLayout_7.addWidget(self.cbLink)
        self.pbToAnketa = QtWidgets.QPushButton(self.frame_3)
        self.pbToAnketa.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pbToAnketa.setObjectName("pbToAnketa")
        self.horizontalLayout_7.addWidget(self.pbToAnketa)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.cbPeople = QtWidgets.QComboBox(self.frame_3)
        self.cbPeople.setObjectName("cbPeople")
        self.horizontalLayout_8.addWidget(self.cbPeople)
        self.pbToMessage = QtWidgets.QPushButton(self.frame_3)
        self.pbToMessage.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pbToMessage.setObjectName("pbToMessage")
        self.horizontalLayout_8.addWidget(self.pbToMessage)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(300, 300))
        self.label_3.setMaximumSize(QtCore.QSize(300, 300))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.anketa_html = QtWidgets.QTextBrowser(Form)
        self.anketa_html.setObjectName("anketa_html")
        self.verticalLayout_4.addWidget(self.anketa_html)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pbPeopleFilter.setText(_translate("Form", "Фильтровать"))
        self.label_2.setText(_translate("Form", "<---ОТ    Этап    ДО--->"))
        self.label.setText(_translate("Form", "<---ОТ   Тип   ДО--->"))
        self.chb_mar.setText(_translate("Form", "брак"))
        self.chb_dist.setText(_translate("Form", "расст"))
        self.chb_child.setText(_translate("Form", "дети"))
        self.chb_home.setText(_translate("Form", "дом"))
        self.chb_edu.setText(_translate("Form", "образов"))
        self.chb_baryg.setText(_translate("Form", "барыга"))
        self.pbReLogin.setText(_translate("Form", "Перезайти"))
        self.pbRefresh.setText(_translate("Form", "Обновить"))
        self.pbScan.setText(_translate("Form", "Сканировать"))
        self.pbGetHTML.setText(_translate("Form", "Get HTML"))
        self.pbToAnketa.setText(_translate("Form", "В анкету"))
        self.pbToMessage.setText(_translate("Form", "Сообщение"))
        self.label_3.setText(_translate("Form", "Будет Фото"))
        self.anketa_html.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

