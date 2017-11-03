class Readme:
    '''
    事件发送者
    有时需要方便的知道哪一个组件是信号发送者。
    因此，PyQt5拥有了sender()方法来解决这个问题。

    在我们的例子中，我们有两个按钮。
    在buttonClikced()方法中，我们调用sender()方法来判断哪一个按钮是我们按下的。

    btn1.clicked.connect(self.buttonClicked)           
    btn2.clicked.connect(self.buttonClicked)
        两个按钮都连接到了同一个槽中。

    def buttonClicked(self):
    sender = self.sender()
    self.statusBar().showMessage(sender.text() + ' was pressed')
        我们调用sender()方法判断发送信号的信号源是哪一个。
        然后在应用的状态栏上显示被按下的按钮的标签内容。
    '''


import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
 
 
class Example(QMainWindow):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):     
 
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)
 
        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)
       
        btn1.clicked.connect(self.buttonClicked)           
        btn2.clicked.connect(self.buttonClicked)
         
        self.statusBar()
         
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()
         
         
    def buttonClicked(self):
       
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
         
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
