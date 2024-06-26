from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def index():
    options = request.args.getlist('options')
    return render_template('index.html', options=options)

@app.route('/start', methods=['POST'])
def start():
    options = request.form.getlist('options')
    if not options:
        return render_template('index.html', error="Please enter at least one option.")
    return redirect(url_for('index', options=options))

@app.route('/choose', methods=['POST'])
def choose():
    options = request.form.getlist('options')
    if not options:
        return render_template('index.html', error="Please enter at least one option.")
    choice = random.choice(options)
    return render_template('index.html', choice=choice, options=options)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True)