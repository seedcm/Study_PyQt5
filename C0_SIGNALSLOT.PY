class Readme:
    '''
    事件
    所有的GUI应用都是事件驱动的。
    事件主要由应用的用户操作产生的。
    但是事件可能由其他条件触发，比如：
        一个网络连接，
        一个窗口管理器，
        一个定时器，
    这些动作都可能触发事件的产生。
    当我们调用应用的exec_()方法时，应用进入了主循环。
    主循环用于检测事件的产生并且将事件送到用于处理的对象中去。

    在事件模型，有三个参与者
        事件源
        事件对象
        事件目标
    事件源是状态发生改变的对象。它产生了事件。
    事件对象(evnet)封装了事件源中的状态变化。
    事件目标是想要被通知的对象。
    事件源对象代表了处理一个事件直到事件目标做出响应的任务。

    PyQt5有一个独一无二的信号和槽机制来处理事件。
    信号和槽用于对象之间的通信。
    当指定事件发生，一个事件信号会被发射。
    槽可以被任何Python脚本调用。
    当和槽连接的信号被发射时，槽会被调用。

    信号 & 槽
    这个例子演示了PyQt5中的信号和槽的使用。

    在我们的例子中，我们显示了一个QtGui.QLCDNumber和一个QtGui.QSlider类。
    我们拖动滑块条的把手，lcd数字会变化。

    sld.valueChanged.connect(lcd.display)
        这里，我们将滑块条的valueChanged信号和lcd数字显示的display槽连接在一起。
        发送者是一个发送了信号的对象。
        接受者是一个接受了信号的对象。
        槽是对信号做出反应的方法。
    '''


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication)
 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):
         
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
 
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
 
        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
         
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()
         
 
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
