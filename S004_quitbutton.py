class __Readme__:
    '''
    关闭窗口

    明显的关闭窗口的方法是点击标题栏的X标记。
    再下面的例子中，我们将展示怎么通过程序来关闭我们的窗口。
    我们将简单的触及信号和槽机制。

    QPushButton(string text, QWidget parent = None)
        text 参数是将显示在按钮中的内容。
        parent 参数是一个用来放置我们按钮的组件。
        在我们的例子中将会是QWidget组件。
        一个应用的组件是分层结构的。
        在这个分层内，大多数组件都有父类。
        没有父类的组件是顶级窗口。
    
    在这个例子中，我们创建一个退出按钮，一旦按下按钮，应用将会结束

    from PyQt5.QtCore import QCoreApplication
        我们需要一个来自QtCore的对象模块。

    qbtn = QPushButton('Quit',self)
        我们创建了一个按钮。
        按钮是一个QPushButton类的实例。
        构造方法的第一个参数是显示在button上的标签文本。
        第二个参数是父组件。
        父组件是Example组件，它继承了QWidget类。

    Qbtn.clicked.connect(QCoreApplication.instance().quit)
        在PyQt5中，事件处理系统由信号&槽机制建立。
        如果我们点击了按钮，信号clicked被发送。
        槽可以是Qt内置的槽或Python的一个方法调用。
        QCoreApplication类包含了主事件循环；它处理和转发所有事件。
        instance()方法给我们返回一个实例化对象。
        注意QCoreApplication类由QApplication创建。
        点击信号连接quit()方法，将结束应用。
        事件通信在两个对象之间进行：发送者和接受者。
        发送者是按钮，接受者是应用对象。
    '''

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        qbtn = QPushButton('Quit',self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
