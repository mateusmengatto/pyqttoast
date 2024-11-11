from qtpy.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QToolButton
from qtpy.QtCore import Signal, Qt, QPoint
import sys

class CloseMiniMenu(QWidget):
    # Define signals for each button action
    variable_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.setWindowModality(Qt.NonModal)

        # Create buttons for each action
        self.close_button = QPushButton("Relembrar")
        self.remind_me_button = QPushButton("Abrir")
        self.keep_on_button = QPushButton("Concluir")
        #'novo', 'aberto', 'espera', 'concluido'
        # Connect each button to its respective signal
        self.close_button.clicked.connect(lambda: self.emit_variable("novo"))
        self.remind_me_button.clicked.connect(lambda: self.emit_variable("aberto"))
        self.keep_on_button.clicked.connect(lambda: self.emit_variable("concluido"))

        # Close the menu after any button is clicked
        self.close_button.clicked.connect(self.close)
        self.remind_me_button.clicked.connect(self.close)
        self.keep_on_button.clicked.connect(self.close)

        # Layout to arrange buttons vertically
        layout = QVBoxLayout()
        layout.addWidget(self.close_button)
        layout.addWidget(self.remind_me_button)
        layout.addWidget(self.keep_on_button)
        self.setLayout(layout)

    def emit_variable(self, variable):
        self.variable_signal.emit(variable)
        self.close()


    def show_menu(self, pos: QPoint):
        # Display the menu at the specified screen position
        self.move(pos)
        self.show()