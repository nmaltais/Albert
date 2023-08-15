import sys
from src import Audio
from src import TTS

def readText(text):
    mp3_file = TTS.textToMp3(text)
    Audio.playAudio(mp3_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python readtext.py <Text to repeat>")
        sys.exit(1)

    text = sys.argv[1]

    readText(text)