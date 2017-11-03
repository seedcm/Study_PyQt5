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

    日历组件（QCalendarWidget）
        QCalendarWidget类提供了一个基于月的日历组件。
        它允许用户通过简单的直观的方式选择日期。

    以下的例子展示一个日历组件和标签组件。
    功能是日历中选择的日期会显示在标签组件中。

    cal = QCalendarWidget(self)
        创建QCalendarWidget类。

    cal.clicked[QDate].connect(self.showDate)
        如果我们在组件上选择了一个日期，clicked[QDate] 信号会被发射。
        我们把这个信号和自定义的showDate()方法连接。

    def showDate(self, date):    
    self.lbl.setText(date.toString())
        我们通过selectedDate()方法检索被选中的日期。
        然后我们把选中的日期对象转化成字符串显示在标签组件上。

    '''

import sys
from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
    QLabel, QApplication)
from PyQt5.QtCore import QDate
 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):     
 
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)
         
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)
         
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()
         
         
    def showDate(self, date):    
         
        self.lbl.setText(date.toString())
         
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


