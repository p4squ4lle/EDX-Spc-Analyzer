import os
from PySide6.QtWidgets import (QMainWindow, QWidget, QLabel, QVBoxLayout, 
                               QHBoxLayout, QFileDialog, QPushButton)
from PySide6.QtCore import QSize, QStringListModel
from PySide6.QtGui import QIcon

# =============================================================================
# CONSTANTS
# =============================================================================
BASEDIR = os.path.dirname(__file__)

MAIN_WINDOW_TITLE = 'EDX SPC Analyzer'
MAIN_WINDOW_MIN_SIZE = QSize(400,300)

class UI_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inputFileNames = QStringListModel()

        self.setWindowTitle(MAIN_WINDOW_TITLE)
        self.setMinimumSize(MAIN_WINDOW_MIN_SIZE)
        #self.setWindowIcon(QIcon(os.path.join(BASEDIR, 'resources/icons/')))
        self.central_widget = QWidget()
        self.central_widget_layout = QVBoxLayout()

        self.input_layout = QHBoxLayout()

        self.input_file_lbl = QLabel('Select input .spc file')
        self.input_layout.addWidget(self.input_file_lbl)
        
        self.input_file_btn = QPushButton("open...") 
        self.input_file_btn.clicked.connect(self.input_file_btn_clicked)
        self.input_layout.addWidget(self.input_file_btn)

        self.central_widget_layout.addLayout(self.input_layout)
        self.central_widget.setLayout(self.central_widget_layout)
        self.setCentralWidget(self.central_widget)

        #self.input_file_dlg = QFileDialog(self)
        #self.central_widget_layout.addWidget(self.input_file_dlg)

    def input_file_btn_clicked(self):    
        dlg = QFileDialog(self)
        dlg.setWindowTitle("Select .spc file ...")
        #dlg.exec_()
        if dlg.exec():
            self.inputFileNames = dlg.selectedFiles()
        print(self.inputFileNames)
        

if __name__ == '__main__':
    from main import main
    main()