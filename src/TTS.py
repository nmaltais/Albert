import os
import platform

def playText(text):
    if platform.system() == 'Darwin': # MacOs
        os.system("say -v Grandpa '" + text + "'")
    elif platform.system() == 'Linux': # RaspberryPi
        os.system("echo " + text + " | festival --tts")