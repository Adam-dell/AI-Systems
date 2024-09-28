class MovieEngine:
    def __init__(self):
        self.rules = []
    
    def add_rule(self, condition, response):
        self.rules.append({"condition": condition, "response": response})
    
    def apply_rules(self, text):
        for rule in self.rules:
            if rule["condition"] in text.lower():
                return f"Bot: {rule['response']}"
        
        return "Bot: I don't understand"
        
movie_engine = MovieEngine()

movie_engine.add_rule("hello", "Hi there! How can I help you today?")
movie_engine.add_rule("hi", "Hello! What can I do for you?")
movie_engine.add_rule("recommend me a movie", "Sure! What genre are you interested in?")
movie_engine.add_rule("action", "I recommend 'Mad Max: Fury Road'.")
movie_engine.add_rule("comedy", "How about watching 'Superbad'?")
movie_engine.add_rule("drama", "You might like 'The Shawshank Redemption'.")
movie_engine.add_rule("horror", "Have you seen 'Get Out'? It's really good!")
movie_engine.add_rule("sci-fi", "You should check out 'Inception'.")
movie_engine.add_rule("romantic", "I recommend 'The Notebook'.")
movie_engine.add_rule("goodbye", "Goodbye!")

while True:
    user_input = input("You: ")
    response = movie_engine.apply_rules(user_input)
    print(response)

    if user_input.lower() == "goodbye":
        break

    