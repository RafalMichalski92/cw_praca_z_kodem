from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        name = escape(name)  # Zabezpiecz przed potencjalnymi atakami XSS
    else:
        name = "Rafał"  # Domyślne imię, jeśli nie podano parametru
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
