# bad_words = ["stupid", "idiot", "hate", "dumb"]

# def check_cyberbullying(message):
#     message_lower = message.lower()
#     for word in bad_words:
#         if word in message_lower:
#             return "⚠️ Warning: Cyberbullying detected!"
#     return "✅ Safe message."
    
from textblob import TextBlob

# Common bullying / insult words (you can expand this list)
bad_words = [
    "stupid", "idiot", "hate", "dumb", "loser", "ugly", "kill", "disgusting",
    "worthless", "shut up", "hate you", "bitch", "fool", "nonsense", "useless"
]

def check_cyberbullying(message):
    message_lower = message.lower()

    # 🔹 Check for bad words (direct insult detection)
    for word in bad_words:
        if word in message_lower:
            return "⚠️ Warning: Cyberbullying or Harassment Detected!"

    # 🔹 Check for negative emotional tone (sentiment-based)
    analysis = TextBlob(message)
    polarity = analysis.sentiment.polarity  # range: -1 (negative) to +1 (positive)
    
    if polarity < -0.5:
        return "⚠️ Warning: Message has negative / hurtful tone. Please be kind."
    else:
        return "✅ Safe message."
