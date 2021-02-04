from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from imagepr import *

form_class = uic.loadUiType("guiform.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(622, 484)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(550, 10, 61, 51))
        self.pushButton.setObjectName("pushButton")

        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 70, 601, 401))
        self.textBrowser.setObjectName("textBrowser")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 31))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 19, 381, 31))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.pushButton2 = QtWidgets.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(480, 20, 51, 31))
        self.pushButton2.setObjectName("toolButton")

        self.retranslateUi(Form)
        self.connection()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "변환"))
        self.label.setText(_translate("Form", "  경로:"))
        self.pushButton2.setText(_translate("Form", "..."))
    
    def push1c(self):
        ip = ImageProcess(self.label_2.text())
        ip.preProcess()

        op = OcrProcess(ip.grayscal_img)
        op.process()
        self.textBrowser.clear()
        self.textBrowser.append(op.textdata)



    def push2c(self):
        fname = QFileDialog.getOpenFileName()
        self.label_2.setText(fname[0])
    
    def connection(self):
        self.pushButton.clicked.connect(self.push1c)
        self.pushButton2.clicked.connect(self.push2c)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
