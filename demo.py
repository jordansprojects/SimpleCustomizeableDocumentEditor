import sys
from WYSIWYGMenu import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
'''
 This is a simple demo class for showing you can import the WYSIWYGMenu 
'''
class TextEditorDemoBase(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(500,200,800,800)


    def initUI(self):
        # create text edit widget
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # create WYSIWYG toolbar, insert QTextEdit object as param
        toolbar = WYSIWYGMenu(self.text_edit)
        self.addToolBar(toolbar)

      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditorDemoBase()
    editor.show()
    sys.exit(app.exec_())
