from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
app.count = 0

@app.route('/')
def index():
    session['count'] += 1
    return render_template('index.html', count=session['count'])

@app.route('/inclement', methods=['POST'])
def inclement():
    session['count'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)
