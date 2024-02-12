from PySide6.QtWidgets import QMainWindow, QDialog
from ui_Qt_interface import Ui_MainWindow
from PySide6.QtGui import QPixmap
from ui_about import Ui_Form
from PySide6 import QtGui
from new_rc import *
import webbrowser
import math

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Set window name
        self.setWindowTitle("Converter")
        self.setWindowIcon(QtGui.QIcon(":/newPrefix/icon.png"))
        # Load and set the image within the QLabel
        pixmap = QPixmap(":/newPrefix/trap.png")
        self.label_3.setPixmap(pixmap)
        self.label_3.setScaledContents(True)  # Ensure the image fits the label size
        self.label_3.setFixedSize(200, 123)  # Set a fixed size for the label

        # Tab 1 inputs
        self.flow_rate_input.textChanged.connect(self.update_output_tab1)
        self.density_input.textChanged.connect(self.update_output_tab1)
        # Tab 2 inputs
        self.side_length_input.textChanged.connect(self.update_output_tab2)
        self.base_a_input.textChanged.connect(self.update_output_tab2)
        self.base_b_input.textChanged.connect(self.update_output_tab2)
        # Menu bar action
        self.actionAbout.triggered.connect(self.open_about_widget)
        self.actionDocumentation.triggered.connect(self.open_documentation)

    def update_output_tab1(self):
        try:
            one_input_value = float(self.flow_rate_input.text())
            two_input_value = float(self.density_input.text())
            # Converts from L/min to kg/s
            result = (two_input_value/60000)*one_input_value
            result = "{0:.8f}".format(result)
            self.flow_rate_output.setText(f"{result}")
        except ValueError:
            self.flow_rate_output.setText("Error. Enter numbers")

    def update_output_tab2(self):
        try:
            side_length = float(self.side_length_input.text())
            base_a = float(self.base_a_input.text())
            base_b = float(self.base_b_input.text())
            # Find height of trapezoid
            base = (base_b-base_a)/2
            altitude = math.sqrt(side_length ** 2 - base ** 2)
            self.height_output.setText(f"{altitude}")
        except ValueError:
            self.height_output.setText("Error. Enter numbers")

    def open_about_widget(self):
        # Create an instance of the AboutDialog class
        about_dialog = AboutDialog()
        # Show the About widget
        about_dialog.exec_()

    def open_documentation(self):
        url = "https://github.com/curious-grapes/converter-tool/wiki"
        webbrowser.open_new_tab(url)

class AboutDialog(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(":/newPrefix/icon.png"))
        # Load and set the image within the QLabel
        pixmap = QPixmap(":/newPrefix/icon_t.png")  # Update the path accordingly
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)  # Ensure the image fits the label size
        self.setFixedSize(390, 240)  # Adjust dimensions as needed
