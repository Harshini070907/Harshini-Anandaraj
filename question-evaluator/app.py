from flask import Flask, render_template, request
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


if __name__ == "__main__":
    app.run(debug=True)