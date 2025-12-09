from googletrans import Translator
from generate_audio_gtts import text_to_audio_file

# Initialize the translator
translator = Translator()

def translate_(text):

    # Perform the translation: auto-detect source language, translate to French
    # Use ISO 639-1 codes (e.g., 'fr' for French, 'es' for Spanish, 'hi' for Hindi)
    result = translator.translate(text, dest='en')

    # print(f"Original Text (Detected as {result.src}): {result.origin}")
    # print(f"Translated Text ({result.dest}): {result.text}")

    # Translate to another language, e.g., Hindi ('hi')
    result_hindi = translator.translate(text, dest='hi')
    print(f"Translated Text ({result_hindi.dest}): {result_hindi.text}")

    print("DEBUG type before sending:", type(result_hindi.text))
    text_to_audio_file(result_hindi.text)
    return result_hindi.text

