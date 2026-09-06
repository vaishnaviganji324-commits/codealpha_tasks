def chatbot_response(message):
    message = message.lower()

    if message == "hello" or message == "hi":
        return "Hi! Nice to meet you!"

    elif message == "how are you":
        return "I am fine, thanks!"

    elif message == "what is your name":
        return "I am a simple Python chatbot."

    elif message == "what can you do":
        return "I can have a simple conversation with you."

    elif message == "bye" or message == "goodbye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that."


print("================================")
print("       BASIC PYTHON CHATBOT")
print("================================")
print("Type 'bye' to exit the chatbot.")

while True:
    user_input = input("\nYou: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if user_input.lower() == "bye" or user_input.lower() == "goodbye":
        break