"""
С помощью Pyqt создайте калькулятор с графическим интерфейсом.
Приложение должно выполнять: Сложение, вычитание, деление, умножение, возведение в степень, запоминание значения,
вывод значения из памяти.
"""
from PyQt6.QtWidgets import QApplication, QWidget

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("fork")



if __name__ == "__main__":
    app = QApplication([])
    calc = Calculator()
    calc.show()
    app.exec()