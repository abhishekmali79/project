from deep_translator import GoogleTranslator
from generate_audio_gtts import text_to_audio_file

def translate_(text):
    try:
        translated=GoogleTranslator(source='auto', target='hi').translate(text)
        text_to_audio_file(translated)
        
        return translated
    except Exception as e:
        return f"Translation Error: {e}"
