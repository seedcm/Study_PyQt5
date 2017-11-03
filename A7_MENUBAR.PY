class Readme:
    '''
    菜单栏
    菜单栏是GUI应用的常规组成部分。
    是位于各种菜单中的一组命令操作。
    
    menubar.setNativeMenuBar(False)
        （Mac OS 对待菜单栏有些不同）
        为了获得全平台一致性的效果，可以在代码中加入这行代码。

    下面的例子中，我们创建了一个有菜单项的菜单栏。
    这个菜单项包含一个选中后中断应用的动作。

    exitAction = QAction(QIcon('exit.png'),'&Exit',self)
    exitAction.setShortcut('Ctrl+Q')
    exitAction.setStatusTip('Exit application')
        QAction是一个用于菜单栏、工具栏或者自定义快捷键的抽象动作行为。
        在上面的三行中，我们创建了一个有指定图标和文本为‘Exit’的标签。
        另外，还未这个动作定义了一个快捷键。
        第三行创建一个当我们鼠标浮于菜单项之上就会显示的一个状态提示。

    exitAction.triggered.connect(qApp.quit)
        当我们选中特定的东西做，一个出发信号就会被发射。
        信号链接到QApplication组件的quit()方法，这样就中断了应用。

    menubar = self.menuBar()
    fileMenu = menubar.addMenu('&File')
    fileMenu.addAction(exitAction)
        menuBar()方法创建了一个菜单栏。
        我们创建一个file菜单，然后将推出动作添加到file菜单中。
    '''

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
 
 
class Example(QMainWindow):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):              
         
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)       
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
 
        self.statusBar()
 
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
         
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')   
        self.show()
         
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

