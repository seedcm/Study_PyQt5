class Readme:
    '''
    箱布局
    布局管理器的布局管理类非常灵活，实用。
    它是将组件定位在窗口上的首选方式。
    QHBoxLayout和QVBoxLayout是两个基础布局管理类，他们水平或垂直的线性排列组件。
    想象一下我们需要在右下角排列两个按钮。
    为了使用箱布局，我们将使用一个水平箱布局和垂直箱布局来实现。
    同样为了使用一些必要的空白，我们将添加一些拉伸因子。

    例子在右下角放置了两个按钮。
    当我们改变应用窗口大小时，它们会相对于应用窗口不改变位置。
    在这个例子中我们使用了QHBoxLayout和QVBoxLayout两个布局类。

    okButton = QPushButton('Ok')
    cancelButton = QPushButton('Cancel')
        这里我们创建了两个按钮

    hbox = QHBoxLayout()
    hbox.addStretch(1)
    hbox.addWidget(okButton)
    hbox.addWdiget(cancelButton)
        这里我们创建了一个水平箱布局，并且增加了一个拉伸因子和两个按钮。
        拉伸因子在两个按钮之间增加了一个可伸缩空间。
        这会将按钮推到窗口的右边。

    vbox = QVBoxLayout()
    vbox.addStretch(1)
    vbox.addLayout(hbox)
        为了创建必要的布局，我们把水平布局放置在垂直布局内。
        拉伸因子将把包含两个按钮的水平箱布局推到窗口的底边。

    self.setLayout(vbox)
        最后，我们设置一下窗口的主布局。
    '''

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication)
 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):
         
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
 
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
 
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
         
        self.setLayout(vbox)   
         
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')   
        self.show()
         
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

