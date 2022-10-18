#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import (
    QFileDialog,
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QHBoxLayout,
    QPushButton,
)

"""
Напишите программу, состоящую из однострочного и многострочного
текстовых полей и двух кнопок "Открыть" и "Сохранить". При клике
на первую должен открываться на чтение файл, чье имя указано в поле
класса Entry, а содержимое файла должно загружаться в поле типа Text.
При клике на вторую кнопку текст, введенный пользователем в экземпляр
Text, должен сохраняться в файле под именем, которое пользователь
указал в однострочном текстовом поле.
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # Вызываем конструктор базового класса QWidget
        self.setWindowTitle("Открытие и сохранение файла")
        self.setGeometry(500, 500, 600, 400)
        self.text_edit = QTextEdit()
        self.initialize_ui()

    def initialize_ui(self):
        vbox = QVBoxLayout()
        grid = QHBoxLayout()
        vbox.addLayout(grid)
        button1 = QPushButton("Открыть")
        button1.clicked.connect(self.opening)
        button2 = QPushButton("Сохранить")
        button2.clicked.connect(self.saving)
        grid.addWidget(button1)
        grid.addWidget(button2)
        vbox.addWidget(self.text_edit)
        self.setLayout(vbox)

    def opening(self):
        self.text_edit.clear()
        name = QFileDialog.getOpenFileName()
        with open(name[0], "r", encoding="utf-8") as f:
            data = f.read()
        self.text_edit.setText(str(data))
        self.setWindowTitle(name[0])

    def saving(self):
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save File As", "", "Text Files (*.txt)"
        )
        if filename:
            text = self.text_edit.toPlainText()
            with open(filename, "w", encoding="utf-8") as f:
                f.write(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
