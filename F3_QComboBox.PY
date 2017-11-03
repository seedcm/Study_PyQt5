class Readme:
    '''
    下拉列表框（QComboBox）
    下拉列表框组件允许用户从列表中选择一个列表项。

    例子中显示了一个下拉列表框和一个标签。
    下拉列表框有五个列表项。
    这五个列表项都是Linux发行版的名字。
    标签组件显示在下拉列表框中选中的列表项的文本。

    combo = QComboBox(self)
    combo.addItem("Ubuntu")
    combo.addItem("Mandriva")
    combo.addItem("Fedora")
    combo.addItem("Arch")
    combo.addItem("Gentoo")
        我们创建一个下拉列表框并填充了五个列表项。

    combo.activated[str].connect(self.onActivated)
        一旦列表项被选中，会调用onActivated()方法。

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
        上面的方法，我们把下拉列表框中选中的列表项的文本显示在标签组件上。
        并且根据标签文本调整了标签大小。
    '''

import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
    QComboBox, QApplication)
 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):     
 
        self.lbl = QLabel("Ubuntu", self)
 
        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")
 
        combo.move(50, 50)
        self.lbl.move(50, 150)
 
        combo.activated[str].connect(self.onActivated)       
          
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()
         
         
    def onActivated(self, text):
       
        self.lbl.setText(text)
        self.lbl.adjustSize() 
         
                 
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
