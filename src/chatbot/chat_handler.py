from src.chatbot.memory import memory


def get_ai_response(user_message: str) -> str:

    # Store user message
    memory.add_user_message(user_message)

    # Temporary mock response
    ai_response = f"I remember you said: '{user_message}'"

    # Store AI response
    memory.add_ai_message(ai_response)

    return ai_response