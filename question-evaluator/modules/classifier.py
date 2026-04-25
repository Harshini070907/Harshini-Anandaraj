def classify_question(question):
    question = question.lower()

    easy = ["define", "list", "state", "identify", "name"]
    medium = ["explain", "describe", "summarize", "interpret", "apply"]
    hard = ["analyze", "compare", "evaluate", "justify", "criticize"]

    if any(word in question for word in easy):
        return "Easy"
    elif any(word in question for word in medium):
        return "Medium"
    elif any(word in question for word in hard):
        return "Hard"
    else:
        return "Uncategorized"
    
def classify_questions_list(questions):
    result = {
        "Easy": [],
        "Medium": [],
        "Hard": [],
        "Uncategorized": []
    }

    for q in questions:
        q = q.strip()
        if not q:
            continue
        
        category = classify_question(q)
        result[category].append(q)

    return result