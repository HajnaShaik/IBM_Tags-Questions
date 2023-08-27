from flask import Flask, render_template, request
from ml_backend import suggestion, search_stack_overflow

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', suggested_tags=None, question_links=None)

@app.route('/get_tags', methods=['POST'])
def get_tags():
    question = request.form['question']
    suggested_tags = suggestion(question)
    return render_template('index.html', suggested_tags=suggested_tags, question_links=None)

@app.route('/suggest_questions', methods=['POST'])
def suggest_questions():
    question = request.form['question']
    suggested_tags = suggestion(question)
    question_links = search_stack_overflow(suggested_tags)
    return render_template('index.html', suggested_tags=suggested_tags, question_links=question_links)

if __name__ == '__main__':
    app.run(debug=True)
