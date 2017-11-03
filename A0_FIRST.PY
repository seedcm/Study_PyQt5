#创建一个简单的窗口
#2017-11-2
#seedcm

class Readme:
    '''
    PyQt5教程
    这是一个显示一个小窗口的简单例子。
    我们可以做许多这样的窗口。
    我们可以调整它的窗口尺寸，最大化或最小化这个窗口。
    这些需求需要码很多代码。
    但一些人已经写好了这些功能实现。
    因为这些需求在很多应用中重复出现了，在这里我们不需要重新写这些代码。
    PyQt5是一个高级工具套件，为我们封装了很多复杂功能的实现代码，我们可以更加简单的通过函数去实现这些功能。
    如果我们是在一个低级工具套件中写代码的话，下面例子的代码很有可能需要数百行来实现。

    在屏幕上显示一个窗口的程序

        import sys
        from PyQt5.QtWidgets import QApplication
        from PyQt5.QtWidgets import QWidget
            导入必要模块，最基础的widget组件位于PyQt5.QtWidget模块中

        x = QApplication(sys.argv)
            所有PyQt5应用必须创建一个应用（Application）对象。sys.argv参数是一个来自命令行的参数列表。Python脚本可以在shell中运行。这是我们用来控制我们应用启动的一种方法。
    
        x = QApplication(sys.argv)
            所有PyQt5应用必须创建一个应用（Application）对象。sys.argv参数是一个来自命令行的参数列表。Python脚本可以在shell中运行。这是我们用来控制我们应用启动的一种方法。
    
        x = QWidget()
            Qwidget组件是PyQt5中所有用户界面类的基础类。我们给QWidget提供了默认的构造方法。默认构造方法没有父类。没有父类的widget组件将被作为窗口使用。
    
        x.resize(250, 150)
            resize()方法调整了widget组件的大小。它现在是250px宽，150px高。
    
        x.move(300, 300)
            move()方法移动widget组件到一个位置，这个位置是屏幕上x=300，y=300的坐标。

        x.setWindowTitle('First Window')
            设置窗口标题，这个标题显示在标题栏中。

        x.show()
            show()方法在屏幕上显示出widget。一个widget对象在这里第一次被在内存中创建，并且之后在屏幕上显示。
    
        sys.exit(app.exec_())
            最后，应用进入主循环。在这个地方，事件处理开始执行。主循环用于接收来自窗口触发的事件，并且转发他们到widget应用上处理。如果我们调用exit()方法或主widget组件被销毁，主循环将退出。sys.exit()方法确保一个不留垃圾的退出。系统环境将会被通知应用是怎样被结束的。

            exec_()方法有一个下划线。因为exec是Python保留关键字。因此，用exec_()来代替。
    '''

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    x = QWidget()
    x.resize(250, 150)
    x.move(300, 300)
    x.setWindowTitle('First Window')
    x.show()

    sys.exit(app.exec_())
 
