from PySide6.QtWidgets import QApplication,QTextEdit, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import Qt
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
from s2s import SpeechWorker
from translator import translate_
import subprocess
from time import sleep
import sys,os

app = QApplication(sys.argv)

window = QWidget()
window.resize(800, 600)
window.setWindowTitle("My First PySide6 App")

def start_listening():
    textarea.append("Listening...")

    worker = SpeechWorker()
    window.worker = worker  # keep a reference so it doesn't get garbage collected

    worker.result_ready.connect(on_speech_result)
    worker.error.connect(on_speech_error)
    worker.start()

def on_speech_result(text):
    textarea.append("Recognized & translated:")
    textarea.append(text)

    audio_file = os.path.abspath("output_speech.mp3")

    for _ in range(20): #waits for the file to reloads
        if os.path.exists(audio_file) and os.path.getsize(audio_file)>0:
            break
        sleep()

    player.stop()
    player.setSource(QUrl())  # clear cache
    player.setSource(QUrl.fromLocalFile(audio_file))  # reload new audio
    # player.play()  # optional: auto-play


def on_speech_error(msg):
    textarea.append(f"Error: {msg}")

# def on_button_click():
#     Text = textbox.text()
#     Text=translate_(Text)
#     print(type(Text))
#     print("Text is:", Text)
#     textarea.append(Text)
#     textbox.clear()

layout = QVBoxLayout()
input_layout = QHBoxLayout()

button = QPushButton("translate")
# button.setMinimumSize(150, 40)
# button.clicked.connect(on_button_click)
button.clicked.connect(start_listening)
input_layout.addWidget(button)

audio_output = QAudioOutput()
player = QMediaPlayer()
player.setAudioOutput(audio_output)

player.setSource(QUrl())   # clear cache
player.setSource(QUrl.fromLocalFile("output_speech.mp3"))
audio_output.setVolume(0.5)

Button = QPushButton("Play")
Button.clicked.connect(player.play)
input_layout.addWidget(Button)

textarea = QTextEdit()
textarea.setReadOnly(True)  # or True if you want it read-only
layout.addWidget(textarea, alignment=Qt.AlignCenter)

# Align items inside the horizontal layout

input_layout.setAlignment(Qt.AlignCenter)

layout.addLayout(input_layout)
layout.setAlignment(Qt.AlignCenter)
layout.setContentsMargins(20, 20, 20, 20)
layout.setSpacing(15)

window.setLayout(layout)
window.show()

sys.exit(app.exec())