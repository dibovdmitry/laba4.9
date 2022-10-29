#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import (
    QWidget,
    QApplication,
    QPushButton,
    QButtonGroup,
    QGridLayout,
    QLabel,
)
from PySide2.QtCore import Qt

"""
Напишите программу, в которой имеется несколько объединенных
в группу радиокнопок, индикатор которых выключен (indicatoron=0).
Если какая-нибудь кнопка включается, то в метке должна отображаться
соответствующая ей информация. Обычных кнопок в окне быть не должно.
"""

people = {
    "Гена": "+7 8005553535",
    "Кирилл": "+7 9620000000",
    "Юргита": "+7 9285555555",
}


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # Вызываем конструктор базового класса QWidget
        self.setWindowTitle("Радиокнопки")
        self.setGeometry(200, 200, 400, 130)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.button1 = QPushButton("Гена")
        self.button1.setCheckable(True)
        self.button2 = QPushButton("Кирилл")
        self.button2.setCheckable(True)
        self.button3 = QPushButton("Юргита")
        self.button3.setCheckable(True)
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.button1)
        self.button_group.addButton(self.button2)
        self.button_group.addButton(self.button3)
        self.button_group.buttonClicked.connect(self.button_clicked)
        self.grid_layout()

    def grid_layout(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.button1, 1, 0)
        grid.addWidget(self.button2, 2, 0)
        grid.addWidget(self.button3, 3, 0)
        grid.addWidget(self.label, 2, 2)
        self.setLayout(grid)

    def button_clicked(self, button):
        self.label.setText(people[button.text()])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
