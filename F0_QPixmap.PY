class Readme:
    '''
    像素图（QPixmap）
    像素图（QPixmap）是各种用于处理图像的组件中的一个。
    它是在屏幕上显示图片的最佳选择。
    在我们代码例子中，我们将使用像素图来在窗口上显示一个图片。

    运行这个例子，我们会把一个图片显示在窗口上。

    pixmap = QPixmap("redrock.png")
        创建QPixmap对象。该对象构造方法传入一个文件的名字作为参数。

    lbl = QLabel(self)
    lbl.setPixmap(pixmap)
        我们把像素图对象设置给标签，从而通过标签来显示像素图。
    '''

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap
 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):     
 
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("redrock.png")
 
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
 
        hbox.addWidget(lbl)
        self.setLayout(hbox)
         
        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()       
         
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
