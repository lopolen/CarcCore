import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

from MainWindowDesign import Ui_MainWindow
import CalcCore
import units


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        # UI initialize
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Reserving variables
        self.n1 = 0
        self.n2 = 0
        self.math_action_symbol = ''

        # Filling comboboxes
        self.SEP = ''
        self.ui.cb_entry_unit.addItems(units.get_all_units(sep=self.SEP))
        self.on_cb_entry_update()

        ### SIGNALS
        # Digit numbers
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
        
        # Point button
        self.ui.btn_point.clicked.connect(self.add_point)

        # Clear button
        self.ui.btn_clear.clicked.connect(self.clear_entry)

        # Backspace button
        self.ui.btn_backspace.clicked.connect(self.backspace_handle)

        # Calculation button
        self.ui.btn_plus.clicked.connect(lambda: self.math_action('+'))
        self.ui.btn_subtract.clicked.connect(lambda: self.math_action('-'))
        self.ui.btn_multiply.clicked.connect(lambda: self.math_action('*'))
        self.ui.btn_divise.clicked.connect(lambda: self.math_action('/'))
        
        self.ui.btn_result.clicked.connect(lambda: self.math_action('='))

        # Entry unit combobox update
        self.ui.cb_entry_unit.currentTextChanged.connect(self.on_cb_entry_update)


    def add_digit(self, text: str): 
        """Adds digits to the entry editline

        Args:
            text (str): Digit string
        """
        if self.ui.el_entry.text() == '0':
            self.ui.el_entry.setText(text)
        else:
            self.ui.el_entry.setText(self.ui.el_entry.text() + text)


    def add_point(self):
        """Adding point to the entry editline
        """
        if not '.' in self.ui.el_entry.text():
            self.ui.el_entry.setText(self.ui.el_entry.text() + '.')

    
    def clear_entry(self):
        """Clearing entry editline or temp label
        """
        if self.ui.el_entry.text() != '0':
            self.ui.el_entry.setText('0')
        else: 
            self.ui.lbl_temp.clear()
            
            # Clearing variables 
            self.n1 = 0
            self.n2 = 0
            self.math_action_symbol = ''

    def backspace_handle(self):
        if len(self.ui.el_entry.text()) > 1:
            self.ui.el_entry.setText(self.ui.el_entry.text()[:-1])
        else:
            self.ui.el_entry.setText('0')

    @staticmethod
    def remove_floating_zeros(num: str) -> str:
        """Removing useles floating zeros from number

        Args:
            num (str): Number

        Returns:
            str: Number
        """
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

    @staticmethod
    def calculate(n1: float, n2: float, math_sign: str) -> float:
        if math_sign == '+':
            return n1 + n2 
        elif math_sign == '-':
            return n1 - n2
        elif math_sign == '*':
            return n1 * n2
        elif math_sign == '/':
            return n1 / n2

    def math_action(self, math_sign: str):
        """Adding a math sign to the entry editline

        Args:
            math_sign (str): Math sign symbol
        """
        if not self.ui.lbl_temp.text():
            # Saving first number and action
            self.n1 = float(self.ui.el_entry.text())
            self.math_action_symbol = math_sign

            # Updating UI
            self.ui.lbl_temp.setText(self.remove_floating_zeros(self.ui.el_entry.text()) + f' {math_sign} ')
            if math_sign != '=':
                self.ui.el_entry.setText('0')
            else:
                self.ui.el_entry.setText(self.remove_floating_zeros(str(self.n1)))

        else:
            if '=' in self.ui.lbl_temp.text():
                self.ui.lbl_temp.clear()
                return self.math_action(math_sign)

            # Calculating previous task
            self.n2 = float(self.ui.el_entry.text())
            self.n1 = self.calculate(self.n1, self.n2, self.math_action_symbol)

            if math_sign == '=':
                self.ui.lbl_temp.setText(self.ui.lbl_temp.text() + f'{self.remove_floating_zeros(str(self.n2))} = ')
                self.ui.el_entry.setText(self.remove_floating_zeros(str(self.n1)))
            else:
                self.ui.lbl_temp.setText(self.remove_floating_zeros(str(self.n1)) + f' {math_sign} ')
                self.ui.el_entry.setText('0')

    def on_cb_entry_update(self):
        """Synth the wanted unit combobox values with entry ones
        """
        self.ui.cb_wanted_unit.clear()

        cb_text = self.ui.cb_entry_unit.currentText()
        if cb_text != self.SEP:
            if cb_text in units.length_c_units.keys():
                self.ui.cb_wanted_unit.addItems(units.length_c_units.keys())
            elif cb_text in units.weight_c_units.keys():
                self.ui.cb_wanted_unit.addItems(units.weight_c_units.keys())
            elif cb_text in units.time_c_units.keys():
                self.ui.cb_wanted_unit.addItems(units.time_c_units.keys())
            elif cb_text in units.amperage_c_units.keys():
                self.ui.cb_wanted_unit.addItems(units.amperage_c_units.keys())
            elif cb_text in ('celsius', 'fahrenheit', 'kelvin'):
                self.ui.cb_wanted_unit.addItems(('celsius', 'fahrenheit', 'kelvin'))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
