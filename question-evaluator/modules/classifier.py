def classify_question(question):
    question = question.lower()

    easy = ["define", "list", "state", "identify", "name"]

    medium = ["explain", "describe", "summarize", "interpret", "apply"]

    hard = [
        "analyze", "compare", "evaluate", "justify", "criticize",
        "differentiate", "distinguish", "discuss", "examine", "illustrate"
    ]

    # PRIORITY: HARD → MEDIUM → EASY
    if any(word in question for word in hard):
        return "Hard"

    elif any(word in question for word in medium):
        return "Medium"

    elif any(word in question for word in easy):
        return "Easy"

    else:
        return "Medium"
    
def classify_questions_list(questions):
    result = {
        "Easy": [],
        "Medium": [],
        "Hard": []
    }

    for q in questions:
        q = q.strip()
        if not q:
            continue
        
        category = classify_question(q)
        result[category].append(q)

    return result