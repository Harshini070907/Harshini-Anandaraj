from flask import Flask, render_template, request
from docx import Document
from modules.classifier import classify_questions_list
from modules.classifier import classify_question

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        question = request.form["question"]

        if not question.strip():
            return "Please enter a question"

        result = classify_question(question)

        return render_template("result.html",
                               question=question,
                               result=result)

    return render_template("index.html")

def read_docx(file_path):
    doc = Document(file_path)
    questions = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            questions.append(text)

    return questions

@app.route("/process-all")
def process_all():
    intro_questions = read_docx("intro.docx")
    networking_questions = read_docx("networking.docx")

    intro_result = classify_questions_list(intro_questions)
    networking_result = classify_questions_list(networking_questions)

    return {
        "Intro to Computer": intro_result,
        "Networking": networking_result
    }

if __name__ == "__main__":
    app.run(debug=True)