from flask import Flask, render_template, request
from src.preprocess import clean_text, tokenize_sentences
from src.task_extractor import extract_task

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_text():
    text = request.form["text"]

    # Preprocess and tokenize sentences
    clean_data = clean_text(text)
    sentences = tokenize_sentences(clean_data)

    # Extract tasks and associate names
    tasks = extract_task(sentences)

    return render_template("result.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)
