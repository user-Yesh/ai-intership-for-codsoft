import re

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Predefined responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif re.search(r"(name|who are you)", user_input):
        return "I'm ChatBot, your friendly assistant."
    elif "help" in user_input:
        return "Sure! Tell me what you need help with."
    elif re.search(r"(bye|goodbye|see you)", user_input):
        return "Goodbye! Have a great day!"
    elif re.search(r"(time|what time is it)", user_input):
        from datetime import datetime
        return f"It's currently {datetime.now().strftime('%H:%M:%S')}."
    elif re.search(r"(weather|forecast)", user_input):
        return "I can't fetch live weather updates right now, but it's always a good idea to carry an umbrella just in case!"
    elif re.search(r"(joke|funny)", user_input):
        return "Why don't scientists trust atoms? Because they make up everything!"
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"

# Main Chat Loop
def chatbot():
    print("ChatBot: Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("ChatBot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()