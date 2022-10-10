from PyQt5 import QtCore


class LabelSignal(QtCore.QObject):
    clicked = QtCore.pyqtSignal()

    def __init__(self):
        QtCore.QObject.__init__(self)

    def click(self):
        self.clicked.emit()
