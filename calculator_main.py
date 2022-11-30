import sys
from PyQt5.QtWidgets import *
import math
import numpy as np
class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        layout_clear_equal = QGridLayout()
        layout_equation_solution = QFormLayout()
        lable_eqsol=QLabel("")
        self.eqsol = QLineEdit("")
        layout_equation_solution.addRow(lable_eqsol, self.eqsol)


        button_division = QPushButton("/")
        button_product = QPushButton("x")
        button_minus = QPushButton("-")
        button_plus = QPushButton("+")
        
        stack=[0,0,0]
    
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation,stack))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation,stack))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation,stack))
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation,stack))
        
        
        

        button_root = QPushButton("x**2")
        button_sqr = QPushButton("x^2")
        button_reverse = QPushButton("1/x")
        button_remain = QPushButton("%")
        button_equal = QPushButton("=")
        button_clear = QPushButton("C")
        button_backspace = QPushButton("CE")



        button_root.clicked.connect(self.button_root_clicked)
        button_sqr.clicked.connect(self.button_sqr_clicked)
        button_reverse.clicked.connect(self.button_reverse_clicked)
        button_remain.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation,stack))
        button_equal.clicked.connect(lambda state, operation = "=": self.button_equal_clicked(stack))
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_clear_clicked)

        layout_clear_equal.addWidget(button_root,1,2)
        layout_clear_equal.addWidget(button_sqr,1,1)
        layout_clear_equal.addWidget(button_reverse,1,0)
        layout_clear_equal.addWidget(button_remain,0,0)
        layout_clear_equal.addWidget(button_clear,0,2)
        layout_clear_equal.addWidget(button_backspace,0,1)
        layout_clear_equal.addWidget(button_equal,5,3)
        layout_clear_equal.addWidget(button_product,2,3)
        layout_clear_equal.addWidget(button_division,1,3)
        layout_clear_equal.addWidget(button_minus,3,3)
        layout_clear_equal.addWidget(button_plus,4,3)

        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num,stack))
    
                
            if number==0:
                layout_clear_equal.addWidget(number_button_dict[number], 5, 1)

                
        layout_clear_equal.addWidget(number_button_dict[7], 2, 0)
        layout_clear_equal.addWidget(number_button_dict[8], 2, 1)
        layout_clear_equal.addWidget(number_button_dict[9], 2, 2)
        layout_clear_equal.addWidget(number_button_dict[4], 3, 0)
        layout_clear_equal.addWidget(number_button_dict[5], 3, 1)
        layout_clear_equal.addWidget(number_button_dict[6], 3, 2)
        layout_clear_equal.addWidget(number_button_dict[1], 4, 0)
        layout_clear_equal.addWidget(number_button_dict[2], 4, 1)
        layout_clear_equal.addWidget(number_button_dict[3], 4, 2)
        
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num,stack))
        layout_clear_equal.addWidget(button_dot, 5, 2)

        

        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_clear_equal)

        self.setLayout(main_layout)
        self.show()

    def number_button_clicked(self, num,stack):
        eqsol = self.eqsol.text()
        eqsol += str(num)
        stack.append(eqsol)
        self.eqsol.setText(eqsol)

        
    def button_operation_clicked(self, operation,stack):
        eqsol = self.eqsol.text()
        eqsol += operation
        stack.append(operation)
        self.eqsol.setText("")
    def button_equal_clicked(self,stack):
        eqsol = self.eqsol.text()
        list = [0,0,0]
        list[0]=stack.pop()
        list[1]=stack.pop()
        list[2]=stack.pop()
        if list[1] == '+':
            eqsol= int(list[2])+int(list[0])
        elif list[1] == '-':
            eqsol= int(list[2])-int(list[0])
        elif list[1] == '*':
            eqsol= int(list[2])*int(list[0])
        elif list[1] == '/':
            eqsol= int(list[2])/int(list[0])
        elif list[1] == '%':
            eqsol= int(list[2])%int(list[0])
        self.eqsol.setText(str(eqsol))

    def button_clear_clicked(self):
        self.eqsol.setText("")

    def button_reverse_clicked(self):
        eqsol = self.eqsol.text()
        eqsol = np.reciprocal(float(eqsol))
        self.eqsol.setText(str(eqsol))

    def button_sqr_clicked(self):
        eqsol = self.eqsol.text()
        eqsol = math.pow(float(eqsol), 2)
        self.eqsol.setText(str(eqsol))

    def button_root_clicked(self):
        eqsol = self.eqsol.text()
        eqsol = math.sqrt(float(eqsol))
        self.eqsol.setText(str(eqsol))
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
