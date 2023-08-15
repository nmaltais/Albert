import pyaudio
from pydub import AudioSegment


def playAudio(mp3_file):
    try:
        # Initialize PyAudio
        p = pyaudio.PyAudio()

        # Load the MP3 file using pydub
        audio = AudioSegment.from_file(mp3_file)

        # Get the audio file's properties
        channels = audio.channels
        sample_width = audio.sample_width
        frame_rate = audio.frame_rate

        # Open the PyAudio stream
        stream = p.open(format=p.get_format_from_width(sample_width),
                        channels=channels,
                        rate=frame_rate,
                        output=True)

        # Play the audio using PyAudio
        stream.write(audio.raw_data)

        # Close the PyAudio stream
        stream.stop_stream()
        stream.close()

        # Terminate PyAudio
        p.terminate()

    except Exception as e:
        print(f"Error playing audio: {e}")