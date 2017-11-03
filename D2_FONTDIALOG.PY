class Readme:
    '''
    字体选择框
    QFontDialog是一个用于选择字体的对话框组件。
    在我们的例子中，我们有一个按钮和一个表情。
    通过字体选择对话框，我们可以改变标签的字体。

    font, ok = QFontDialog.getFont()
        在这儿我们弹出一个字体对话框。
        getFont()方法返回字体名字和布尔值。
        如果用户点击了OK，布尔值为True；否则为False。

    if ok:
        self.label.setFont(font)
        如果我们点击了Ok按钮，标签字体会被改变。
'''

import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
    QSizePolicy, QLabel, QFontDialog, QApplication)
 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):     
 
        vbox = QVBoxLayout()
 
        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed,
            QSizePolicy.Fixed)
         
        btn.move(20, 20)
 
        vbox.addWidget(btn)
 
        btn.clicked.connect(self.showDialog)
         
        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)
 
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)         
         
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()
         
         
    def showDialog(self):
 
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)
         
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

