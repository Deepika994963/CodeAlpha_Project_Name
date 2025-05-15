import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    
    [r"hi|hello|hey", ["Hello! How can I help you today?"]],
    
    
    [r"what is your name?", ["I am a simple chatbot created using NLTK."]],
    
    
    [r"how are you?", ["I'm just a bot, but I'm here to help you!"]],
    
    
    [r"(.) help (.)", ["Sure, I can help you with that. Could you please specify?"]],
    
    
    [r"bye|exit|quit", ["Goodbye! Have a great day!"]],
    
    [r"i need (.*)", ["What kind of help do you need with %1?"]],
    
    [r"(.*)", ["I'm sorry, I didn't quite get that. Could you please clarify?"]]
]


chatbot = Chat(pairs, reflections)

print("Welcome to the NLTK Chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ")  # Get user input
    if user_input.lower() in ["bye", "exit", "quit"]:  
        print("Chatbot: Goodbye! Have a great day!")
        break
    else:
        print("Chatbot:", chatbot.respond(user_input))  
