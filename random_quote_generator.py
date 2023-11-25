import random
def GRQ():
    quotes=["The only way to do great work is to love what you do. - Steve Jobs",
        "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
        "Believe you can and you're halfway there. -Theodore Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt",
        "Don't watch the clock; do what it does. Keep going. -Sam Levenson",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt"]
    return random.choice(quotes)

print(GRQ())