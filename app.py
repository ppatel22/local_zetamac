from flask import Flask, render_template, request
from question import generate_multiple_questions

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/questions.html')
def question_page():
    questions, answers = generate_multiple_questions()
    return render_template('questions.html', q_arr=questions, ans_arr=answers)

@app.route('/ending')
def ending_page():
    score = request.args.get('score')
    return render_template('ending.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)