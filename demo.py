import sys
from WYSIWYGMenu import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import docx
import docx2txt
'''

'''
class TextEditorBase(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(500,200,900,800)

    def initUI(self):
       # Create a menu bar with 
        open_file_action = QAction("File open", self)
        open_file_action.triggered.connect(self.open_docx_file)
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(open_file_action)

       # Create a menu bar with a "Open Image" action
        open_image_action = QAction("Open Image", self)
        open_image_action.triggered.connect(self.open_image)
        file_menu = self.menuBar().addMenu("Customize")
        file_menu.addAction(open_image_action)


        #Setup Layout
        layout = QHBoxLayout()
        widget = QWidget(self)
        widget.setLayout(layout)

        # create text edit widget
        self.text_edit = QTextEdit()
        self.text_edit.setFixedSize(700, 770)
        # add scrollbar to text edit widget
        scrollbar = QScrollBar(Qt.Vertical, self.text_edit)
        scrollbar.setGeometry(540,20,20,360)
        self.text_edit.setVerticalScrollBar(scrollbar)

        # create spacer   
        spacer= QSpacerItem(0,0, QSizePolicy.Expanding, QSizePolicy.Minimum)
       
        # add a spacer to the left
        layout.addItem(spacer)
       
        # set size policy to fixed so it doesnt change size
        self.text_edit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed) 
        
        # add text edit widget to the layout
        layout.addWidget(self.text_edit)
        
        # add a spacer to the right
        layout.addItem(spacer)

        # set widget as central
        self.setCentralWidget(widget)
        
        # create WYSIWYG toolbar, insert QTextEdit object as param
        toolbar = WYSIWYGMenu(self.text_edit)
        self.addToolBar(toolbar)


   # Opens file explorer so that the user can pick a background image
    def open_image(self):
        # Open a file dialog to select an image file
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Image Files (*.png *.jpg *.bmp)")
        if file_dialog.exec_() == QFileDialog.Accepted:
            filename = file_dialog.selectedFiles()[0]
            # Load the selected image and display it in the label
            pixmap = QPixmap(filename)
            palette = self.palette()
            palette.setBrush(QPalette.Window, QBrush(pixmap))
            self.setPalette(palette)


# THIS DOESNT WORK RIGHT YET!!
    # Opens file explorer so that the user can select a docx file
    def open_docx_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Document", "", "Word Documents (*.docx)")
        if filename:
                doc = docx.Document(filename)
                full_text = ""
                for para in doc.paragraphs:
                    full_text+=(para.text)
                self.text_edit.setHtml(full_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditorBase()
    editor.show()
    sys.exit(app.exec_())
