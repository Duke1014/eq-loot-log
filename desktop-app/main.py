# import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QVBoxLayout, QLabel, QPushButton
# from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EQ Loot Log")
        layout = QVBoxLayout()


        # widget.setGeometry(50, 50, 1400, 1000)

        self.label = QLabel("<h1> This is important text stuff.</h1>")
        self.button = QPushButton("Click me!")
        self.button.clicked.connect(self.button_clicked)

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # self.master = QHBoxLayout()
        # column_1 = QVBoxLayout()
        # column_2 = QVBoxLayout()

        # column_1.setWidget(QLabel("column 1"))
        # column_2.setWidget(QLabel("column 2"))

        # self.layout.addLayout(column_1, 15)
        # self.layout.addLayout(column_2, 85)    
        
        # widget.setLayout(self.layout)
        # self.setFixedSize(QSize(1400,800))

        # self.setCentralWidget(widget)

        window = QWidget()
        window.setLayout(layout)

        self.setCentralWidget(window)

    def button_clicked(self):
        self.label.setText("Clicked!")
        self.button.setText("Button clicked!")


app = QApplication([])

window = MainWindow()
window.show()

app.exec()