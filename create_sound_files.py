from pydub import AudioSegment
from gtts import gTTS
import tempfile
from pydub.playback import play 

drowsy_list = [
"Our system has detected signs of drowsiness. It's important to take a break and rest before continuing your journey for your own safety.",
"We've noticed indications of fatigue. Please take a moment to rest before continuing your journey for your well-being.",
"Alert: You appear to be feeling drowsy. We recommend taking a break and resting before continuing your journey for your own safety.",
"Your driving seems to indicate fatigue. Please consider taking a break and getting some rest before continuing your journey for your safety.",
"Attention: Signs of drowsiness have been detected. For your safety, we suggest taking a break and resting before resuming your journey."
]
sleep_list = [
"It seems like your eyes may be closed. For your safety and the safety of others; please pull over to a safe location immediately and take a break from driving.",
"To ensure your safety and the safety of those around you, please immediately pull over to a secure location and take a break from driving if it appears that your eyes are closed.",
"If it seems like your eyes are closed, please stop driving and take a break in a secure area to ensure your safety and the safety of others.",
"In order to guarantee your own safety and that of other individuals on the road, if you think your eyes are closed, please pull over to a secure location right away and take a break from driving.",
"To avoid any risks and keep yourself and others safe, please pull over to a safe spot immediately and take a break from driving if it seems like your eyes may be closed."
]

for i in range(len(drowsy_list)):
    text = drowsy_list[i]
    tts = gTTS(text, lang = 'en')

    tts.save("drowsy{}.mp3".format(i))

    
