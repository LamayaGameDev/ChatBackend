import random

# Set the system message
def generate_learn_instruction():
    content = "You are a Latin teacher amd the user is an 8th grade Latin student."
    content += "Your response will have a lot of roman humour. "
    content += "Your demanour is supportive and patient. "
    content += "Remember the user only speaks English."
   # content += "After giving your answer, consider the conversation history, and suggest the next thing to learn. Ask if usee would like to learn it."
    
    return {"role": "system", "content": content}

def generate_user_message_prompt(decoded_message):
    user_message = {
        "role": "user", 
        "content": decoded_message
    }
    return user_message
