# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui-elements/add-customers-table.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UiFrame(object):
    def setupUi(self, Frame):
        # Frame.setObjectName("Frame")
        # Frame.resize(702, 691)
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
        self.widget_3 = QtWidgets.QWidget(self.horizontalLayoutWidget)
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
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_4.setMinimumSize(QtCore.QSize(470, 0))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_4.setObjectName("widget_4")
        self.label_12 = QtWidgets.QLabel(self.widget_4)
        self.label_12.setGeometry(QtCore.QRect(60, 0, 101, 16))
        self.label_12.setObjectName("label_12")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.widget_4)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(0, 20, 461, 49))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_6 = QtWidgets.QFrame(self.horizontalLayoutWidget_6)
        self.frame_6.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_6.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        self.label_13.setGeometry(QtCore.QRect(0, 0, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(120, 75, 227, 255), stop:1 rgba(180, 239, 115, 255));")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.frame_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_6.addWidget(self.lineEdit_5)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_5.setObjectName("widget_5")
        self.label_14 = QtWidgets.QLabel(self.widget_5)
        self.label_14.setGeometry(QtCore.QRect(60, 0, 131, 16))
        self.label_14.setObjectName("label_14")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.widget_5)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(0, 20, 229, 49))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_7 = QtWidgets.QFrame(self.horizontalLayoutWidget_7)
        self.frame_7.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_7.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_15 = QtWidgets.QLabel(self.frame_7)
        self.label_15.setGeometry(QtCore.QRect(0, 0, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(120, 75, 227, 255), stop:1 rgba(180, 239, 115, 255));")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.frame_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_7.addWidget(self.lineEdit_6)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_6.setObjectName("widget_6")
        self.label_16 = QtWidgets.QLabel(self.widget_6)
        self.label_16.setGeometry(QtCore.QRect(60, 0, 181, 16))
        self.label_16.setObjectName("label_16")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.widget_6)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(0, 20, 301, 49))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_8 = QtWidgets.QFrame(self.horizontalLayoutWidget_8)
        self.frame_8.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_8.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_17 = QtWidgets.QLabel(self.frame_8)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(120, 75, 227, 255), stop:1 rgba(180, 239, 115, 255));")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_8.addWidget(self.frame_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_8.addWidget(self.lineEdit_7)
        self.verticalLayout.addWidget(self.widget_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(470, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        # Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "<html><head/><body><p>Задать значения для новой строки</p></body></html>"))
        self.label_10.setText(_translate("Frame", "Наименование организации / ФИО"))
        self.label_11.setText(_translate("Frame", "<html><head/><body><p align=\"center\">*</p></body></html>"))
        self.lineEdit_4.setText(_translate("Frame", "Иван Г."))
        self.label_12.setText(_translate("Frame", "Адрес клиента"))
        self.label_13.setText(_translate("Frame", "<html><head/><body><p align=\"center\">*</p></body></html>"))
        self.lineEdit_5.setText(_translate("Frame", "город Москва, просп. Вернадского, 78"))
        self.label_14.setText(_translate("Frame", "Контактный телефон"))
        self.label_15.setText(_translate("Frame", "<html><head/><body><p align=\"center\">*</p></body></html>"))
        self.lineEdit_6.setText(_translate("Frame", "79552156565"))
        self.label_16.setText(_translate("Frame", "Электронная почта E-mail"))
        self.label_17.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lineEdit_7.setText(_translate("Frame", "ivan.g@mirea.ru"))
        self.pushButton.setText(_translate("Frame", "Вставить запись"))
