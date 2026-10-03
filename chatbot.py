# Basic Rule-Based Chatbot

def chatbot():

    print("===== BASIC CHATBOT =====")
    print("Chatbot: Hi! I am a simple Python chatbot.")
    print("Chatbot: Type 'bye' to exit.")

    while True:

        user_input = input("You: ").lower().strip()

        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi! Nice to meet you.")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Chatbot: My name is CodeBot.")

        elif user_input == "help":
            print("Chatbot: You can say hello, ask how I am, or say bye.")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")

# Start chatbot
chatbot()