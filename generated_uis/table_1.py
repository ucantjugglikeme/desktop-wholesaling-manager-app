# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui-elements/table1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UiForm(object):
    def setupUi(self, Form):
        # Form.setObjectName("Form")
        # Form.resize(838, 682)
        self.horizontalLayoutWidgetT1 = QtWidgets.QWidget()
        self.horizontalLayoutWidgetT1.setGeometry(QtCore.QRect(0, 0, 831, 671))
        self.horizontalLayoutWidgetT1.setObjectName("horizontalLayoutWidgetT1")
        self.horizontalLayoutT1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidgetT1)
        self.horizontalLayoutT1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutT1.setObjectName("horizontalLayoutT1")
        self.frameT1 = QtWidgets.QFrame(self.horizontalLayoutWidgetT1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameT1.sizePolicy().hasHeightForWidth())
        self.frameT1.setSizePolicy(sizePolicy)
        self.frameT1.setMinimumSize(QtCore.QSize(0, 0))
        self.frameT1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frameT1.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.frameT1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameT1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameT1.setObjectName("frameT1")
        self.horizontalLayoutT1.addWidget(self.frameT1)
        self.verticalLayoutT1 = QtWidgets.QVBoxLayout()
        self.verticalLayoutT1.setObjectName("verticalLayoutT1")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidgetT1)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayoutT1.addWidget(self.label)
        self.horizontalLayoutT1.addLayout(self.verticalLayoutT1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        # Form.setWindowTitle(_translate("Form", "Form"))
