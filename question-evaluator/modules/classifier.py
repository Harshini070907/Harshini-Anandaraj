def classify_question(question):
    question = question.lower()

    remembering = ["define", "list", "state", "identify", "name"]
    understanding = ["explain", "describe", "summarize", "interpret"]
    higher = ["analyze", "compare", "evaluate", "justify", "criticize"]

    if any(word in question for word in remembering):
        return "Remembering (Easy)"

    elif any(word in question for word in understanding):
        return "Understanding (Medium)"

    elif any(word in question for word in higher):
        return "Higher Order (Hard)"

    else:
        return "Uncategorized"