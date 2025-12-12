from PySide6.QtCore import QThread, Signal
import speech_recognition as sr
from translator import translate_

class SpeechWorker(QThread):
    result_ready = Signal(str)
    error = Signal(str)

    def __init__(self):
        super().__init__()
        print("[DEBUG] Worker initialized")

    def run(self):
        print("[DEBUG] Worker thread started")

        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                print("[DEBUG] Adjusting for noise")
                r.adjust_for_ambient_noise(source, duration=0.2)

                print("[DEBUG] Listening...")
                audio = r.listen(source)   # <— If mic works, this returns audio

            print("[DEBUG] Recognizing...")
            text = r.recognize_google(audio)

            print("[DEBUG] Translating:", text)
            translated = translate_(text)

            self.result_ready.emit(translated)

        except Exception as e:
            print("[DEBUG] ERROR in thread:", e)
            self.error.emit(str(e))
