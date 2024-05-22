import random

# Define responses for each command
responses = {
    "hello": ["Hello! ", "Hi there!", "Hey! How are you doing today?"],
    "how are you": ["I'm good, thanks for asking!", "Feeling great! How about you?"],
    "what's your name": ["I'm a chatbot. What's your name?", "I'm your virtual assistant. What should I call you?"],
    "what time is it": ["It's time to get a watch!", "Looks like it's time for you to check your clock!"],
    "weather": ["It's sunny today.", "Looks like rain. Don't forget your umbrella!"],
    "help": ["Sure, I can help you with various tasks. What do you need assistance with?"],
    "goodbye": ["Goodbye! It was nice chatting with you.", "See you later! Have a great day!"],
    "calculate": ["Let me do the math for you.", "Sure, I can calculate that."],
    "news": ["Let me fetch the latest news for you.", "I'll find the news right away."],
    "joke": ["Here's a joke: Why was the math book sad? Because it had too many problems!", "Did you hear about the claustrophobic astronaut? He needed a little space!"],
    "quote": ["Here's a quote: 'The only way to do great work is to love what you do.' - Steve Jobs", "How about this quote: 'In the end, it's not the years in your life that count. It's the life in your years.' - Abraham Lincoln"],
    "time zone": ["What time zone are you interested in?", "I can tell you the time in any time zone."],
    "calendar": ["Let me check your calendar.", "Sure, I can help you manage your schedule."],
    "recipes": ["What type of recipe are you looking for?", "I can suggest some delicious recipes for you."],
    "reminder": ["Would you like me to remind you about something?", "Sure, I can set a reminder for you."],
    "traffic": ["I can check the traffic for you.", "Let me see what the traffic looks like."],
    "translate": ["What language would you like me to translate?", "Sure, I can translate that for you."],
    "directions": ["Where do you need directions to?", "I can help you find your way."],
    "alarm": ["What time would you like me to set the alarm for?", "Sure, I'll wake you up at that time."],
    "movies": ["What movie are you interested in?", "I can recommend some great movies for you."],
    "music": ["What type of music are you in the mood for?", "I can play some music for you."],
    "book": ["Looking for a specific book or genre?", "I can suggest some interesting books for you to read."],
    "fact": ["Did you know? The Eiffel Tower can be 15 cm taller during the summer!", "Here's a fact: The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes."],
    "wiki": ["What topic would you like me to search on Wikipedia?", "I can find information on any topic for you."],
    "birthday": ["When is your birthday?", "I can help you remember important dates like birthdays."],
    "timer": ["For how long would you like to set the timer?", "Sure, I'll let you know when the time is up."],
    "currency": ["Which currency would you like to convert?", "I can convert currencies for you."],
    "calories": ["What food or exercise would you like me to check the calories for?", "Sure, I can provide you with calorie information."],
    "temperature": ["What location's temperature would you like to know?", "I can check the temperature for you."],
    "definition": ["What word would you like me to define?", "I can provide you with the definition of any word."],
    "tip": ["Here's a tip: Drink plenty of water to stay hydrated!", "How about this tip: Take breaks during work to stay productive."],
    "movie review": ["What movie would you like me to review?", "I can give you my thoughts on any movie."],
    "poem": ["Would you like to hear a famous poem?", "I can recite a poem for you."],
    "exercise": ["Looking for a specific exercise or workout routine?", "I can suggest some exercises for you."],
    "news headline": ["What topic are you interested in?", "I can provide you with the latest headlines."],
    "health tip": ["Here's a health tip: Get regular exercise to stay healthy!", "How about this health tip: Eat plenty of fruits and vegetables for a balanced diet."],
    "reminder": ["What would you like me to remind you about?", "Sure, I can set a reminder for you."],
    "to do list": ["Would you like me to create a to-do list for you?", "I can help you organize your tasks."],
    "grocery list": ["What items do you need to add to your grocery list?", "Sure, I can help you create a grocery list."],
    "phone call": ["Who would you like me to call?", "Sure, I can place a call for you."],
    "email": ["Who would you like to send an email to?", "Sure, I can help you compose an email."],
    "measurement conversion": ["What units would you like me to convert?", "Sure, I can convert measurements for you."],
    "calendar event": ["What event would you like to add to your calendar?", "Sure, I can help you schedule an event."],
    "restaurant recommendation": ["What type of cuisine are you in the mood for?", "I can recommend some great restaurants for you."],
    "tip calculator": ["What was the total bill and how many people are splitting it?", "Sure, I can help you calculate the tip."],
    "movie trailer": ["What movie would you like to see the trailer for?", "I can find the trailer for you."],
    "horoscope": ["What's your zodiac sign?", "I can provide you with your daily horoscope."],
    "travel recommendation": ["Where are you planning to travel to?", "I can suggest some travel destinations for you."],
}
# Define follow-up questions for certain responses
follow_up_questions = {
    "I'm your virtual assistant. What should I call you?": ["Nice to meet you! Is there anything specific you'd like to do today?"],
    "Sure, I can help you with various tasks. What do you need assistance with?": ["Feel free to ask me anything! I'm here to help."],
    "Let me do the math for you.": ["What calculations do you need help with?"],
    "I can suggest some delicious recipes for you.": ["What type of cuisine are you in the mood for?", "I can recommend some great recipes. Do you have any dietary preferences?"],
    "I can provide you with calorie information.": ["What food or exercise would you like me to check the calories for?"],
    "I can check the traffic for you.": ["Where are you headed? I can help you find the best route."],
    "I can convert currencies for you.": ["Which currency would you like to convert, and what's the amount?"],
    "I can tell you the time in any time zone.": ["Which time zone are you interested in?"],
    "Sure, I can help you manage your schedule.": ["Do you have any specific events you need assistance with?"],
    "I'll find the news right away.": ["What kind of news are you interested in?"],
    "What movie are you interested in?": ["What genre of movie are you in the mood for?"],
    "What type of music are you in the mood for?": ["Any specific artist or genre you're interested in?"],
    "Sure, I can play some music for you.": ["What song would you like to listen to?"],
    "I can help you remember important dates like birthdays.": ["Whose birthday would you like me to remember?"],
    "What event would you like to add to your calendar?": ["When is the event, and what's the occasion?"],
    "Sure, I can set a reminder for you.": ["What would you like me to remind you about, and when?"],
    "What topic would you like me to search on Wikipedia?": ["What are you curious to learn more about?"],
    "Would you like me to create a to-do list for you?": ["What tasks would you like to add to your to-do list?"],
    "What items do you need to add to your grocery list?": ["What groceries do you need to buy?"],
    "Who would you like me to call?": ["Whom would you like to call, and what's their number?"],
    "Who would you like to send an email to?": ["To whom would you like to send an email, and what's the message?"],
    "What units would you like me to convert?": ["Which units would you like to convert, and what's the value?"],
    "What movie would you like me to review?": ["Which movie are you interested in getting a review for?"],
    "What food or exercise would you like me to check the calories for?": ["Which food or exercise do you want me to check the calories for?"],
    "What location's temperature would you like to know?": ["Where are you interested in knowing the temperature?"],
    "What word would you like me to define?": ["Which word would you like me to provide a definition for?"],
    "What was the total bill and how many people are splitting it?": ["What's the total bill amount, and how many people are splitting it?"],
    "What type of cuisine are you in the mood for?": ["Do you have any specific preferences or dietary restrictions?"],
    "What movie would you like to see the trailer for?": ["Which movie's trailer are you interested in watching?"],
    "What's your zodiac sign?": ["What's your birth date?"],
    "Where are you planning to travel to?": ["What type of travel experience are you looking for?"],
}


# Main function to handle user input and respond
def chatbot():
    print("Hello! I'm Edison chatbot. How can I assist you today?")
    while True:
        user_input = input("> ").lower()  # Get user input and convert to lowercase
        if user_input == "exit":
            print("Goodbye! It was nice chatting with you.")
            break
        elif user_input == "help":
            print("Here are the commands you can use:")
            for command in responses.keys():
                print("-", command)
        elif user_input in responses:
            response = random.choice(responses[user_input])
            print(response)
            if response in follow_up_questions:
                follow_up_question = random.choice(follow_up_questions[response])
                print(follow_up_question)
        else:
            print("I'm sorry, I don't understand that command. Type 'help' to see available commands.")

# Run the chatbot
chatbot()
