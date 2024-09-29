import re

class chatEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, response):
        self.rules.append({"condition": condition, "response": response})
    
    def apply_rules(self, text):
        for rule in self.rules:
            if re.search(rule["condition"], text, re.IGNORECASE):
                return f"Bot: {rule['response']}"
        
        return "Bot: I don't Understand."
    
chatbot = chatEngine()

chatbot.add_rule(r'\bhello\b|\bhi\b|\bhey\b', "Hello! How can I assist you with your travel plans?")
chatbot.add_rule(r'\brecommend\b.*\btravel\b', "Sure! What type of travel destination are you looking for?")
chatbot.add_rule(r'\badventure\b', "For an adventure, I recommend hiking in the Swiss Alps or exploring the Amazon Rainforest!")
chatbot.add_rule(r'\bbeach\b', "If you like beaches, you could try the Maldives, Hawaii, or Bali.")
chatbot.add_rule(r'\bcity\b|\burban\b', "I would suggest visiting Tokyo, New York City, or Paris for an amazing city experience!")
chatbot.add_rule(r'\bculture\b|\bhistory\b', "How about visiting Rome, Athens, or Kyoto? These cities are rich in history and culture.")
chatbot.add_rule(r'\bbudget\b', "For budget travel, you can explore Southeast Asia, especially Vietnam and Thailand.")
chatbot.add_rule(r'\bluxury\b', "For luxury, I recommend staying at a resort in Bora Bora or a private villa in the Maldives.")
chatbot.add_rule(r'\bthank you\b|\bthanks\b', "You're welcome! I hope you have a great trip!")
chatbot.add_rule(r'\bgoodbye\b|\bbye\b', "Goodbye! Safe travels!")
    

while True:
    user_input = input("You: ")
    response = chatbot.apply_rules(user_input)
    print(response)

    if re.search(r'\bgoodbye\b|\bbye\b', user_input, re.IGNORECASE):
        break