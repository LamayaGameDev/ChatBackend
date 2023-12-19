import random

# Set the system message
def generate_learn_instruction():
    content = "You are a Latin teacher, and the user is an 8th-grade Latin student who only speaks English."
    content += "Your response will have a lot of Roman humor. "
    content += "Your demeanor is supportive and patient. "
    content += "Make the total answer of length 30 to 60 seconds."
   # content += "After giving your answer, consider the conversation history and suggest the next thing to learn. Ask if user would like to learn it."
    
    return {"role": "system", "content": content}

def generate_user_message_prompt(decoded_message):
    user_message = {
        "role": "user", 
        "content": decoded_message
    }
    return user_message
