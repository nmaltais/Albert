import os
import sys
import wave
import pyaudio

def play_audio(audio_file):
    chunk = 1024

    try:
        wf = wave.open(audio_file, 'rb')
        p = pyaudio.PyAudio()

        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )

        data = wf.readframes(chunk)

        while data:
            stream.write(data)
            data = wf.readframes(chunk)

        stream.stop_stream()
        stream.close()

        p.terminate()

    except Exception as e:
        print(f"Error playing audio: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python playwav.py <audio_file>")
        sys.exit(1)

    audio_file = sys.argv[1]
    if not os.path.exists(audio_file):
        print("Audio file not found.")
        sys.exit(1)

    play_audio(audio_file)