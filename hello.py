from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)


@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	return '<h1>You are running %s browser</h1>' %user_agent



@app.route('/name/<name>')
def name(name):
	return "I think your name is %s" %name

@app.route('/fuck')
def fuck():
	response = make_response("<h1> Bad request </h1>")
	response.set_cookie('answer', 42)
	return response
		


if __name__ == '__main__':
    app.run(debug=True)
