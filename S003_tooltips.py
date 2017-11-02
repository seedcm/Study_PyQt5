class Readme:
    '''
    我们可以给我们的任何widget组件提供起泡帮组提示框。
    这个例子中，我们为两个PyQt5组件显示了提示框。

    QToolTip.setFont(QFont('yahei',10)
        这个静态方法设置了用语提示框的字体，我们用10px大小的YaHei字体。

    self.setToolTip('This is a <b>QWidget</b> widget')
        为了创建提示框，我们调用了setTooltip()方法，我们可以在提示框中使用富文本格式。

    btn = QPushButton('Button',self)
    btn.setToolTip('This is a <b>QPushButton</b> widget')
        我们创建了一个按钮组件并为它设置了一个提示框。

    btn.resize(btn.sizeHint())
    btn.move(50, 50)
        这里改变了按钮的大小，并移动了在窗口上的位置。setHint()方法给了按钮一个推荐的大小。
    '''

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('yahei',10))

        self.setToolTip('this is a <b>QWidget</b> widget')

        btn = QPushButton('Button',self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
