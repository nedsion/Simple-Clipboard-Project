import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from main_ui import Ui_MainWindow
import pyperclip


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.label_2.setOpenExternalLinks(True)
        self.uic.label_2.setText("<a href=\"https://www.facebook.com/nedsion/\">Support</a>")
    
    def show(self):
        self.main_win.show()
        self.uic.pushButton.clicked.connect(self.open_file)
        self.uic.pushButton_2.clicked.connect(self.get_line)
        

    def open_file(self):
        fname = QFileDialog.getOpenFileName()
        path = fname[0]
        self.path2 = path
        self.count_clicked = -1
        if fname:
            self.uic.lineEdit.setText(str(path))

    def get_line(self):
        with open(self.path2, 'r') as f:
            num_lines = sum(1 for line in open(self.path2))
            lines = f.readlines()
            self.count_clicked += 1 
            data = lines[self.count_clicked].split()
            for element in data:
                stringdata = ""
                stringdata = element
            pyperclip.copy(stringdata)


if __name__=="__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())