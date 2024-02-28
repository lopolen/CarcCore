import sys
import math
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox

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
        self.n1 = None
        self.n2 = None
        self.math_operator = None

        # Constants
        self.SEP = ''
        self.ONLY_n1_OPERATOS = ['n!', '√x', '3√x', '^3', '^2', '1 / x', 'sin', 
                                 'cos', 'tg', 'ctg', 'arcsin', 'arccos', 'arctg', 'arcctg']

        # Filling comboboxes
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

        # Change module button
        self.ui.btn_change_mod.clicked.connect(self.handle_change_mod)

        # Calculation button
        self.ui.btn_plus.clicked.connect(lambda: self.handle_calculation_buttons('+'))
        self.ui.btn_subtract.clicked.connect(lambda: self.handle_calculation_buttons('-'))
        self.ui.btn_multiply.clicked.connect(lambda: self.handle_calculation_buttons('*'))
        self.ui.btn_divise.clicked.connect(lambda: self.handle_calculation_buttons('/'))
        self.ui.btn_factorial.clicked.connect(lambda: self.handle_calculation_buttons('n!'))
        self.ui.btn_convert.clicked.connect(lambda: self.handle_calculation_buttons('*10^y'))
        self.ui.btn_power_2.clicked.connect(lambda: self.handle_calculation_buttons('^2'))
        self.ui.btn_power_3.clicked.connect(lambda: self.handle_calculation_buttons('^3'))
        self.ui.btn_power_y.clicked.connect(lambda: self.handle_calculation_buttons('^y'))
        self.ui.btn_inverse.clicked.connect(lambda: self.handle_calculation_buttons('1 / x'))
        self.ui.btn_square_root.clicked.connect(lambda: self.handle_calculation_buttons('√x'))
        self.ui.btn_cube_root.clicked.connect(lambda: self.handle_calculation_buttons('3√x'))
        self.ui.btn_algebry_root.clicked.connect(lambda: self.handle_calculation_buttons('y√x'))
        
        self.ui.btn_sin.clicked.connect(lambda: self.handle_calculation_buttons('sin'))
        self.ui.btn_cos.clicked.connect(lambda: self.handle_calculation_buttons('cos'))
        self.ui.btn_tg.clicked.connect(lambda: self.handle_calculation_buttons('tg'))
        self.ui.btn_ctg.clicked.connect(lambda: self.handle_calculation_buttons('ctg'))
        self.ui.btn_arcsin.clicked.connect(lambda: self.handle_calculation_buttons('arcsin'))
        self.ui.btn_arccos.clicked.connect(lambda: self.handle_calculation_buttons('arccos'))
        self.ui.btn_arctg.clicked.connect(lambda: self.handle_calculation_buttons('arctg'))
        self.ui.btn_arcctg.clicked.connect(lambda: self.handle_calculation_buttons('arcctg'))

        self.ui.btn_result.clicked.connect(self.handle_equal_button)

        # Convert button
        self.ui.btn_convert_unit.clicked.connect(self.handle_convert_unit) 

        # Entry unit combobox update
        self.ui.cb_entry_unit.currentTextChanged.connect(self.on_cb_entry_update)

    def handle_equal_button(self):
        try:
            if self.n1 is None:
                self.n1 = float(self.ui.el_entry.text())
            elif self.n2 is None:
                self.n2 = float(self.ui.el_entry.text())

            result = None
            
            # Two variables operations
            if self.math_operator == '+':
                result = self.n1 + self.n2
            elif self.math_operator == '-':
                result = self.n1 - self.n2
            elif self.math_operator == '*':
                result = self.n1 * self.n2
            elif self.math_operator == '/':
                result = self.n1 / self.n2
            elif self.math_operator == '*10^y':
                result = self.n1 * 10 ** self.n2
            elif self.math_operator == 'y√x':
                if self.n2 % 2 == 0 and self.n1 < 0:
                    raise ValueError
                result = self.n1 ** (1 / self.n2)
            elif self.math_operator == '^y':
                result = self.n1 ** self.n2

                # One variable operation 
            elif self.math_operator == 'n!':
                result = math.factorial(int(self.n1))
            elif self.math_operator == '^2':
                result = self.n1 ** 2
            elif self.math_operator == '^3':
                result = self.n1 ** 3
            elif self.math_operator == '3√x':
                result = self.n1 ** (1 / 3)
            elif self.math_operator == '√x':
                result = math.sqrt(self.n1)
            elif self.math_operator == '1 / x':
                result = 1 / self.n1
            
            # Trigonometria 
            elif self.math_operator == 'sin':
                if self.ui.rb_degrees.isChecked():
                    result = math.degrees(math.sin(math.radians(self.n1)))
                else:
                    result = math.sin(self.n1)
            elif self.math_operator == 'cos':
                if self.ui.rb_degrees.isChecked():
                    result = math.degrees(math.cos(math.radians(self.n1)))
                result = math.cos(self.n1)
            elif self.math_operator == 'tg':
                if self.ui.rb_degrees.isChecked():
                    result = math.degrees(math.tan(math.radians(self.n1)))
                result = math.tan(self.n1)
            elif self.math_operator == 'ctg':
                if self.ui.rb_degrees.isChecked():
                    result = math.degrees(1 / math.tan(math.radians(self.n1)))
                result = 1 / math.tan(self.n1)
            elif self.math_operator == 'arcsin':
                if self.ui.rb_degrees.isChecked():
                    result = math.degrees(math.asin(math.radians(self.n1)))
                result = math.asin(self.n1)
            elif self.math_operator == 'arccos':
                if self.ui.rb_degrees.isChecked():
                    result = math.degrees(math.acos(math.radians(self.n1)))
                result = math.acos(self.n1)
            elif self.math_operator == 'arctg':
                if self.ui.rb_degrees.isChecked():
                    result = math.degrees(math.atan(math.radians(self.n1)))
                result = math.atan(self.n1)
            elif self.math_operator == 'arcctg':
                if self.ui.rb_degrees.isChecked():
                    result = math.degrees(math.pi / 2 - math.atan(math.radians(self.n1)))
                result = math.pi / 2 - math.atan(self.n1)
            
            # Equal double click
            elif self.math_operator == None:
                self.ui.lbl_temp.setText(f'{self.ui.el_entry.text()} = ')
                self.ui.el_entry.setText(str(self.ui.el_entry.text()))
                return
            
            if self.math_operator in self.ONLY_n1_OPERATOS:
                self.ui.lbl_temp.setText(f'{self.n1} {self.math_operator} = ')
                self.ui.el_entry.setText(str(result))

            else:
                self.ui.lbl_temp.setText(f'{self.n1} {self.math_operator} {self.n2} = ')
                self.ui.el_entry.setText(str(result))

            self.math_operator = None
        
        except ValueError:
            QMessageBox.warning(self, 'Lopolen calc. Warning. ValueError', 'You entered unvalid values!')
            self.clear_entry()
            self.clear_entry()
        except ZeroDivisionError:
            QMessageBox.warning(self, 'Lopolen Calc. Warning. ZeroDivisionError', 'You can\'t divise by zero!')
            self.clear_entry()
            self.clear_entry()

    def handle_calculation_buttons(self, math_operator):
        if self.n1 is None:
            # Saving
            self.n1 = float(self.ui.el_entry.text())
            self.math_operator = math_operator

            # Calling equal if needed only one parameter 
            if math_operator in self.ONLY_n1_OPERATOS:
               self.handle_equal_button()
               self.n1 = float(self.ui.el_entry.text())
               self.math_operator = None
               return

            # Updating UI
            self.ui.lbl_temp.setText(f'{self.n1} {self.math_operator} ')
            self.ui.el_entry.clear()

        else:
            if self.ui.el_entry.text() == '':
                self.math_operator = math_operator
                self.ui.lbl_temp.setText(f'{self.n1} {self.math_operator} ')
                return
            
            # Saving
            self.n2 = float(self.ui.el_entry.text())

            # Calling equal and saving as n1
            self.handle_equal_button()
            self.n1 = float(self.ui.el_entry.text())
            self.n2 = None
            self.math_operator = math_operator

            # Updating UI
            self.ui.lbl_temp.setText(f'{self.n1} {self.math_operator} ')
            self.ui.el_entry.clear()

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
    
    def handle_change_mod(self): 
        try:
            if self.ui.el_entry.text()[0] == '-':
                try:
                    self.ui.el_entry.setText(self.ui.el_entry.text()[1:])
                except IndexError:
                    self.ui.el_entry.setText('')
                finally:
                    return
        except IndexError:
            pass
        self.ui.el_entry.setText(f'-{self.ui.el_entry.text()}')

    def clear_entry(self):
        """Clearing entry editline or temp label
        """
        if self.ui.el_entry.text() != '0':
            self.ui.el_entry.setText('0')
        else: 
            self.ui.lbl_temp.clear()
            
            # Clearing variables 
            self.n1 = None
            self.n2 = None
            self.math_operator = ''

    def backspace_handle(self):
        if len(self.ui.el_entry.text()) > 1:
            self.ui.el_entry.setText(self.ui.el_entry.text()[:-1])
        else:
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

    def handle_convert_unit(self):
        if self.ui.cb_entry_unit.currentText() == self.SEP:
            return 
        
        num = float(self.ui.el_entry.text())
        entry_unit = self.ui.cb_entry_unit.currentText()
        wanted_unit = self.ui.cb_wanted_unit.currentText()

        res = CalcCore.convert(num, entry_unit, wanted_unit)
        
        self.ui.el_entry.setText(str(res[0]))
        
        self.ui.cb_entry_unit.setCurrentText(wanted_unit)
        self.ui.cb_wanted_unit.setCurrentText(entry_unit)

        self.ui.lbl_temp.setText(f'Convert {num} {entry_unit} to {wanted_unit} = ')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
