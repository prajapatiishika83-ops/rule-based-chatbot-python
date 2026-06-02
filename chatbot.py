while True: 
    user = input("You: ").lower() 
    if user == "hello" or user == "hi": 
        print("Bot: Hello! Nice to meet you.") 
    elif user == "how are you": 
        print("Bot: I am fine. Thank you!") 
    elif user == "what is your name": 
        print("Bot: My name is AI Chatbot.") 
    elif user == "bye" or user == "exit": 
        print("Bot: Goodbye!") 
        break 
    else: 
        print("Bot: Sorry, I don't understand.") 
