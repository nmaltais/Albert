from os import path
import speech_recognition as sr
import re

# with m as source:
#     print("Adjusting to ambient sound...")
#     r.adjust_for_ambient_noise(source, 2)
# with sr.Microphone() as source:
#     print("Listening...")
#     audio = r.listen(source, 10, 3)

# write audio to a WAV file
# with open("microphone-results.wav", "wb") as f:
#     f.write(audio.get_wav_data())

# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "../microphone-results.wav")
# # use the audio file as the audio source
# r = sr.Recognizer()
# with sr.AudioFile(AUDIO_FILE) as source:
#     audio = r.record(source)  # read the entire audio file

# Listen for phrases that are frequent "ghost words", meaning they are heard when there was actually silence.
# Must be lowercased
FREQUENT_FALSE_POSITIVES_PER_TOOL = {
    "sphinx": [],
    "whisper": ["thank you.", "you"],
}


def capture_mic_audio():
    with m as source:
        audio = r.listen(source, 10, 3)
        return audio


def audio_to_text(audio, tool="sphinx"):
    if audio == None:
        return None
    try:
        if tool == "sphinx":
            text = r.recognize_sphinx(audio, language="en-US")
        if tool == "whisper":
            text = r.recognize_whisper(audio, language="english")
            # text = r.recognize_whisper(audio, language="english", initial_prompt=['Albert'])

        print("OG text:" + text)
        if text.strip().lower() in FREQUENT_FALSE_POSITIVES_PER_TOOL[tool] or text == "":
            return None
        return text.strip()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error: {0}".format(e))
    except Exception:
        print("Error: {0}".format(e))


def get_voice_input(tool, keyword=False):
    audio = None
    # if keyword:
    #     with m as source:
    #         # audio = r.listen(source, None, 3, Snowboy)
    #         return audio
    # else:
    with m as source:
        audio = r.listen(source, 10, 3)
        # return audio
    return audio_to_text(audio, tool)


def listen_for_keyword(keyword):
    with m as source:
        audio = r.listen(source, None, 2)
        sentence = audio_to_text(audio, tool="whipser")
        match = re.search(keyword.lower(), sentence.lower())
        if match:
            return True
    return False


def adjust_for_ambient_sound():
    with m as source:
        print("Adjusting to ambient sound...")
        r.adjust_for_ambient_noise(source, 2)
    r.energy_threshold += 1000


def test_different_offline_tools():
    m = sr.Microphone.list_working_microphones()
    print(m)
    audio = capture_mic_audio()
    try:
        print(
            "Sphinx thinks you said: '"
            + r.recognize_sphinx(audio, language="en-US")
            + "'"
        )
        print(
            "Whisper thinks you said: '"
            + r.recognize_whisper(audio, language="english")
            + "'"
        )
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error: {0}".format(e))
    except sr.WaitTimeoutError as e:
        print("Error: {0}".format(e))


def output_listening_stats():
    print("energy_threshold: " + str(r.energy_threshold))
    print("dynamic_energy_threshold: " + str(r.dynamic_energy_threshold))
    print(
        "dynamic_energy_adjustment_damping: " + str(r.dynamic_energy_adjustment_damping)
    )
    print("pause_threshold: " + str(r.pause_threshold))
    print("operation_timeout: " + str(r.operation_timeout))


r = sr.Recognizer()
m = sr.Microphone()
r.pause_threshold = 1.2
adjust_for_ambient_sound()
output_listening_stats()
print("Ready")
