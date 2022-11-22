# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui-elements/add-products-table.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UiFrame(object):
    def setupUi(self, Frame):
        # Frame.setObjectName("Frame")
        # Frame.resize(905, 691)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 865, 671))
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
        self.tableWidget_2 = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget_2)
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
        self.widget_13 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_13.setObjectName("widget_13")
        self.label_46 = QtWidgets.QLabel(self.widget_13)
        self.label_46.setGeometry(QtCore.QRect(60, 0, 181, 16))
        self.label_46.setObjectName("label_46")
        self.horizontalLayoutWidget_23 = QtWidgets.QWidget(self.widget_13)
        self.horizontalLayoutWidget_23.setGeometry(QtCore.QRect(0, 20, 231, 49))
        self.horizontalLayoutWidget_23.setObjectName("horizontalLayoutWidget_23")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_23)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.frame_23 = QtWidgets.QFrame(self.horizontalLayoutWidget_23)
        self.frame_23.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_23.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.label_47 = QtWidgets.QLabel(self.frame_23)
        self.label_47.setGeometry(QtCore.QRect(0, 0, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(120, 75, 227, 255), stop:1 rgba(180, 239, 115, 255));")
        self.label_47.setObjectName("label_47")
        self.horizontalLayout_23.addWidget(self.frame_23)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_23)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_23.sizePolicy().hasHeightForWidth())
        self.lineEdit_23.setSizePolicy(sizePolicy)
        self.lineEdit_23.setMinimumSize(QtCore.QSize(171, 30))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.horizontalLayout_23.addWidget(self.lineEdit_23)
        self.verticalLayout.addWidget(self.widget_13)
        self.widget_16 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_16.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_16.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_16.setObjectName("widget_16")
        self.label_38 = QtWidgets.QLabel(self.widget_16)
        self.label_38.setGeometry(QtCore.QRect(60, 0, 101, 16))
        self.label_38.setObjectName("label_38")
        self.horizontalLayoutWidget_25 = QtWidgets.QWidget(self.widget_16)
        self.horizontalLayoutWidget_25.setGeometry(QtCore.QRect(0, 20, 231, 49))
        self.horizontalLayoutWidget_25.setObjectName("horizontalLayoutWidget_25")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_25)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.frame_25 = QtWidgets.QFrame(self.horizontalLayoutWidget_25)
        self.frame_25.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_25.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.label_50 = QtWidgets.QLabel(self.frame_25)
        self.label_50.setGeometry(QtCore.QRect(0, 0, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(120, 75, 227, 255), stop:1 rgba(180, 239, 115, 255));")
        self.label_50.setObjectName("label_50")
        self.horizontalLayout_25.addWidget(self.frame_25)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_24.sizePolicy().hasHeightForWidth())
        self.lineEdit_24.setSizePolicy(sizePolicy)
        self.lineEdit_24.setMinimumSize(QtCore.QSize(171, 30))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.horizontalLayout_25.addWidget(self.lineEdit_24)
        self.verticalLayout.addWidget(self.widget_16)
        self.widget_14 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_14.setObjectName("widget_14")
        self.label_40 = QtWidgets.QLabel(self.widget_14)
        self.label_40.setGeometry(QtCore.QRect(60, 0, 131, 16))
        self.label_40.setObjectName("label_40")
        self.horizontalLayoutWidget_20 = QtWidgets.QWidget(self.widget_14)
        self.horizontalLayoutWidget_20.setGeometry(QtCore.QRect(0, 20, 191, 49))
        self.horizontalLayoutWidget_20.setObjectName("horizontalLayoutWidget_20")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_20)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.frame_20 = QtWidgets.QFrame(self.horizontalLayoutWidget_20)
        self.frame_20.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_20.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.label_41 = QtWidgets.QLabel(self.frame_20)
        self.label_41.setGeometry(QtCore.QRect(0, 0, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(120, 75, 227, 255), stop:1 rgba(180, 239, 115, 255));")
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_20.addWidget(self.frame_20)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_25.sizePolicy().hasHeightForWidth())
        self.lineEdit_25.setSizePolicy(sizePolicy)
        self.lineEdit_25.setMinimumSize(QtCore.QSize(131, 30))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.horizontalLayout_20.addWidget(self.lineEdit_25)
        self.verticalLayout.addWidget(self.widget_14)
        self.widget_15 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_15.setObjectName("widget_15")
        self.label_44 = QtWidgets.QLabel(self.widget_15)
        self.label_44.setGeometry(QtCore.QRect(60, 0, 181, 16))
        self.label_44.setObjectName("label_44")
        self.horizontalLayoutWidget_22 = QtWidgets.QWidget(self.widget_15)
        self.horizontalLayoutWidget_22.setGeometry(QtCore.QRect(0, 20, 191, 49))
        self.horizontalLayoutWidget_22.setObjectName("horizontalLayoutWidget_22")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_22)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.frame_22 = QtWidgets.QFrame(self.horizontalLayoutWidget_22)
        self.frame_22.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_22.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.label_45 = QtWidgets.QLabel(self.frame_22)
        self.label_45.setGeometry(QtCore.QRect(0, 0, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(120, 75, 227, 255), stop:1 rgba(180, 239, 115, 255));")
        self.label_45.setObjectName("label_45")
        self.horizontalLayout_22.addWidget(self.frame_22)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_26.sizePolicy().hasHeightForWidth())
        self.lineEdit_26.setSizePolicy(sizePolicy)
        self.lineEdit_26.setMinimumSize(QtCore.QSize(131, 30))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.horizontalLayout_22.addWidget(self.lineEdit_26)
        self.verticalLayout.addWidget(self.widget_15)
        self.widget_12 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_12.setObjectName("widget_12")
        self.label_42 = QtWidgets.QLabel(self.widget_12)
        self.label_42.setGeometry(QtCore.QRect(60, 0, 181, 16))
        self.label_42.setObjectName("label_42")
        self.horizontalLayoutWidget_21 = QtWidgets.QWidget(self.widget_12)
        self.horizontalLayoutWidget_21.setGeometry(QtCore.QRect(0, 20, 191, 49))
        self.horizontalLayoutWidget_21.setObjectName("horizontalLayoutWidget_21")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_21)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.frame_21 = QtWidgets.QFrame(self.horizontalLayoutWidget_21)
        self.frame_21.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_21.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.label_43 = QtWidgets.QLabel(self.frame_21)
        self.label_43.setGeometry(QtCore.QRect(0, 0, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(120, 75, 227, 255), stop:1 rgba(180, 239, 115, 255));")
        self.label_43.setObjectName("label_43")
        self.horizontalLayout_21.addWidget(self.frame_21)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_27.sizePolicy().hasHeightForWidth())
        self.lineEdit_27.setSizePolicy(sizePolicy)
        self.lineEdit_27.setMinimumSize(QtCore.QSize(131, 30))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.horizontalLayout_21.addWidget(self.lineEdit_27)
        self.verticalLayout.addWidget(self.widget_12)
        self.widget_11 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_11.setObjectName("widget_11")
        self.label_48 = QtWidgets.QLabel(self.widget_11)
        self.label_48.setGeometry(QtCore.QRect(60, 0, 181, 16))
        self.label_48.setObjectName("label_48")
        self.horizontalLayoutWidget_24 = QtWidgets.QWidget(self.widget_11)
        self.horizontalLayoutWidget_24.setGeometry(QtCore.QRect(0, 20, 191, 49))
        self.horizontalLayoutWidget_24.setObjectName("horizontalLayoutWidget_24")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_24)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.frame_24 = QtWidgets.QFrame(self.horizontalLayoutWidget_24)
        self.frame_24.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_24.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.label_49 = QtWidgets.QLabel(self.frame_24)
        self.label_49.setGeometry(QtCore.QRect(0, 0, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(120, 75, 227, 255), stop:1 rgba(180, 239, 115, 255));")
        self.label_49.setObjectName("label_49")
        self.horizontalLayout_24.addWidget(self.frame_24)
        self.lineEdit_28 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_28.sizePolicy().hasHeightForWidth())
        self.lineEdit_28.setSizePolicy(sizePolicy)
        self.lineEdit_28.setMinimumSize(QtCore.QSize(131, 30))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.horizontalLayout_24.addWidget(self.lineEdit_28)
        self.verticalLayout.addWidget(self.widget_11)
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
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(250, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        self.widget_18 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_18.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_18.setObjectName("widget_18")
        self.label_52 = QtWidgets.QLabel(self.widget_18)
        self.label_52.setGeometry(QtCore.QRect(100, 0, 111, 16))
        self.label_52.setObjectName("label_52")
        self.horizontalLayoutWidget_26 = QtWidgets.QWidget(self.widget_18)
        self.horizontalLayoutWidget_26.setGeometry(QtCore.QRect(20, 20, 231, 49))
        self.horizontalLayoutWidget_26.setObjectName("horizontalLayoutWidget_26")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_26)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.frame_26 = QtWidgets.QFrame(self.horizontalLayoutWidget_26)
        self.frame_26.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_26.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.label_53 = QtWidgets.QLabel(self.frame_26)
        self.label_53.setGeometry(QtCore.QRect(0, 0, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(120, 75, 227, 255), stop:1 rgba(180, 239, 115, 255));")
        self.label_53.setObjectName("label_53")
        self.horizontalLayout_26.addWidget(self.frame_26)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_29.sizePolicy().hasHeightForWidth())
        self.lineEdit_29.setSizePolicy(sizePolicy)
        self.lineEdit_29.setMinimumSize(QtCore.QSize(171, 30))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.horizontalLayout_26.addWidget(self.lineEdit_29)
        self.verticalLayout_9.addWidget(self.widget_18)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_54 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_54.setStyleSheet("")
        self.label_54.setText("")
        self.label_54.setObjectName("label_54")
        self.verticalLayout_10.addWidget(self.label_54)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(470, 16777215))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_9.addWidget(self.pushButton_4)
        self.horizontalLayout.addLayout(self.verticalLayout_9)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        # Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "<html><head/><body><p>Задать значения для</p></body></html>"))
        self.label_46.setText(_translate("Frame", "Наименование товара"))
        self.label_47.setText(_translate("Frame", "<html><head/><body><p align=\"center\">*</p></body></html>"))
        self.lineEdit_23.setText(_translate("Frame", "Конфеты \"Калужские\""))
        self.label_38.setText(_translate("Frame", "Стоимость товара"))
        self.label_50.setText(_translate("Frame", "<html><head/><body><p align=\"center\">*</p></body></html>"))
        self.lineEdit_24.setText(_translate("Frame", "159.99"))
        self.label_40.setText(_translate("Frame", "Кол-во товара"))
        self.label_41.setText(_translate("Frame", "<html><head/><body><p align=\"center\">*</p></body></html>"))
        self.lineEdit_25.setText(_translate("Frame", "86"))
        self.label_44.setText(_translate("Frame", "ID категории товара"))
        self.label_45.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_42.setText(_translate("Frame", "ID склада"))
        self.label_43.setText(_translate("Frame", "<html><head/><body><p align=\"center\">*</p></body></html>"))
        self.lineEdit_27.setText(_translate("Frame", "1"))
        self.label_48.setText(_translate("Frame", "ID поставщика"))
        self.label_49.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton.setText(_translate("Frame", "Вставить запись"))
        self.label_4.setText(_translate("Frame", "<html><head/><body><p>новой строки</p></body></html>"))
        self.label_52.setText(_translate("Frame", "Категория товара"))
        self.label_53.setText(_translate("Frame", "<html><head/><body><p align=\"center\">*</p></body></html>"))
        self.lineEdit_29.setText(_translate("Frame", "Кондитерские изделия сахаристые"))
        self.pushButton_4.setText(_translate("Frame", "Вставить запись"))