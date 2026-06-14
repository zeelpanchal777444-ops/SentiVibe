# from textblob import TextBlob

# def detect_mood(text):
#     analysis = TextBlob(text)
#     polarity = analysis.sentiment.polarity

#     if polarity > 0.3:
#         return "Happy 😊"
#     elif polarity < -0.3:
#         return "Sad 😢"
#     else:
#         return "Neutral 😐"

from textblob import TextBlob

def detect_mood(text):
    text_lower = text.lower()
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    # Keyword-based emotional correction
    sad_keywords = ["lonely", "alone", "missing", "broken", "hurt", "depressed", "cry", "tears", "pain", "sad","miss","can't","not good"]
    happy_keywords = ["happy", "joy", "excited", "grateful", "smile", "love", "fun", "enjoy","not-sad"]
    romantic_keywords = ["love", "crush", "romantic", "kiss", "heart", "together", "miss you"]
    angry_keywords = ["angry", "mad", "frustrated", "irritated", "hate"]
    relaxed_keywords = ["calm", "peaceful", "relaxed", "chill", "breeze", "quiet", "soothing"]

    # Check for keyword-based moods first
    if any(word in text_lower for word in sad_keywords):
        return "Sad 😢"
    elif any(word in text_lower for word in happy_keywords):
        return "Happy 😊"
    elif any(word in text_lower for word in romantic_keywords):
        return "Romantic 💞"
    elif any(word in text_lower for word in angry_keywords):
        return "Angry 😠"
    elif any(word in text_lower for word in relaxed_keywords):
        return "Relaxed 😌"

    # Fallback to sentiment polarity
    # if polarity > 0.3:
    #     return "Happy 😊"
    # elif polarity < -0.3:
    #     return "Sad 😢"
    # else:
    #     return "Neutral 😐"
    if polarity > 0.6:
        return "Happy 😊"
    elif polarity > 0.2:
        return "Romantic 💞"
    elif polarity < -0.6:
        return "Sad 😢"
    elif polarity < -0.2:
        return "Angry 😠"
    else:
        return "Neutral 😐"
