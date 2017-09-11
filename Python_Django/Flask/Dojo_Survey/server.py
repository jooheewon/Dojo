from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result/<name>/<location>/<language>/<comment>', methods=["POST"])
def get_survey(name, location, language, comment):
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    return render_template('result.html', name = name, location = location, language = language, comment = comment)

@app.route('/', methods=['POST'])
def back():
    return redirect('/')


app.run(debug=True)