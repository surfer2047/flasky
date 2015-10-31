from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	return "You are using %s browser" % user_agent

@app.route('/user/<name>')
def name(name):
	return "You said your name is %s" % name

if __name__ == '__main__':
	app.run(debug=True)