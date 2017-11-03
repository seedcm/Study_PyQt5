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

    切换按钮
    切换按钮是QPushButton的特殊模式。
    切换按钮有两种状态：
        按下和没有按下。
        我们可以通过点击它在两种状态之间切换。
        下面的列子展示了切换按钮合适出现的情景。

    在我们的例子中，我们创建了三个切换按钮和一个QWidget组件。
    我们把QWidget组件的背景颜色设置为黑色。
    切换按钮将在红色，绿色和蓝色的RGB值部分进行切换。
    QWidget组件的背景颜色将取决于哪一个切换按钮被按下。

    self.col = QColor(0, 0, 0)
        这里是初始化，让RGB值为黑色。

    redb = QPushButton('Red', self)
    redb.setCheckable(True)
    redb.move(10, 10)
        要创建切换按钮，就要创建QPushButton，并且调用setCheckable()方法让它可被选中。

    redb.clicked[bool].connect(self.setColor)
        我们把clicked信号连接到我们定义的方法上。
        我们使用clicked信号来操作布尔值。

    source = self.sender()
        我们获得发生状态切换的按钮。

    if source.text() == "Red":
        self.col.setRed(val)
        在这种情况下，如果发生切换的是red按钮，我们更新RGB值中的红色部分的颜色值。

    self.square.setStyleSheet("QWidget { background-color: %s }" %  self.col.name())
        我们使用样式表来改变背景颜色。
    '''

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QFrame, QApplication)
from PyQt5.QtGui import QColor
 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):     
 
        self.col = QColor(0, 0, 0)      
 
        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)
 
        redb.clicked[bool].connect(self.setColor)
 
        redb = QPushButton('Green', self)
        redb.setCheckable(True)
        redb.move(10, 60)
 
        redb.clicked[bool].connect(self.setColor)
 
        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)
 
        blueb.clicked[bool].connect(self.setColor)
 
        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" % 
            self.col.name())
         
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()
         
         
    def setColor(self, pressed):
         
        source = self.sender()
         
        if pressed:
            val = 255
        else: val = 0
                         
        if source.text() == "Red":
            self.col.setRed(val)               
        elif source.text() == "Green":
            self.col.setGreen(val)            
        else:
            self.col.setBlue(val)
             
        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name()) 
        
        
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
