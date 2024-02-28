# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_temp = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        self.lbl_temp.setText("")
        self.lbl_temp.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbl_temp.setObjectName("lbl_temp")
        self.verticalLayout.addWidget(self.lbl_temp)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rb_degrees = QtWidgets.QRadioButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_degrees.sizePolicy().hasHeightForWidth())
        self.rb_degrees.setSizePolicy(sizePolicy)
        self.rb_degrees.setChecked(True)
        self.rb_degrees.setObjectName("rb_degrees")
        self.horizontalLayout.addWidget(self.rb_degrees)
        self.rb_radians = QtWidgets.QRadioButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_radians.sizePolicy().hasHeightForWidth())
        self.rb_radians.setSizePolicy(sizePolicy)
        self.rb_radians.setChecked(False)
        self.rb_radians.setObjectName("rb_radians")
        self.horizontalLayout.addWidget(self.rb_radians)
        self.cb_entry_unit = QtWidgets.QComboBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_entry_unit.sizePolicy().hasHeightForWidth())
        self.cb_entry_unit.setSizePolicy(sizePolicy)
        self.cb_entry_unit.setObjectName("cb_entry_unit")
        self.horizontalLayout.addWidget(self.cb_entry_unit)
        self.cb_wanted_unit = QtWidgets.QComboBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_wanted_unit.sizePolicy().hasHeightForWidth())
        self.cb_wanted_unit.setSizePolicy(sizePolicy)
        self.cb_wanted_unit.setObjectName("cb_wanted_unit")
        self.horizontalLayout.addWidget(self.cb_wanted_unit)
        self.btn_convert_unit = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_convert_unit.sizePolicy().hasHeightForWidth())
        self.btn_convert_unit.setSizePolicy(sizePolicy)
        self.btn_convert_unit.setObjectName("btn_convert_unit")
        self.horizontalLayout.addWidget(self.btn_convert_unit)
        self.el_entry = QtWidgets.QLineEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.el_entry.sizePolicy().hasHeightForWidth())
        self.el_entry.setSizePolicy(sizePolicy)
        self.el_entry.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.el_entry.setReadOnly(True)
        self.el_entry.setObjectName("el_entry")
        self.horizontalLayout.addWidget(self.el_entry)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttons_grid = QtWidgets.QGridLayout()
        self.buttons_grid.setObjectName("buttons_grid")
        self.btn_n4 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_n4.sizePolicy().hasHeightForWidth())
        self.btn_n4.setSizePolicy(sizePolicy)
        self.btn_n4.setObjectName("btn_n4")
        self.buttons_grid.addWidget(self.btn_n4, 2, 2, 1, 1)
        self.btn_power_y = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_power_y.sizePolicy().hasHeightForWidth())
        self.btn_power_y.setSizePolicy(sizePolicy)
        self.btn_power_y.setObjectName("btn_power_y")
        self.buttons_grid.addWidget(self.btn_power_y, 3, 1, 1, 1)
        self.btn_divise = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_divise.sizePolicy().hasHeightForWidth())
        self.btn_divise.setSizePolicy(sizePolicy)
        self.btn_divise.setObjectName("btn_divise")
        self.buttons_grid.addWidget(self.btn_divise, 3, 5, 1, 1)
        self.btn_n8 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_n8.sizePolicy().hasHeightForWidth())
        self.btn_n8.setSizePolicy(sizePolicy)
        self.btn_n8.setObjectName("btn_n8")
        self.buttons_grid.addWidget(self.btn_n8, 1, 3, 1, 1)
        self.btn_backspace = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy)
        self.btn_backspace.setObjectName("btn_backspace")
        self.buttons_grid.addWidget(self.btn_backspace, 0, 4, 1, 1)
        self.btn_cube_root = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cube_root.sizePolicy().hasHeightForWidth())
        self.btn_cube_root.setSizePolicy(sizePolicy)
        self.btn_cube_root.setObjectName("btn_cube_root")
        self.buttons_grid.addWidget(self.btn_cube_root, 2, 0, 1, 1)
        self.btn_power_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_power_2.sizePolicy().hasHeightForWidth())
        self.btn_power_2.setSizePolicy(sizePolicy)
        self.btn_power_2.setObjectName("btn_power_2")
        self.buttons_grid.addWidget(self.btn_power_2, 1, 1, 1, 1)
        self.btn_arccos = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_arccos.sizePolicy().hasHeightForWidth())
        self.btn_arccos.setSizePolicy(sizePolicy)
        self.btn_arccos.setObjectName("btn_arccos")
        self.buttons_grid.addWidget(self.btn_arccos, 5, 3, 1, 1)
        self.btn_ctg = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ctg.sizePolicy().hasHeightForWidth())
        self.btn_ctg.setSizePolicy(sizePolicy)
        self.btn_ctg.setObjectName("btn_ctg")
        self.buttons_grid.addWidget(self.btn_ctg, 5, 1, 1, 1)
        self.btn_arcctg = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_arcctg.sizePolicy().hasHeightForWidth())
        self.btn_arcctg.setSizePolicy(sizePolicy)
        self.btn_arcctg.setObjectName("btn_arcctg")
        self.buttons_grid.addWidget(self.btn_arcctg, 5, 5, 1, 1)
        self.btn_n6 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_n6.sizePolicy().hasHeightForWidth())
        self.btn_n6.setSizePolicy(sizePolicy)
        self.btn_n6.setObjectName("btn_n6")
        self.buttons_grid.addWidget(self.btn_n6, 2, 4, 1, 1)
        self.btn_change_mod = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_change_mod.sizePolicy().hasHeightForWidth())
        self.btn_change_mod.setSizePolicy(sizePolicy)
        self.btn_change_mod.setObjectName("btn_change_mod")
        self.buttons_grid.addWidget(self.btn_change_mod, 4, 2, 1, 1)
        self.btn_n0 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_n0.sizePolicy().hasHeightForWidth())
        self.btn_n0.setSizePolicy(sizePolicy)
        self.btn_n0.setObjectName("btn_n0")
        self.buttons_grid.addWidget(self.btn_n0, 4, 3, 1, 1)
        self.btn_n2 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_n2.sizePolicy().hasHeightForWidth())
        self.btn_n2.setSizePolicy(sizePolicy)
        self.btn_n2.setObjectName("btn_n2")
        self.buttons_grid.addWidget(self.btn_n2, 3, 3, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setObjectName("btn_clear")
        self.buttons_grid.addWidget(self.btn_clear, 0, 3, 1, 1)
        self.btn_power_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_power_3.sizePolicy().hasHeightForWidth())
        self.btn_power_3.setSizePolicy(sizePolicy)
        self.btn_power_3.setObjectName("btn_power_3")
        self.buttons_grid.addWidget(self.btn_power_3, 2, 1, 1, 1)
        self.btn_result = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_result.sizePolicy().hasHeightForWidth())
        self.btn_result.setSizePolicy(sizePolicy)
        self.btn_result.setObjectName("btn_result")
        self.buttons_grid.addWidget(self.btn_result, 4, 5, 1, 1)
        self.btn_multiply = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_multiply.sizePolicy().hasHeightForWidth())
        self.btn_multiply.setSizePolicy(sizePolicy)
        self.btn_multiply.setObjectName("btn_multiply")
        self.buttons_grid.addWidget(self.btn_multiply, 2, 5, 1, 1)
        self.btn_n3 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_n3.sizePolicy().hasHeightForWidth())
        self.btn_n3.setSizePolicy(sizePolicy)
        self.btn_n3.setObjectName("btn_n3")
        self.buttons_grid.addWidget(self.btn_n3, 3, 4, 1, 1)
        self.btn_inverse = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_inverse.sizePolicy().hasHeightForWidth())
        self.btn_inverse.setSizePolicy(sizePolicy)
        self.btn_inverse.setObjectName("btn_inverse")
        self.buttons_grid.addWidget(self.btn_inverse, 0, 0, 1, 1)
        self.btn_arctg = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_arctg.sizePolicy().hasHeightForWidth())
        self.btn_arctg.setSizePolicy(sizePolicy)
        self.btn_arctg.setObjectName("btn_arctg")
        self.buttons_grid.addWidget(self.btn_arctg, 5, 4, 1, 1)
        self.btn_n1 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_n1.sizePolicy().hasHeightForWidth())
        self.btn_n1.setSizePolicy(sizePolicy)
        self.btn_n1.setObjectName("btn_n1")
        self.buttons_grid.addWidget(self.btn_n1, 3, 2, 1, 1)
        self.btn_algebry_root = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_algebry_root.sizePolicy().hasHeightForWidth())
        self.btn_algebry_root.setSizePolicy(sizePolicy)
        self.btn_algebry_root.setObjectName("btn_algebry_root")
        self.buttons_grid.addWidget(self.btn_algebry_root, 3, 0, 1, 1)
        self.btn_cos = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cos.sizePolicy().hasHeightForWidth())
        self.btn_cos.setSizePolicy(sizePolicy)
        self.btn_cos.setObjectName("btn_cos")
        self.buttons_grid.addWidget(self.btn_cos, 4, 1, 1, 1)
        self.btn_factorial = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_factorial.sizePolicy().hasHeightForWidth())
        self.btn_factorial.setSizePolicy(sizePolicy)
        self.btn_factorial.setObjectName("btn_factorial")
        self.buttons_grid.addWidget(self.btn_factorial, 0, 2, 1, 1)
        self.btn_n7 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_n7.sizePolicy().hasHeightForWidth())
        self.btn_n7.setSizePolicy(sizePolicy)
        self.btn_n7.setObjectName("btn_n7")
        self.buttons_grid.addWidget(self.btn_n7, 1, 2, 1, 1)
        self.btn_subtract = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_subtract.sizePolicy().hasHeightForWidth())
        self.btn_subtract.setSizePolicy(sizePolicy)
        self.btn_subtract.setObjectName("btn_subtract")
        self.buttons_grid.addWidget(self.btn_subtract, 1, 5, 1, 1)
        self.btn_point = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy)
        self.btn_point.setObjectName("btn_point")
        self.buttons_grid.addWidget(self.btn_point, 4, 4, 1, 1)
        self.btn_n5 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_n5.sizePolicy().hasHeightForWidth())
        self.btn_n5.setSizePolicy(sizePolicy)
        self.btn_n5.setObjectName("btn_n5")
        self.buttons_grid.addWidget(self.btn_n5, 2, 3, 1, 1)
        self.btn_square_root = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_square_root.sizePolicy().hasHeightForWidth())
        self.btn_square_root.setSizePolicy(sizePolicy)
        self.btn_square_root.setObjectName("btn_square_root")
        self.buttons_grid.addWidget(self.btn_square_root, 1, 0, 1, 1)
        self.btn_convert = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_convert.sizePolicy().hasHeightForWidth())
        self.btn_convert.setSizePolicy(sizePolicy)
        self.btn_convert.setObjectName("btn_convert")
        self.buttons_grid.addWidget(self.btn_convert, 0, 1, 1, 1)
        self.btn_sin = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sin.sizePolicy().hasHeightForWidth())
        self.btn_sin.setSizePolicy(sizePolicy)
        self.btn_sin.setObjectName("btn_sin")
        self.buttons_grid.addWidget(self.btn_sin, 4, 0, 1, 1)
        self.btn_n9 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_n9.sizePolicy().hasHeightForWidth())
        self.btn_n9.setSizePolicy(sizePolicy)
        self.btn_n9.setObjectName("btn_n9")
        self.buttons_grid.addWidget(self.btn_n9, 1, 4, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        self.btn_plus.setObjectName("btn_plus")
        self.buttons_grid.addWidget(self.btn_plus, 0, 5, 1, 1)
        self.btn_tg = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_tg.sizePolicy().hasHeightForWidth())
        self.btn_tg.setSizePolicy(sizePolicy)
        self.btn_tg.setObjectName("btn_tg")
        self.buttons_grid.addWidget(self.btn_tg, 5, 0, 1, 1)
        self.btn_arcsin = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_arcsin.sizePolicy().hasHeightForWidth())
        self.btn_arcsin.setSizePolicy(sizePolicy)
        self.btn_arcsin.setObjectName("btn_arcsin")
        self.buttons_grid.addWidget(self.btn_arcsin, 5, 2, 1, 1)
        self.verticalLayout.addLayout(self.buttons_grid)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lopolen Calc"))
        self.rb_degrees.setText(_translate("MainWindow", "Degrees"))
        self.rb_radians.setText(_translate("MainWindow", "Radians"))
        self.cb_entry_unit.setPlaceholderText(_translate("MainWindow", "Entry unit"))
        self.cb_wanted_unit.setPlaceholderText(_translate("MainWindow", "Wanted unit"))
        self.btn_convert_unit.setText(_translate("MainWindow", "Convert!"))
        self.el_entry.setText(_translate("MainWindow", "0"))
        self.btn_n4.setText(_translate("MainWindow", "4"))
        self.btn_n4.setShortcut(_translate("MainWindow", "4"))
        self.btn_power_y.setText(_translate("MainWindow", "^y"))
        self.btn_divise.setText(_translate("MainWindow", "/"))
        self.btn_divise.setShortcut(_translate("MainWindow", "/"))
        self.btn_n8.setText(_translate("MainWindow", "8"))
        self.btn_n8.setShortcut(_translate("MainWindow", "8"))
        self.btn_backspace.setText(_translate("MainWindow", "<-"))
        self.btn_backspace.setShortcut(_translate("MainWindow", "Backspace"))
        self.btn_cube_root.setText(_translate("MainWindow", "3√x"))
        self.btn_power_2.setText(_translate("MainWindow", "^2"))
        self.btn_arccos.setText(_translate("MainWindow", "arccos"))
        self.btn_ctg.setText(_translate("MainWindow", "ctg"))
        self.btn_arcctg.setText(_translate("MainWindow", "arcctg"))
        self.btn_n6.setText(_translate("MainWindow", "6"))
        self.btn_n6.setShortcut(_translate("MainWindow", "6"))
        self.btn_change_mod.setText(_translate("MainWindow", "+/-"))
        self.btn_n0.setText(_translate("MainWindow", "0"))
        self.btn_n0.setShortcut(_translate("MainWindow", "0"))
        self.btn_n2.setText(_translate("MainWindow", "2"))
        self.btn_n2.setShortcut(_translate("MainWindow", "2"))
        self.btn_clear.setText(_translate("MainWindow", "C"))
        self.btn_clear.setShortcut(_translate("MainWindow", "Esc"))
        self.btn_power_3.setText(_translate("MainWindow", "^3"))
        self.btn_result.setText(_translate("MainWindow", "="))
        self.btn_result.setShortcut(_translate("MainWindow", "Enter"))
        self.btn_multiply.setText(_translate("MainWindow", "*"))
        self.btn_multiply.setShortcut(_translate("MainWindow", "*"))
        self.btn_n3.setText(_translate("MainWindow", "3"))
        self.btn_n3.setShortcut(_translate("MainWindow", "3"))
        self.btn_inverse.setText(_translate("MainWindow", "1 / x"))
        self.btn_arctg.setText(_translate("MainWindow", "arctg"))
        self.btn_n1.setText(_translate("MainWindow", "1"))
        self.btn_n1.setShortcut(_translate("MainWindow", "1"))
        self.btn_algebry_root.setText(_translate("MainWindow", "y√x"))
        self.btn_cos.setText(_translate("MainWindow", "cos"))
        self.btn_factorial.setText(_translate("MainWindow", "n!"))
        self.btn_n7.setText(_translate("MainWindow", "7"))
        self.btn_n7.setShortcut(_translate("MainWindow", "7"))
        self.btn_subtract.setText(_translate("MainWindow", "-"))
        self.btn_subtract.setShortcut(_translate("MainWindow", "-"))
        self.btn_point.setText(_translate("MainWindow", "."))
        self.btn_point.setShortcut(_translate("MainWindow", ","))
        self.btn_n5.setText(_translate("MainWindow", "5"))
        self.btn_n5.setShortcut(_translate("MainWindow", "5"))
        self.btn_square_root.setText(_translate("MainWindow", "√x"))
        self.btn_convert.setText(_translate("MainWindow", "*10^y"))
        self.btn_sin.setText(_translate("MainWindow", "sin"))
        self.btn_n9.setText(_translate("MainWindow", "9"))
        self.btn_n9.setShortcut(_translate("MainWindow", "9"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_plus.setShortcut(_translate("MainWindow", "+"))
        self.btn_tg.setText(_translate("MainWindow", "tg"))
        self.btn_arcsin.setText(_translate("MainWindow", "arcsin"))
