import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLineEdit
from PyQt5.QtGui import QPixmap

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("standard.ui",self)
        self.num1.clicked.connect(self.insertNum1)
        self.num2.clicked.connect(self.insertNum2)
        self.num3.clicked.connect(self.insertNum3)
        self.num4.clicked.connect(self.insertNum4)
        self.num5.clicked.connect(self.insertNum5)
        self.num6.clicked.connect(self.insertNum6)
        self.num7.clicked.connect(self.insertNum7)
        self.num8.clicked.connect(self.insertNum8)
        self.num9.clicked.connect(self.insertNum9)
        self.num0.clicked.connect(self.insertNum0)
        self.period.clicked.connect(self.insertPer)

        self.add.clicked.connect(self.insertAdd)
        self.subtract.clicked.connect(self.insertSub)
        self.multiply.clicked.connect(self.insertMul)
        self.divide.clicked.connect(self.insertDi)

        self.ptsOpen.clicked.connect(self.addOpenPst)
        self.ptsClose.clicked.connect(self.addClosePst)

        self.ClearAll.clicked.connect(self.clearAll)
        self.delete_2.clicked.connect(self.delLast)

        self.pi.clicked.connect(self.insertPi)
        self.root.clicked.connect(self.SqrRoot)
        self.equals.clicked.connect(self.Evaluate)




    def insertNum1(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "1")

    def insertNum2(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "2")

    def insertNum3(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "3")

    def insertNum4(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "4")

    def insertNum5(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "5")

    def insertNum6(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "6")

    def insertNum7(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "7")

    def insertNum8(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "8")

    def insertNum9(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "9")

    def insertNum0(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "0")
    
    def insertAdd(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "+")
    
    def insertSub(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "-")
    
    def insertMul(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "*")
    
    def insertDi(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "/")

    
    def addOpenPst(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "(")
    

    def addClosePst(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + ")")
    
    def delLast(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(self.inputArea.text()[:len(self.inputArea.text())-1])

    def SqrRoot(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "√")
    
    def insertPi(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "π")
    
    def insertPer(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + ".")
    
    def insertMod(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(self.inputArea.text()) + "%")
    
    def Evaluate(self):
        try:
            eqa = self.inputArea.text()
            self.summaryArea.setText(eqa)
            self.inputArea.setText(str(eval(eqa)))
        except:
            self.inputArea.setText("Invalid Expression")

    def clearAll(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(""))
    


app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(807)
widget.setWindowOpacity(0.9)
widget.setFixedWidth(512)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
