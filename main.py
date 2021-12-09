from os import replace
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLineEdit
from PyQt5.QtGui import QPixmap
import math
from PyQt5 import QtGui
import keyboard as kb
class Standard(QDialog):
    def __init__(self):
        super(Standard, self).__init__()
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
        self.inputArea.editingFinished.connect(self.Evaluate)
        self.remainder.clicked.connect(self.insertMod)
        self.history.clicked.connect(self.showhistory)
        self.hist=[]
        self.menuBtn.clicked.connect(self.gotomenu)
        kb.add_hotkey("1", self.insertNum1)
        kb.add_hotkey("2", self.insertNum2)
        kb.add_hotkey("3", self.insertNum3)
        kb.add_hotkey("4", self.insertNum4)
        kb.add_hotkey("5", self.insertNum5)
        kb.add_hotkey("6", self.insertNum6)
        kb.add_hotkey("7", self.insertNum7)
        kb.add_hotkey("8", self.insertNum8)
        kb.add_hotkey("9", self.insertNum9)
        kb.add_hotkey("0", self.insertNum0)
        kb.add_hotkey("Shift+8", self.insertMul)
        kb.add_hotkey("Shift+=", self.insertAdd)
        kb.add_hotkey("-", self.insertSub)
        kb.add_hotkey("/", self.insertDi)
        kb.add_hotkey("Shift+5", self.insertMod)
        kb.add_hotkey("Enter", self.Evaluate)
        kb.add_hotkey("Backspace", self.delLast)
        kb.add_hotkey("Shift+9", self.addOpenPst)
        kb.add_hotkey("Shift+0", self.addClosePst)
        kb.add_hotkey(".", self.insertPer)
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
        self.inputArea.setText(str(self.inputArea.text()) + "*100")
    
    def Evaluate(self):
        try:
            eqa = self.inputArea.text()
            if "π" in eqa:
                eqa = eqa.replace("π", (f'({math.pi})'))
 
            print(eqa)
            self.hist.append(eqa)
            self.summaryArea.setText(eqa)
            self.inputArea.setText(str(eval(eqa)))
        except:
            self.inputArea.setText("Invalid Expression")
    def showhistory(self):
        self.inputArea.setText(str(self.hist))
    def clearAll(self):
        print(str(self.inputArea.text()))
        self.inputArea.setText(str(""))
    
    def gotomenu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Scientific(QDialog):
    flag=1

    def __init__(self):
        super(Scientific, self).__init__()
        loadUi("scientific.ui",self)
        kb.add_hotkey("1", lambda: self.Signal('1'))
        kb.add_hotkey("2", lambda: self.Signal('2'))
        kb.add_hotkey("3", lambda: self.Signal('3'))
        kb.add_hotkey("4", lambda: self.Signal('4'))
        kb.add_hotkey("5", lambda: self.Signal('5'))
        kb.add_hotkey("6", lambda: self.Signal('6'))
        kb.add_hotkey("7", lambda: self.Signal('7'))
        kb.add_hotkey("8", lambda: self.Signal('8'))
        kb.add_hotkey("9", lambda: self.Signal('9'))
        kb.add_hotkey("0", lambda: self.Signal('0'))
        
        self.btn1.clicked.connect(lambda: self.Signal('C'))

        self.btn2.clicked.connect(lambda: self.Signal('7'))

        self.btn3.clicked.connect(lambda: self.Signal('8'))

        self.btn4.clicked.connect(lambda: self.Signal('9'))

        self.btn5.clicked.connect(lambda: self.Signal('+'))

        self.btn6.clicked.connect(lambda: self.Signal('del'))

        self.btn7.clicked.connect(lambda: self.Signal('4'))

        self.btn8.clicked.connect(lambda: self.Signal('5'))

        self.btn9.clicked.connect(lambda: self.Signal('6'))

        self.btn10.clicked.connect(lambda: self.Signal('-'))

        self.btn11.clicked.connect(lambda: self.Signal('math.sin('))

        self.btn12.clicked.connect(lambda: self.Signal('1'))

        self.btn13.clicked.connect(lambda: self.Signal('2'))

        self.btn14.clicked.connect(lambda: self.Signal('3'))

        self.btn15.clicked.connect(lambda: self.Signal('*'))

        self.btn16.clicked.connect(lambda: self.Signal('math.cos('))

        self.btn17.clicked.connect(lambda: self.Signal('math.log10('))

        self.btn18.clicked.connect(lambda: self.Signal('0'))

        self.btn19.clicked.connect(lambda: self.Signal('.'))

        self.btn20.clicked.connect(lambda: self.Signal('/'))

        self.btn21.clicked.connect(lambda: self.Signal('math.tan('))

        self.btn22.clicked.connect(lambda: self.Signal('math.log('))

        self.btn23.clicked.connect(lambda: self.Signal('math.factorial('))

        self.btn24.clicked.connect(lambda: self.Signal('Ans'))

        self.btn25.clicked.connect(lambda: self.Signal('math.e'))

        self.btn26.clicked.connect(lambda: self.Signal('('))

        self.btn27.clicked.connect(lambda: self.Signal(')'))

        self.btn28.clicked.connect(lambda: self.Signal('math.sqrt('))

        self.btn29.clicked.connect(lambda: self.Signal('='))

        self.menu.clicked.connect(self.gotomenu)

        self.show()
         
    
    def gotomenu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Signal(self,n):
        font3 = QtGui.QFont()
        font3.setPointSize(15)

        if Scientific.flag==1:
            global list,ans,Answer
            ans=" "
            list=[]
            Answer=" "
        if n=='Ans':
            list.append(Answer)
            ans=ans+'Ans'
            self.inputArea.setText(str(ans))
        else:
          if n!='=':
            if n!='del':
                if n!='C':
                   list.append(n)
                   if n[0]!='m':
                    ans=ans+n
                    self.inputArea.setText(str(ans))
                   else:
                     if n=='math.log10(':
                        ans=ans+'log('
                        self.inputArea.setText(str(ans))
                     elif n=='math.log(':
                             ans=ans+'ln('
                             self.inputArea.setText(str(ans))
                     else:
                          n=n[5:]
                          ans=ans+n
                          self.inputArea.setText(str(ans))

        if n=='C':
               list[:]=[]
               ans=""
               self.inputArea.clear()
        if n=='del':
                print(str(self.inputArea.text()))
                self.inputArea.setText(self.inputArea.text()[:len(self.inputArea.text())-1])

        if n=='=':
            
             self.inputArea.clear()
             st="".join(list)
             try:
                result=eval(st)    #USING EVAL FOR SOLVING MATH EXPRESSION STRING
                ans=str(result)
                Answer=str(result)
                ans=""
                list[:]=[]
                self.inputArea.setText(str(result))
             except (ValueError,SyntaxError,ZeroDivisionError):    #CATCHING INVALID FORMAT OR INVALID MATHEMATICS TERM
                  self.inputArea.clear()
                  self.inputArea.setFont(font3)
                  self.inputArea.setText("Invalid Format")

        Scientific.flag=2

class Menu(QDialog):
    def __init__(self):
        super(Menu, self).__init__()
        loadUi("menu.ui",self)
        self.std.clicked.connect(self.gotostd)
        self.sci.clicked.connect(self.gotosci)

    
    def gotostd(self):
        std = Standard()
        widget.addWidget(std)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def gotosci(self):
        sci = Scientific()
        widget.addWidget(sci)
        widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication(sys.argv)
calc = Standard()
widget = QtWidgets.QStackedWidget()
widget.addWidget(calc)
widget.setFixedHeight(807)
widget.setWindowOpacity(0.9)
widget.setFixedWidth(512)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
