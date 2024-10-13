import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QColorDialog, QHBoxLayout
from PyQt5.QtCore import Qt

class CustomCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the main layout
        vbox = QVBoxLayout()

        # Display field for the calculator
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        vbox.addWidget(self.display)

        # Create grid layout for buttons
        self.grid = QGridLayout()
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]
        positions = [(i, j) for i in range(4) for j in range(4)]

        # Create and add buttons to the grid
        self.buttons = []
        for position, name in zip(positions, buttons):
            button = QPushButton(name)
            button.clicked.connect(self.on_button_clicked)
            self.grid.addWidget(button, *position)
            self.buttons.append(button)

        vbox.addLayout(self.grid)

        # Add customization section for colors
        hbox = QHBoxLayout()
        self.bg_color_button = QPushButton('Set Background Color')
        self.bg_color_button.clicked.connect(self.set_background_color)

        self.btn_color_button = QPushButton('Set Button Color')
        self.btn_color_button.clicked.connect(self.set_button_color)

        hbox.addWidget(self.bg_color_button)
        hbox.addWidget(self.btn_color_button)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        # Set default styles and window properties
        self.setStyleSheet("background-color: #1e1e1e;")
        self.setWindowTitle('Customizable Calculator')
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)  # Stay on top
        self.setGeometry(100, 100, 300, 400)

    def set_background_color(self):
        # Open color picker and set the background color
        color = QColorDialog.getColor()
        if color.isValid():
            self.setStyleSheet(f"background-color: {color.name()};")

    def set_button_color(self):
        # Open color picker and apply the color to all buttons
        color = QColorDialog.getColor()
        if color.isValid():
            for button in self.buttons:
                button.setStyleSheet(f"""
                    QPushButton {{
                        background-color: {color.name()};
                        color: #ffffff;
                        font-size: 18px;
                        border: 1px solid #555555;
                        padding: 15px;
                    }}
                """)

    def on_button_clicked(self):
        button = self.sender()
        if button.text() == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + button.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = CustomCalculator()
    calc.show()
    sys.exit(app.exec_())

