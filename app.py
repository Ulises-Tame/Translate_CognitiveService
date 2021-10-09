from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/', methods=['POST'])
def process():
    text = request.form['text']

if __name__ == '__main__':
	app.run(debug=True)