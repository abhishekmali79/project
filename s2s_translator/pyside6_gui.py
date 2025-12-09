from PySide6.QtWidgets import QApplication,QTextEdit, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import Qt
from translator import translate_
import sys

app = QApplication(sys.argv)

def on_button_click():
    Text = textbox.text()
    Text=translate_(Text)
    print(type(Text))
    print("Text is:", Text)
    textarea.append(Text)
    textbox.clear()

window = QWidget()
window.resize(800, 600)
window.setWindowTitle("My First PySide6 App")

layout = QVBoxLayout()
input_layout = QHBoxLayout()

textbox = QLineEdit()
textbox.setFixedWidth(200)
textbox.setPlaceholderText("enter text here")

button = QPushButton("translate")
button.setMinimumSize(150, 40)
button.clicked.connect(on_button_click)

textarea = QTextEdit()
textarea.setReadOnly(True)  # or True if you want it read-only

# Align items inside the horizontal layout
input_layout.setAlignment(Qt.AlignCenter)
input_layout.addWidget(textbox)

layout.addLayout(input_layout)
layout.addWidget(button, alignment=Qt.AlignCenter)
layout.addWidget(textarea, alignment=Qt.AlignCenter)
layout.setContentsMargins(20, 20, 20, 20)
layout.setSpacing(15)

window.setLayout(layout)
window.show()

sys.exit(app.exec())
