from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from random import randint


class Sound_Alerts:
    """
    has one function: input
    input 1 for a TTS sound for drowsiness
    input 2 for a TTS sound for falling asleep
    """
    def __init__(self):
        self.chime1 = AudioSegment.from_wav("dundun_short.wav")
        self.chime2 = AudioSegment.from_wav("Alarm_short.wav")
        self.chime3 = AudioSegment.from_wav("AUGHHHH.wav")
        self.drowsy = []
        self.sleepy = []



        for i in range(5):
            self.drowsy.append(AudioSegment.from_mp3("drowsy{}.wav".format(i)))
            self.sleepy.append(AudioSegment.from_mp3("sleep{}.wav".format(i)))
        print(self.drowsy)
        print(self.sleepy)

    def input(self, input: int):
    # takes an input:
    # 1: User seems drowsy
    # 2: user has fallen asleep
    # 3:  
        
        index = randint(0, 4)

        if input == 1:
            play(self.chime1)
            play(self.drowsy[index])
        elif input == 2:
            play(self.chime2)
            play(self.sleepy[index])
        elif input == 3:
            play(self.chime3)
            self.create_sound("zzz")

