class Readme:
    '''
    message box
    默认的，如果我们点击了标题栏上的X按钮，QWidget会被关闭。
    可是我们希望通过一个message box来确认这个动作。

    如果我们关闭一个QWidget， QCloseEvent类事件将被生成。
    要修改组件动作我们需要重新实现closeEvent()时间处理方法。

    reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        我们实现一个带两个按钮的message box: YES和NO按钮。
        代码中第一个字符串的内容被显示在标题栏上。
        第二个字符串是对话框上显示的文本。
        第三个参数指定了显示在对话框的按钮集合。
        最后一个参数是默认选中的按钮。
        这个按钮一开始就获得焦点。
        返回值被储存在reply变量中。

    if reply == QtGui.QMessageBox.Yes:
        event.accept()
    else:
        event.ignore()
        在这里我们测试一下返回值。
        代码逻辑是，如果我们点击Yes按钮，我们接收到的事件关闭事件，这将导致了组件的关闭和应用的技术。
        否则不是点击Yes按钮的话我们将忽略关闭事件。
    '''

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
