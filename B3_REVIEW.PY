class Readme:
    '''
    在网格中，组件可以跨多列或多行。
    在这个例子中，我们对它进行一下说明。
    我们创建了包含三个标签，两个单行编辑框和一个文本编辑框组件的窗口。
    布局使用了QGridLayout布局。

    grid = QGridLayout()
    grid.setSpacing(10)
        我们创建了一个网格布局并且设置了组件之间的间距。

    grid.addWidget(reviewEdit, 3, 1, 5 ,1)
        如果我们向网格布局中增加一个组件，我们可以提供组件的跨行和跨列参数。
        在这个例子中，我们让reviewEdit组件垮了5行。
    '''


import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication)
 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):
         
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')
 
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()
 
        grid = QGridLayout()
        grid.setSpacing(10)
 
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
 
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
 
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
         
        self.setLayout(grid)
         
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')   
        self.show()
         
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

