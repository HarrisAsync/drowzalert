from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import tempfile

class Sound_Alerts:
    """
    has one function: input
    input 1 for a TTS sound for drowsiness
    input 2 for a TTS sound for falling asleep
    """
    def input(self, input: int):
    # takes an input:
    # 1: User seems drowsy
    # 2: user has fallen asleep
    # 3: 
        if input == 1:
            self.create_sound("Drowsiness detected. Please consider taking a break and rest before continuing your journey.")
        elif input == 2:
            self.create_sound("You may be falling asleep. It's time to take a break and rest before continuing your journey. Please pull over to a safe location and take a break.")
        elif input == 3:
            pass
    
    def create_sound(self, text):
        """
        this plays the sound
        """
        tts = gTTS(text, lang = 'en')

        # Save the speech to a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as f:
            tts.save(f.name)
            speech_file = f.name

        # Load the speech from the temporary file using pydub
        speech = AudioSegment.from_file(speech_file, format='mp3')

        # Play the speech using pydub
        play(speech)



jack = Sound_Alerts()

jack.input(1)

