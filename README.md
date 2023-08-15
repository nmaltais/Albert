# Albert
Virtual Assistant


Installation

1- connect to wifi

2- enable ssh

3- speaker-test -c2

4- sudo apt-get install python-pyaudio

5- sudo apt-get install python3-venv -y

6- create venv and install reqs
    python -m venv albertvenv
    source albertvenv/bin/activate (on Unix-like systems)
    venv_name\Scripts\activate (on Windows)
    pip install -r requirements.txt

7- run the program
   python src/main.py audio/yes.py