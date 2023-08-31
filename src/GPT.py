import os
import requests
from requests.structures import CaseInsensitiveDict
import json
import tiktoken

# OpenAI API key for Albert
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

# Chat GPT Config
CHATGPT_MODEL_NAME = "gpt-3.5-turbo"
CHATGPT_API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
MAX_RESPONSE_TOKENS=250
TOKEN_LIMIT=4096

HEADERS = CaseInsensitiveDict()
HEADERS["Content-Type"] = "application/json"
HEADERS["Authorization"] = f"Bearer {OPENAI_API_KEY}"


def num_tokens_from_messages(messages):
    encoding= tiktoken.get_encoding("cl100k_base")  #model to encoding mapping https://github.com/openai/tiktoken/blob/main/tiktoken/model.py
    num_tokens = 0
    for message in messages:
        num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":  # if there's a name, the role is omitted
                num_tokens += -1  # role is always required and always 1 token
    num_tokens += 2  # every reply is primed with <im_start>assistant
    return num_tokens

# Function to generate prompts using ChatGPT API
def get_answer(setup, verbose = False):
    data = {
        "model": CHATGPT_MODEL_NAME,
        "temperature": 0.7,
        "max_tokens": 256,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "messages": setup
    }
    if verbose: 
        print(data)

    response = requests.post(CHATGPT_API_ENDPOINT, headers=HEADERS, data=json.dumps(data))
    if verbose: 
        print(response)

    if response.status_code == 200:
        response_data = json.loads(response.text)
        if verbose: 
            print(response_data)
        response_string = response_data['choices'][0]['message']['content']
        return response_string
    else:
        print("Failed to generate prompts using ChatGPT API.")
        print(response.status_code)
        print(response.text)
        return None


def make_conversation(conversation, user_input, verbose = False):
    
    if conversation is None:
        # Initial conversation setup if needed
        system_message = {"role": "system", "content": "You are an assistant named Albert. Address the person you are assisting as 'My Good Sir'. Give short and helpful answers. Ask clarifying questions, if needed, to better assist."}
        conversation = []
        conversation.append(system_message)
    elif len(conversation) > 10:
        return
    
    if user_input is not None:
        conversation.append({"role": "user", "content": user_input})
        conv_history_tokens = num_tokens_from_messages(conversation)

        # Remove oldest messages from conversation if exceeding token limit
        while conv_history_tokens + MAX_RESPONSE_TOKENS >= TOKEN_LIMIT:
            del conversation[1] 
            conv_history_tokens = num_tokens_from_messages(conversation)

        # Query ChatGPT
        response_string = get_answer(conversation, True)

        conversation.append({"role": "assistant", "content": response_string})
        if (verbose):
            print(response_string)
            print(conversation)
        return response_string, conversation