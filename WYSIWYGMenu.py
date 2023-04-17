import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTextEdit, QPushButton, QToolBar, QAction, QComboBox
from PyQt5.QtGui import * 
'''
  Simple WYSIWYG Menu that can be added to a PyQt project with a textbox 
'''
class WYSIWYGMenu(QToolBar):
    # constructor requires a QTextEdit parameter so that it knows what text to format and modify
    def __init__(self, text_edit: QTextEdit ):
        # Constants
        self.BOLD = 75
        self.DEFAULT =  50
        super().__init__() 
        self.text_edit = text_edit
        self.createMenu()

        # for now we will have the toolbar be white
        self.setStyleSheet("background-color : white;")
    '''
    createMenu : called by constructor.  Populates toolbar with components such as buttons for bold,italic, and underline and a QComboBox for selecting Fonts 
    '''
    def createMenu(self):
        # create bold button 
        bold_action = QAction('Bold', self)
        bold_action.setShortcut('Ctrl+B')
        bold_action.triggered.connect(self.bold)
        
        # create italic button
        italic_action = QAction('Italic', self)
        italic_action.setShortcut('Ctrl+I')
        italic_action.triggered.connect(self.italic)

        # create underline button
        underline_action = QAction('Underline', self)
        underline_action.setShortcut('Ctrl+U')
        underline_action.triggered.connect(self.underline)


        # create center-align button
        align_center_action = QAction('Align Center', self)
        align_center_action.triggered.connect(self.setCenter)

        # create left-align button
        align_left_action = QAction('Align Left', self)
        align_left_action.triggered.connect(self.setLeft)


        # create right-align button
        align_right_action = QAction('Align Right', self)
        align_right_action.triggered.connect(self.setRight)


        # add actions to toolbar
        self.addAction(bold_action)
        self.addAction(italic_action)
        self.addAction(underline_action)

        # create font selection widget
        fontComboBox = QComboBox(self)
        # add all supported fonts to the combobox
        fontComboBox.addItems(QFontDatabase().families()) 
        fontComboBox.activated[str].connect(self.setFont)
        fontComboBox.setCurrentIndex(2) # set default font 
        self.addWidget(fontComboBox)

        # create font size widget
        sizeComboBox = QComboBox(self)
        # add all supported font sizes to the combobox
        sizeComboBox.addItems([str(size) for size in range(8,73,2)]) 
        sizeComboBox.activated[str].connect(self.setSize)
        sizeComboBox.setCurrentIndex(2); # set default font size
        self.addWidget(sizeComboBox)

        self.addAction(align_right_action)
        self.addAction(align_center_action)
        self.addAction(align_left_action)



## FONT FORMATTING FUNCTIONS : 
# this needs work too

    def setCenter(self):
         self.text_edit.setAlignment(Qt.AlignCenter)

    def setLeft(self):
        self.text_edit.setAlignment(Qt.AlignLeft)

    def setRight(self):
        self.text_edit.setAlignment(Qt.AlignRight)


    def setSize(self, size):
        self.text_edit.setFontPointSize(int(size))    
        cursor = self.text_edit.textCursor()
        if not cursor.hasSelection():
            return
        format = cursor.charFormat()
        format.setFontPointSize(int(size));
        cursor.mergeCharFormat(format)

    def setFont(self, font):
        self.text_edit.setFontFamily(font)    
        cursor = self.text_edit.textCursor()
        if not cursor.hasSelection():
            return
        format = cursor.charFormat()
        format.setFontFamily(font);
        cursor.mergeCharFormat(format)

    def bold(self):
        # grab text cursor 
        cursor = self.text_edit.textCursor()
        if (not cursor.hasSelection()):
            return

        format = cursor.charFormat()
        if format.fontWeight() == self.DEFAULT:
            format.setFontWeight(self.BOLD)
        else:
            format.setFontWeight(self.DEFAULT)
        cursor.mergeCharFormat(format);
    
    def underline(self):
        # grab text cursor
        cursor = self.text_edit.textCursor()
        format = cursor.charFormat()
        format.setFontUnderline( not format.fontUnderline()) 
        if (not cursor.hasSelection()):
            return
        cursor.mergeCharFormat(format);

    def italic(self):
        # grab text cursor 
        cursor = self.text_edit.textCursor()
        if (not cursor.hasSelection()):
            return
        format = cursor.charFormat()
        format.setFontItalic( not format.fontItalic()) 
        cursor.mergeCharFormat(format);



