# import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QVBoxLayout, QLabel, QPushButton, QTabWidget
from PyQt6.QtGui import QColor
# from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EQ Loot Log")
        self.setFixedSize(QSize(1400,800))

        # main layout
        self.main_layout                = QHBoxLayout()
        self.fight_navigation_layout    = QVBoxLayout()
        self.data_layout                = QVBoxLayout()

        # spacing for main layout
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(10)

        # fight nav (left side of app)
        self.fight_navigation_label     = QLabel("<h1>Fight Nav</h1>")
        self.fight_navigation_layout.addWidget(self.fight_navigation_label)

        file_name = "Load a log file here."
        self.log_file_add_button        = QPushButton(file_name)
        self.fight_navigation_layout.addWidget(self.log_file_add_button)

        # add to main
        self.main_layout.addLayout(self.fight_navigation_layout, 15)

        # data (right side of app)
        self.data_label = QLabel("<h1>Data goes here</h1>")
        self.data_layout.addWidget(self.data_label)

        # add to main
        self.main_layout.addLayout(self.data_layout, 85)


        # self.label = QLabel("<h1> This is important text stuff.</h1>")
        # self.button = QPushButton("Click me!")
        # self.button.clicked.connect(self.button_clicked)

        # layout.addWidget(self.label)
        # layout.addWidget(self.button)
        # color = QColor(255, 0 , 0)
        # self.button.setStyleSheet(f"background-color: {color.name()};")

        # self.master = QHBoxLayout()
        # column_1 = QVBoxLayout()
        # column_2 = QVBoxLayout()

        # column_1.setWidget(QLabel("column 1"))
        # column_2.setWidget(QLabel("column 2"))

        # layout.addWidget(column_1, 15)
        # layout.addWidget(column_2, 85)    
        


        # self.setCentralWidget(widget)

        self.window = QWidget()
        self.window.setLayout(self.main_layout)

        self.setCentralWidget(self.window)

    def button_clicked(self):
        self.label.setText("Clicked!")
        self.button.setText("Button clicked!")


app = QApplication([])

window = MainWindow()
window.show()

app.exec()