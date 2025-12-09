from gtts import gTTS
import os
import platform
import subprocess

def text_to_audio_file(text, filename="output_speech.mp3", language='en'):
    """
    Converts text to speech using Google TTS and saves it as an MP3 file.
    """
    print(f"Generating audio for text: '{text[:50]}...'")
    try:
        # Create a gTTS object (slow=False makes speech speed normal)
        tts = gTTS(text=text, lang=language, slow=False)
        
        # Save the audio file
        tts.save(filename)
        print(f"Audio saved successfully to {filename}")
        return filename
    except Exception as e:
        print(f"An error occurred during gTTS generation: {e}")
        return None

def play_audio_file(filename):
    """
    Plays the generated MP3 file using the default system player.
    """
    if filename:
        system_platform = platform.system()
        try:
            if system_platform == "Windows":
                os.startfile(filename)
            elif system_platform == "Darwin": # macOS
                subprocess.run(["afplay", filename])
            elif system_platform == "Linux":
                # Requires 'mpg123' or 'omxplayer' or similar to be installed
                subprocess.run(["mpg123", filename]) 
            else:
                print("Cannot automatically play audio on this operating system.")
        except FileNotFoundError:
            print(f"Could not find a suitable player for {system_platform}. Please play '{filename}' manually.")
        except Exception as e:
            print(f"Error trying to play audio file: {e}")

# --- Main execution ---
if __name__ == "__main__":
    my_text = "The gTTS library is working perfectly. You have successfully created an MP3 file using Google's text-to-speech API."
    audio_file = text_to_audio_file(my_text)
    
    if audio_file:
        # Note: Automatic playback might not work on all systems without extra dependencies.
        # It's safest to locate the file in your directory and play it manually.
        # Uncomment the line below if you want to attempt automatic playback:
        # play_audio_file(audio_file)
        pass

