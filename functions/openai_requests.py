import os
import openai
from dotenv import load_dotenv
from functions.database import get_recent_messages
from .prompts import generate_user_message_prompt

load_dotenv()

openai.organization = os.environ.get("OPEN_AI_ORG")
openai.api_key = os.environ.get("OPEN_AI_KEY")


def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript["text"]
    except Exception as e:
        return 

def get_chat_response(decoded_message):
    messages = get_recent_messages()
    user_message = generate_user_message_prompt(decoded_message)
    messages.append(user_message)
    print(messages)

    try:
        response = openai.ChatCompletion.create(
            # model="gpt-3.5-turbo",
            # model="gpt-3.5-turbo-16k",
            # model="gpt-4-32k",
             model="gpt-4",
            # model="gpt-4-1106-preview", #gpt 4 Turbo
            messages=messages
        )
        message_text = response["choices"][0]["message"]["content"]
        return message_text if isinstance(message_text, str) else {"error": "Unexpected response type"}
    except Exception as e:
        return
        
