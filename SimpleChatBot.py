# Simple chatbot example

def chatbot():
    print("Chatbot: Hello! I'm your friendly chatbot. How can I assist you today?")
    
    while True:
        # Get user input
        user_input = input("You: ").lower()
        
        # Quit condition
        if "exit" in user_input or "quit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Basic responses
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm here to help!")
        elif "your name" in user_input:
            print("Chatbot: I'm ChatBot 1.0. What's your name?")
        elif "time" in user_input:
            from datetime import datetime
            print(f"Chatbot: The current time is {datetime.now().strftime('%H:%M:%S')}.")
        elif "help" in user_input:
            print("Chatbot: Sure! You can ask me about the weather, time, or just chat.")
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Could you rephrase?")

# Run the chatbot
chatbot()
