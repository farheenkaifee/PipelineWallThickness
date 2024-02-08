from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.valueslist = [10, 20, 30]  # Example list attribute

        # Assigning the first value of self.valueslist to a variable
        self.Measured_Minimum_Thickness_for_Test_Pressure_t1 = self.valueslist[0]

        # Example button to demonstrate variable assignment
        self.button = QPushButton('Print Value', self)
        self.button.clicked.connect(self.print_value)
        self.button.move(50, 50)

    def print_value(self):
        print(self.Measured_Minimum_Thickness_for_Test_Pressure_t1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
