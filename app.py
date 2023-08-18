from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    question1 = request.form['question1']
    question2 = request.form['question2']
    question3 = request.form['question3']
    
    result = ""
    
    if question1 == 'Mech' and question2 == 'Try to kill him' and question3 == 'Give them acorns that happened to be in your pocket':
        result = 'You win!'
    else:
        result = 'You lose.'
        
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)