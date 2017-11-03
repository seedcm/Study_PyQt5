class Readme:
    '''
    PyQt5中的组件（widgets）
    组件（widgets）是构建一个应用的基础模块。
    PyQt5有广泛的各式各样的组件，
    包含按钮，复选按钮，滑块条，和列表框。
    在这个部分的教程中，我们将学习几种有用的组件：
        复选按钮（QCheckBox）
        切换按钮（ToggleButton）
        滑块条（QSlider）
        进度条（ProgressBar）
        日历组件（QCalendarWidget）。

    复选框（QCheckBox）
    复选框组件有两种状态：
        选中和未选中。
        它是由一个选择框和一个标签组成的。
        一个应用中，复选框是典型的用来代表有效或无效状态的组件。

    在我们的例子中，我们创建了一个复选框，用来切换窗口标题。

    cb = QCheckBox('Show title', self)
        这是QCheckBox类的构造方法。

    cb.toggle()
        我们需要设置窗口标题，所以我们必须选中复选框。
        如果不选中复选框，默认情况下复选框不会被选中所以窗口标题也不会被设置。

    cb.stateChanged.connect(self.changeTitle)
        将我们自定义的changeTitle()槽方法和stateChanged信号连接。
        
    changeTitle()方法将用于切换窗口标题。

    def changeTitle(self, state):
        if state == Qt.Checked:
        self.setWindowTitle('QCheckBox')
    else:
        self.setWindowTitle('')
        复选框组件的状态会传入changeTitle()方法的state参数。
        如果复选框被选中，我们设置窗口标题。
        否则，我们把窗口标题设置成一个空字符串。
    '''

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):     
 
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
         
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()
         
         
    def changeTitle(self, state):
       
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')
             
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
