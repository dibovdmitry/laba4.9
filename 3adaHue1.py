#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import (
    QWidget,
    QApplication,
    QLabel,
    QPushButton,
    QLineEdit,
)
from PySide2.QtCore import Qt

"""
Напишите простейший калькулятор, состоящий из двух
текстовых полей, куда пользователь вводит числа, и
четырех кнопок "+", "-", "*", "/". Результат вычисления
должен отображаться в метке. Если арифметическое действие
выполнить невозможно(например, если были введены буквы, а
не числа), то в метке должно появляться слово "ошибка".
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # Вызываем конструктор базового класса QWidget
        self.setGeometry(200, 200, 300, 250)
        self.setWindowTitle("Калькулятор")
        self.line_edit1 = QLineEdit(self)
        self.line_edit2 = QLineEdit(self)
        self.label = QLabel(self)
        self.button1 = QPushButton("+", self)
        self.button2 = QPushButton("-", self)
        self.button3 = QPushButton("*", self)
        self.button4 = QPushButton("/", self)
        self.initialize_ui()

    def initialize_ui(self):
        self.line_edit1.move(123, 25)
        self.line_edit1.resize(60, 20)
        self.line_edit1.setAlignment(Qt.AlignHCenter)

        self.line_edit2.move(123, 50)
        self.line_edit2.resize(60, 20)
        self.line_edit2.setAlignment(Qt.AlignHCenter)

        self.button1.move(105, 80)
        self.button1.clicked.connect(self.addition)

        self.button2.move(105, 110)
        self.button2.clicked.connect(self.subtraction)

        self.button3.move(105, 140)
        self.button3.clicked.connect(self.multiplication)

        self.button4.move(105, 170)
        self.button4.clicked.connect(self.division)

        self.label.move(78, 210)
        self.label.resize(150, 20)
        self.label.setAlignment(Qt.AlignHCenter)

    def addition(self):
        try:
            a = self.line_edit1.text()
            b = self.line_edit2.text()
            result = str(float(a) + float(b))
            self.label.setText(result)
        except ValueError:
            self.label.setText("Ошибка")

    def subtraction(self):
        try:
            a = self.line_edit1.text()
            b = self.line_edit2.text()
            result = str(float(a) - float(b))
            self.label.setText(result)
        except ValueError:
            self.label.setText("Ошибка")

    def multiplication(self):
        try:
            a = self.line_edit1.text()
            b = self.line_edit2.text()
            result = str(float(a) * float(b))
            self.label.setText(result)
        except ValueError:
            self.label.setText("Ошибка")

    def division(self):
        try:
            a = self.line_edit1.text()
            b = self.line_edit2.text()
            result = str(float(a) / float(b))
            self.label.setText(result)
        except ValueError:
            self.label.setText("Ошибка")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
