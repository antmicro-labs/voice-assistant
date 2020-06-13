from gtts import gTTS
import os

def textReader(text):
    myobj = gTTS(text=text, lang='pl', slow=False)
    myobj.save('response.mp3')
    os.system('mpg123 response.mp3')