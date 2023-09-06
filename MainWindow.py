from UI_MainWindow import UI_MainWindow

class MainWindow(UI_MainWindow):
    def __init__(self):
        super().__init__()

        # ====================================================================
        # How to add checkable items to QListWidget
        # ===================================================================
        # lw = self.spectra_selection
        # for i in range(5):
        #     text = f'Item {i}'
        #     item = QListWidgetItem(text)
        #     item.setCheckState(Qt.Unchecked)
        #     lw.addItem(item)

if __name__ == '__main__':
    from main import main
    main()