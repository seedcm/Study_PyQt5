class Readme:
    '''
    布局管理-绝对定位
    程序指定了组件的位置并且每个组件的大小用像素作为单位来丈量。
    当你使用了绝对定位，我们需要知道下面的几点限制：
        如果我们改变了窗口大小，组件的位置和大小并不会发生改变。
        在不同平台上，应用的外观可能不同
        改变我们应用中的字体的话可能会把应用弄得一团糟。
        如果我们决定改变我们的布局，我们必须完全重写我们的布局，这样非常乏味和浪费时间。
        
    下面的例子中，使用了绝对坐标来定位组件。

    我们使用move()方法来定位我们的组件。
    在下面的例子中我们使用move()方法定位了一些标签组件。
    在使用move()方法时，我们给move()方法提供了x和y坐标作为参数。
    move()使用的坐标系统是从左上角开始计算的。
    x值从左到右增长，y值从上到下增长。

    lbl1 = QLabel('Zetcode',self)
    lbl1.move(15, 10)
        将标签组件定位在x=15, y=10的坐标位置。
    '''


import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):
         
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)
 
        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)
         
        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)       
         
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')   
        self.show()
         
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
