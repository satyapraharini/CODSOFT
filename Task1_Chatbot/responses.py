import random
from knowledge import knowledge

def get_response(user_input):

    user_input = user_input.lower().strip()

    for keyword, answer in knowledge.items():
        if keyword in user_input:
            return answer

    return random.choice([
        "Sorry, I don't understand that.",
        "Can you ask another question?",
        "I'm still learning. Please rephrase your question.",
        "I don't have information about that."
    ])