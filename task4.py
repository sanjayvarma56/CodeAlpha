# BASIC CHATBOT
# PROGRAM RULES / FLOW
# 1. Start the chatbot.
# 2. Ask the user for a message.
# 3. Convert the message to lowercase.
# 4. Check the message and give a predefined reply.
# 5. Continue chatting until the user types "bye".
# 6. End the program when the user enters "bye".

def chatbot():
    print("Chatbot: Hello! I am your chatbot.")
    print("Chatbot: type 'bye' to exit. \n")
    while True:
        user =input("You: ").lower()
        if user == "hello":
            print("ChatBot: Hi!")
            print("ChatBot: How can i help you?")
        elif user == "how are you":
            print("ChatBot: I am fine, thank you!")
        elif user == "what is your name":
            print("ChatBot: My name is ChatBot")
        elif user == "who created you":
            print("ChatBot: I was created by a team of developers using Python.")
        elif user == "bye":
            print("ChatBot: Goodbye! Have a great day!")
            break
        else:
            print("ChatBot: I'm sorry, I don't understand that.")
chatbot()