# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(798, 889)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cbStatus = QtWidgets.QComboBox(self.frame)
        self.cbStatus.setMinimumSize(QtCore.QSize(150, 0))
        self.cbStatus.setObjectName("cbStatus")
        self.horizontalLayout_3.addWidget(self.cbStatus)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pbPeopleFilter = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbPeopleFilter.sizePolicy().hasHeightForWidth())
        self.pbPeopleFilter.setSizePolicy(sizePolicy)
        self.pbPeopleFilter.setMinimumSize(QtCore.QSize(120, 0))
        self.pbPeopleFilter.setObjectName("pbPeopleFilter")
        self.horizontalLayout_3.addWidget(self.pbPeopleFilter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
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
        self.pbToAnketa = QtWidgets.QPushButton(self.frame_2)
        self.pbToAnketa.setObjectName("pbToAnketa")
        self.horizontalLayout_4.addWidget(self.pbToAnketa)
        self.pbToMessage = QtWidgets.QPushButton(self.frame_2)
        self.pbToMessage.setObjectName("pbToMessage")
        self.horizontalLayout_4.addWidget(self.pbToMessage)
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
        self.cbLink = QtWidgets.QComboBox(self.frame_3)
        self.cbLink.setObjectName("cbLink")
        self.verticalLayout_2.addWidget(self.cbLink)
        self.cbPeople = QtWidgets.QComboBox(self.frame_3)
        self.cbPeople.setObjectName("cbPeople")
        self.verticalLayout_2.addWidget(self.cbPeople)
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
        self.tableWidget.raise_()
        self.verticalLayout_4.addWidget(self.frame_3)
        self.widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 100))
        self.widget.setObjectName("widget")
        self.verticalLayout_4.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<---ОТ    Этап    ДО--->"))
        self.pbPeopleFilter.setText(_translate("Form", "Фильтровать"))
        self.label.setText(_translate("Form", "<---ОТ   Тип   ДО--->"))
        self.pbReLogin.setText(_translate("Form", "Перезайти"))
        self.pbRefresh.setText(_translate("Form", "Обновить"))
        self.pbScan.setText(_translate("Form", "Сканировать"))
        self.pbToAnketa.setText(_translate("Form", "В анкету"))
        self.pbToMessage.setText(_translate("Form", "Сообщение"))
        self.label_3.setText(_translate("Form", "Будет Фото"))

