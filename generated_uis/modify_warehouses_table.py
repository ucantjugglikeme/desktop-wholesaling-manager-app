# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui-elements/modify-warehouses-table.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UiFrame(object):
    def setupUi(self, Frame):
        # Frame.setObjectName("Frame")
        # Frame.resize(840, 641)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 691, 671))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.frame = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.frame.setMinimumSize(QtCore.QSize(100, 0))
        self.frame.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.widget_7 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_7.setObjectName("widget_7")
        self.label_18 = QtWidgets.QLabel(self.widget_7)
        self.label_18.setGeometry(QtCore.QRect(60, 0, 181, 16))
        self.label_18.setObjectName("label_18")
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.widget_7)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(0, 20, 331, 49))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_9 = QtWidgets.QFrame(self.horizontalLayoutWidget_9)
        self.frame_9.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_9.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_19 = QtWidgets.QLabel(self.frame_9)
        self.label_19.setGeometry(QtCore.QRect(0, 0, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.130955, y1:0.347, x2:0.130636, y2:0.682, stop:0 rgba(200, 104, 0, 255), stop:1 rgba(205, 183, 84, 255));")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_9.addWidget(self.frame_9)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_9)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_9.addWidget(self.comboBox)
        self.verticalLayout.addWidget(self.widget_7)
        self.widget_3 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_3.setMinimumSize(QtCore.QSize(470, 0))
        self.widget_3.setObjectName("widget_3")
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(60, 0, 181, 16))
        self.label_10.setObjectName("label_10")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.widget_3)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 20, 301, 49))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.horizontalLayoutWidget_5)
        self.frame_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_5.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(120, 75, 227, 255), stop:1 rgba(180, 239, 115, 255));")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.frame_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.checkBox = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox.setGeometry(QtCore.QRect(390, 30, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.widget_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.frame_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(0, 40, 221, 23))
        self.pushButton.setMaximumSize(QtCore.QSize(470, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 40, 221, 23))
        self.pushButton_2.setMaximumSize(QtCore.QSize(470, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        # Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "<html><head/><body><p>Задать новые значения</p></body></html>"))
        self.label_18.setText(_translate("Frame", "ID склада"))
        self.label_19.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_10.setText(_translate("Frame", "Адрес склада"))
        self.label_11.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lineEdit_4.setText(_translate("Frame", "город Москва, просп. Вернадского, 78"))
        self.checkBox.setText(_translate("Frame", "Заменить"))
        self.pushButton.setText(_translate("Frame", "Проверить записи"))
        self.pushButton_2.setText(_translate("Frame", "Изменить записи"))
