import os

from PySide6.QtWidgets import (QMainWindow, QWidget, QLabel, QVBoxLayout, 
                               QHBoxLayout, QFileDialog, QPushButton, QTextEdit,
                               QListWidget)
from PySide6.QtCore import QSize, QStringListModel, Qt
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

        # Input file selection
        self.input_layout = QHBoxLayout()
        self.input_file_lbl = QLabel('Select input .spc file')
        self.input_layout.addWidget(self.input_file_lbl)

        self.input_file_btn = QPushButton("open...") 
        self.input_file_btn.clicked.connect(self.input_file_btn_clicked)
        self.input_layout.addWidget(self.input_file_btn)

        # Input filename display
        self.input_FN_layout = QHBoxLayout()
        self.input_FN_lbl = QLabel('Path to .spc file:')
        self.input_FN_layout.addWidget(self.input_FN_lbl)
        self.input_path_textedit = QTextEdit()
        self.input_path_textedit.setReadOnly(True)
        self.input_path_textedit.setMaximumHeight(25)
        self.input_FN_layout.addWidget(self.input_path_textedit)
        
        # Input spectra selection
        self.spectra_lbl_metadata_layout = QHBoxLayout()
        self.spectra_selection_lbl = QLabel('Select spectra to export')
        self.spectra_lbl_metadata_layout.addWidget(self.spectra_selection_lbl)
        
        self.show_metadata_btn = QPushButton('show metadata ...')
        self.spectra_lbl_metadata_layout.addWidget(self.show_metadata_btn)
        
        self.spectra_selection_layout = QVBoxLayout()
        self.spectra_selection = QListWidget()
        self.spectra_selection_layout.addWidget(self.spectra_selection)

        self.output_lbl = QLabel('Choose output destination \nand export data')
        self.output_dest_btn = QPushButton('select folder ...')
        self.output_dest_btn.clicked.connect(self.output_dest_btn_clicked)
        self.export_btn = QPushButton('export spectra')

        self.output_layout = QHBoxLayout()
        self.output_layout.addWidget(self.output_lbl)
        self.output_btn_layout = QVBoxLayout()
        self.output_btn_layout.addWidget(self.output_dest_btn)
        self.output_btn_layout.addWidget(self.export_btn)
        self.output_layout.addLayout(self.output_btn_layout)

        self.central_widget_layout.addLayout(self.input_layout)
        self.central_widget_layout.addLayout(self.input_FN_layout)
        self.central_widget_layout.addLayout(self.spectra_lbl_metadata_layout)
        self.central_widget_layout.addLayout(self.spectra_selection_layout)
        self.central_widget_layout.addLayout(self.output_layout)

        self.central_widget.setLayout(self.central_widget_layout)
        self.setCentralWidget(self.central_widget)

        
        
        #lw = QListWidget()
        #for i in range(5):
        #    text = f'Item {i}'
        #    item = QListWidgetItem(text)
        #    item.setCheckState(Qt.Unchecked)
        #    lw.addItem(item)

    def input_file_btn_clicked(self):    
        dlg = QFileDialog(self)
        dlg.setWindowTitle("Select .spc file ...")
        #dlg.exec_()
        if dlg.exec():
            self.inputFileNames = dlg.selectedFiles()
            self.input_path_textedit.setText(self.inputFileNames[-1])
        print(self.inputFileNames)

    def output_dest_btn_clicked(self):
        dlg = QFileDialog(self)
        dlg.setWindowTitle("Select output folder destination ...")
        #dlg.exec_()
        folder = dlg.getExistingDirectory()
        print(folder)


if __name__ == '__main__':
    from main import main
    main()