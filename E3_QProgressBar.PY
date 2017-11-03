class Readme:
    '''
    PyQt5中的组件（widgets）
    组件（widgets）是构建一个应用的基础模块。
    PyQt5有广泛的各式各样的组件，包含按钮，复选按钮，滑块条，和列表框。
    在这个部分的教程中，我们将学习几种有用的组件：
        复选按钮（QCheckBox）
        切换按钮（ToggleButton）
        滑块条（QSlider）
        进度条（ProgressBar）
        日历组件（QCalendarWidget）

    进度条（QProgressBar）
    当我们处理耗时长的任务时，我们需要用到进度条组件。
    它通过动画的方式让我们了解任务正在处理中。
    在PyQt5中，进度条组件提供了横向和纵向的进度条选择。
    程序员可以设置进度条的最大值和最小值。
    进度条的默认值是0~99。

    在我们的例子中有一个横向进度条和一个按钮。
    按钮控制滑块条的开始和停止。

    self.pbar = QProgressBar(self)
        这是滑块条类的构造方法。

    self.timer = QtCore.QBasicTimer()
        我们用定时器对象来激活进度条。

    self.timer.start(100, self)
        为了开启定时器事件，我们调用了start()方法。
        这个方法有两个参数：
            定时时间和接收定时器事件的对象。

    def timerEvent(self, e):
       if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
         
    self.step = self.step + 1
    self.pbar.setValue(self.step)
        每个QObject类和它的子类都有timerEvent()事件处理函数用于处理定时事件。
        为了对定时器事件作出反馈，我们重新实现了这个事件处理函数。

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start') 
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
        在doAction()方法中，我们开始和停止定时器。
    '''
import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar,
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):     
 
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
 
        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)
 
        self.timer = QBasicTimer()
        self.step = 0
         
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()
         
         
    def timerEvent(self, e):
       
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
             
        self.step = self.step + 1
        self.pbar.setValue(self.step)
         
 
    def doAction(self):
       
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
             
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
