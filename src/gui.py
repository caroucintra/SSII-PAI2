from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Transmisión Punto-Punto")
        layout = QVBoxLayout()

        origin = QLineEdit()
        self.origin_input = ""
        origin.textEdited.connect(self.origin_edited)

        destination = QLineEdit()
        self.destination_input = ""
        destination.textEdited.connect(self.destination_edited)

        quantity = QLineEdit()
        self.quantity_input = ""
        quantity.textEdited.connect(self.quantity_edited)

        run = QPushButton("RUN")
        run.clicked.connect(self.run)

        widgets = [
            QLabel("Cuenta Origen"),
            origin,
            QLabel("Cuenta Destino"),
            destination,
            QLabel("Cantidad"),
            quantity,
            run,
        ]

        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def origin_edited(self, s):
        self.origin_input = s

    def destination_edited(self, s):
        self.destination_input = s

    def quantity_edited(self, s):
        self.quantity_input = s

    def run(self):
        print(self.origin_input, self.destination_input, self.quantity_input)
        start()


def start():
    print("starts app")

def startGUI():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec_()

startGUI()