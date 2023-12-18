import os
import json
from .prompts import generate_learn_instruction

def get_recent_messages():
    file_name = "stored_data.json"
    messages = [generate_learn_instruction()]
    N = 10

    try:
        with open(file_name) as user_file:
            data = json.load(user_file)
            messages.extend(data[-N:] if len(data) >= N else data)
    except:
        pass

    return messages

def store_messages(message_decoded, chat_response):
    file_name = "stored_data.json"
    messages = get_recent_messages()[1:]
    user_message = {"role": "user", "content": message_decoded}
    assistant_message = {"role": "assistant", "content": chat_response}
    messages.extend([user_message, assistant_message])

    with open(file_name, "w") as f:
        json.dump(messages, f)
    return

def reset_messages():
    file_name = "stored_data.json"
    open(file_name, "w").close()
    return
