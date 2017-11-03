#窗口居中
#2017-11-3
#seedcm

class Readme:
    '''
    将窗口居中显示在屏幕上
    QtGui.QDesktopWidget类提供了我们桌面窗口的信息，包含了屏幕尺寸。
    
    self.center()
        将窗口居中放置的代码在自定义的center()方法中。

    qr = self.frameGeometry()
        我们获得主窗口的一个矩形待定几何图形，这包含了窗口的框架。

    cp = QDesktopWidget().availableGeometry().center()
        我们算出相对于显示器的绝对值，并且从这个绝对值中，我们获得了屏幕中心点。

    qr.move(cp)
        我们的矩形已经设置好了它的宽和高，现在我们把矩形的中心设置到屏幕的中间去，矩形的大小并不会改变。

    self.move(qr.topLeft())
        我们移动了应用窗口的左上方的点到qr矩形的左上方的点，因此居中显示在屏幕上。
    '''

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):              
         
        self.resize(250, 150)
        self.center()
         
        self.setWindowTitle('Center')   
        self.show()
         
         
    def center(self):
         
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
         
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_()) 
