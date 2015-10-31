from flask import Flask
from flask import request
from flask import redirect
from flask.ext.script import Manager

app = Flask(__name__)


@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	return "You are using %s browser" % user_agent

@app.route('/user/<name>')
def name(name):
	return "You said your name is %s" % name

@app.route('/google')
def google():
	return redirect("http://google.com.np")

manager = Manager(app)

if __name__ == '__main__':
	manager.run()