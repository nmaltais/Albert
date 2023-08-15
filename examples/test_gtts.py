from gtts import gTTS

tts = gTTS('hello world', lang='en', tld='com.au')
tts.save('audio/hello_world.mp3')