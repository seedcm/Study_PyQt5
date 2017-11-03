class Readme:
    '''
    分割框（QSplitter）
    分割框组件让我们通过拖拽分割线来控制子组件的大小。
    在我们的例子中，我们显示由两个分割框组件约束的三个QFrame组件。

    在我们的例子中，我们有三个框架组件和两个分割框组件。
    注意在某些主题下，分割框组件可能不会被显示。

    topleft = QFrame(self)
    topleft.setFrameShape(QFrame.StyledPanel)
        我们使用了一个样式框架，为了让框架组件之间的分割线看的明显。

    splitter1 = QSplitter(Qt.Horizontal)
    splitter1.addWidget(topleft)
    splitter1.addWidget(topright)
        我们创建了一个分割框组件并且在这个分割框中添加进入两个框架组件。

    splitter2 = QSplitter(Qt.Vertical)
    splitter2.addWidget(splitter1)
        我们把第一个分割框添加进另一个分割框组件中。
    '''

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
    QSplitter, QStyleFactory, QApplication)
from PyQt5.QtCore import Qt
 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):     
 
        hbox = QHBoxLayout(self)
 
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
  
        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)
 
        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)
 
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
 
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
 
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
         
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()
         
         
    def onChanged(self, text):
         
        self.lbl.setText(text)
        self.lbl.adjustSize()       
         
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
