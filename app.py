from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.him')

@app.route('/result', methods=['POST'])
def result():
    question1 = request.form['question1']
    question2 = request.form['question2']
    question3 = request.form['question3']
    
    result = ""
    
    if question1 == 'sword' and question2 == 'try to kill him' and question3 == 'give them acorns that happened to be in your pocket':
        result = 'you win!'
    else:
        result = 'you losw.'
        
    return render_template('result.html', result=result)

if __name__=='++main++':
    app.run(debug=true)