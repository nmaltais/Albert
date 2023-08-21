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
        <!-- brew install espeak -->
        python3 -m pip install --user virtualenv
        pip3 install python3-pyaudio

    Linux / RaspberryPi OS
        sudo apt-get install libttspico-utils
        sudo apt-get install python-pyaudio
        sudo apt-get install python3-venv -y
<!-- wget http://ftp.us.debian.org/debian/pool/non-free/s/svox/libttspico0_1.0+git20130326-9_armhf.deb
        wget http://ftp.us.debian.org/debian/pool/non-free/s/svox/libttspico-utils_1.0+git20130326-9_armhf.deb
        sudo apt-get install -f ./libttspico0_1.0+git20130326-9_armhf.deb ./libttspico-utils_1.0+git20130326-9_armhf.deb
        pico2wave -l en-US -w lookdave.wav "Hi, Welcome to Circuit Digest Tutorial" && aplay lookdave.wav -->
        sudo apt-get install festival
        sudo apt-get install festvox-us-slt-hts
        add this line to /etc/festival.scm: (set! voice_default 'voice_cmu_us_slt_arctic_hts) 



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