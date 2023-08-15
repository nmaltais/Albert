from gtts import gTTS

def textToMp3(text):
    tts = gTTS(text, lang='en', tld='com.au')
    path = "audio/readtext.mp3"
    tts.save(path)
    return path