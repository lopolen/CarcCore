import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

from MainWindowDesign import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_n0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.btn_n1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.btn_n2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.btn_n3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.btn_n4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.btn_n5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.btn_n6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.btn_n7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.btn_n8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.btn_n9.clicked.connect(lambda: self.add_digit('9'))
        
        self.ui.btn_point.clicked.connect(self.add_point)

        self.ui.btn_clear.clicked.connect(self.clear_entry)


    def add_digit(self, text: str): 
        if self.ui.el_entry.text() == '0':
            self.ui.el_entry.setText(text)
        else:
            self.ui.el_entry.setText(self.ui.el_entry.text() + text)


    def add_point(self):
        if not '.' in self.ui.el_entry.text():
            self.ui.el_entry.setText(self.ui.el_entry.text() + '.')

    
    def clear_entry(self):
        if self.ui.el_entry.text() == '0':
            self.ui.el_entry.setText('0')
        else: 
            self.ui.lbl_temp.clear()

    def add_temp(self, math_sign):
        if not self.ui.lbl_temp.text():
            self.ui.lbl_temp.setText(self.ui.el_entry.text() + f' {math_sign}')
            self.ui.el_entry.setText('0')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
