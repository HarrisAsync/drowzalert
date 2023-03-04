from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import tempfile
from random import randint


class Sound_Alerts:
    def __init__(self):
        self.drowsy_list = [
        "Our system has detected signs of drowsiness. It's important to take a break and rest before continuing your journey for your own safety.",
        "We've noticed indications of fatigue. Please take a moment to rest before continuing your journey for your well-being.",
        "Alert: You appear to be feeling drowsy. We recommend taking a break and resting before continuing your journey for your own safety.",
        "Your driving seems to indicate fatigue. Please consider taking a break and getting some rest before continuing your journey for your safety.",
        "Attention: Signs of drowsiness have been detected. For your safety, we suggest taking a break and resting before resuming your journey."
        ]
        self.sleep_list = [
        "It seems like your eyes may be closed. For your safety and the safety of others, please pull over to a safe location immediately and take a break from driving.",
        "To ensure your safety and the safety of those around you, please immediately pull over to a secure location and take a break from driving if it appears that your eyes are closed.",
        "If it seems like your eyes are closed, please stop driving and take a break in a secure area to ensure your safety and the safety of others.",
        "In order to guarantee your own safety and that of other individuals on the road, if you think your eyes are closed, please pull over to a secure location right away and take a break from driving.",
        "To avoid any risks and keep yourself and others safe, please pull over to a safe spot immediately and take a break from driving if it seems like your eyes may be closed."
        ]
        self.chime1 = AudioSegment.from_wav("dundun_short.wav")
        self.chime2 = AudioSegment.from_wav("Alarm_short.wav")
        self.chime3 = AudioSegment.from_wav("AUGHHHH.wav")

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
        
        index = randint(0, 4)

        
        if input == 1:
            play(self.chime1)
            self.create_sound(self.drowsy_list[index])
        elif input == 2:
            play(self.chime2)
            self.create_sound(self.sleep_list[index])
        elif input == 3:
            play(self.chime3)
            self.create_sound("zzz")


    
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

