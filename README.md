# Albert
Virtual Assistant


Installation

1- connect to wifi

2- enable ssh

3- speaker-test -c2

4- installs
    Mac
        brew install portaudio
        brew install ffmpeg
        python3 -m pip install --user virtualenv
        pip3 install python3-pyaudio

    Linux / RaspberryPi OS
        sudo apt-get install python-pyaudio
        sudo apt-get install python3-venv -y


5- create venv and install reqs
    python -m venv albertvenv
    source albertvenv/bin/activate (on Unix-like systems)
    venv_name\Scripts\activate (on Windows)
    pip install -r requirements.txt

6- run programs
   python -m examples.playwav audio/yes.wav
   python -m examples.test_gtts
   python -m examples.test_pydub audio/hello_world.mp3
   python -m examples.readtext "Hello there, how are you?"