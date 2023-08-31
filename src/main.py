from time import sleep
import TTS
import GPT
import STT

conversation = None
while True:
    # if STT.listen_for_keyword("albert"):
        user_input = input("Waiting for input... ") # Text input
        print("Listening...")
        # user_input = STT.get_voice_input(tool="whisper")
        if user_input == None or user_input == '':
            continue
        print(user_input)
        response, conversation = GPT.make_conversation(conversation, user_input)
        TTS.play_text(response)
        # TODO: delete conversation, if the conversation is over, to save on tokens
    # sleep(2)