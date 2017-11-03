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
        日历组件（QCalendarWidget）。

    滑块条(QSlider)
    滑块条(QSlider)组件有一个简单的可调节手柄。
    这个手柄可以前后拖动。
    我们可以使用这个方式来选择具体的数值。
    有时使用滑块条比直接输入数字或使用数值选择框更自然，在我们下面的例子中，我们将显示一个滑块条和一个标签。
    标签将会显示一个图像。
    滑块条将控制标签。

    在我们的例子中，我们模拟了一个音量控制器。
    通过拖动滑块条的把手，我们可以改变标签的图像。

    sld = QSlider(Qt.Horizontal, self)
        这里我们创建了一个横向的滑块条。

    self.label = QLabel(self)
    self.label.setPixmap(QPixmap('mute.png'))
        我们创建了一个标签组件，并且设置一个初始的无声图片。

    sld.valueChanged[int].connect(self.changeValue)
        我们把valueChanged 信号连接到我们自定义的 changeValue()方法上。

    if value == 0:
        self.label.setPixmap(QPixmap('mute.png'))
        ...
        这里实现了根据滑块条的值，我们设置不同的标签图片。
        在上面的代码中，如果滑块条的值等于零，我们为标签设置mute.png图片。
    '''

import sys
from PyQt5.QtWidgets import (QWidget, QSlider,
    QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):     
 
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)
         
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.png'))
        self.label.setGeometry(160, 40, 80, 30)
         
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()
         
         
    def changeValue(self, value):
 
        if value == 0:
            self.label.setPixmap(QPixmap('mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('med.png'))
        else:
            self.label.setPixmap(QPixmap('max.png'))
             
 
if __name__ == '__main__':
 
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
