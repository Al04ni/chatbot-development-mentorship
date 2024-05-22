import random
import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'I\'m good, thanks for asking.', 'Fine, thanks.']),
    (r'what is your name?', ['My name is ChatBot.', 'I\'m ChatBot, nice to meet you.']),
    (r'(.*) your name(.*)', ['My name is ChatBot.', 'I\'m ChatBot, nice to meet you.']),
    (r'(.*) help (.*)', ['How can I help you?', 'Sure, what do you need help with?']),
    (r'(.*) (location|city) ?', ['I am located in the internet.', 'I don\'t have a physical location.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

def chat():
    print("Welcome to ChatBot. How can I assist you today? (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("ChatBot:", response)

if __name__ == "__main__":
    nltk.download('punkt')  # Download NLTK data if not already downloaded
    chat()
