class Readme:
    '''
    菜单栏可以集成所有命令，这样我们可以在应用中使用这些被集成的命令。
    工具栏提供了一个快速访问常用命令的方式。
    下面例子中，我们创建了一个简单的工具栏。
    工具栏有一个动作，当这个退出动作被触发时，应用将被中断。

    exitAction = QAction(QIcon('exit24.png'),'Exit',self)
    exitAction.setShortcut('Ctrl+Q')
    exitAction.triggered.connect(qApp.quit)
        我们创建了一个动作对象，和之前菜单栏中的部分代码相似。
        这个动作有一个标签、图标和快捷键。
        并且将QtGui.QMainWindow的quit()方法连接到了触发信号上。

    self.toolbar = self.addToolBar('Exit')
    self.toolbar.addAction(exitAction)
        我们这里创建了一个工具栏，并且在其中插入一个动作对象
    '''


import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
 
 
class Example(QMainWindow):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):              
         
        exitAction = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)
         
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
         
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')   
        self.show()
         
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

