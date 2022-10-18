#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import (
    QWidget,
    QApplication,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QLineEdit,
)
from PySide2.QtCore import Qt

"""
Перепишите программу из предыдущего задания
так, чтобы интерфейс выглядел по-другому.
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # Вызываем конструктор базового класса QWidget
        self.setWindowTitle("Цвета радуги №2")
        self.setGeometry(200, 200, 300, 100)
        self.line_edit = QLineEdit(self)
        self.label = QLabel(self)
        self.button1 = QPushButton()
        self.button2 = QPushButton()
        self.button3 = QPushButton()
        self.button4 = QPushButton()
        self.button5 = QPushButton()
        self.button6 = QPushButton()
        self.button7 = QPushButton()
        self.initialize_ui()

    def initialize_ui(self):
        self.label.resize(80, 10)
        self.label.setAlignment(Qt.AlignHCenter)

        self.line_edit.resize(60, 20)
        self.line_edit.setAlignment(Qt.AlignHCenter)

        self.button1.setStyleSheet("background-color: #ff0000;")
        self.button1.clicked.connect(self.red)

        self.button2.setStyleSheet("background-color: #ff7d00;")
        self.button2.clicked.connect(self.orange)

        self.button3.setStyleSheet("background-color: #ffff00;")
        self.button3.clicked.connect(self.yellow)

        self.button4.setStyleSheet("background-color: #00ff00;")
        self.button4.clicked.connect(self.green)

        self.button5.setStyleSheet("background-color: #007dff;")
        self.button5.clicked.connect(self.blue)

        self.button6.setStyleSheet("background-color: #0000ff;")
        self.button6.clicked.connect(self.darkblue)

        self.button7.setStyleSheet("background-color: #7d00ff;")
        self.button7.clicked.connect(self.purple)

    def widgets(self):
        vbox = QVBoxLayout()
        layout = QHBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.line_edit)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.button6)
        layout.addWidget(self.button7)
        vbox.addLayout(layout)
        self.setLayout(vbox)

    def red(self):
        self.label.setText("Красный")
        self.line_edit.setText("#ff0000")

    def orange(self):
        self.label.setText("Оранжевый")
        self.line_edit.setText("#ff7d00")

    def yellow(self):
        self.label.setText("Желтый")
        self.line_edit.setText("#ffff00")

    def green(self):
        self.label.setText("Зеленый")
        self.line_edit.setText("#00ff00")

    def blue(self):
        self.label.setText("Голубой")
        self.line_edit.setText("#007dff")

    def darkblue(self):
        self.label.setText("Синий")
        self.line_edit.setText("#0000ff")

    def purple(self):
        self.label.setText("Фиолетовый")
        self.line_edit.setText("#7d00ff")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.widgets()
    window.show()
    sys.exit(app.exec_())
