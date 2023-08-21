import TTS
import GPT

convertation = None
while True:
    user_input = input("Waiting for input... ") # TODO: Make this audio input, and wait for a keyword before recording until a end of prompt
    print(user_input)
    response, convertation = GPT.makeConversation(convertation, user_input)
    TTS.playText(response)
    # TODO: delete conversation if the conversation is over to save on tokens