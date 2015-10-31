virtualenv flasky
(flasky)$ pip install flask
(flasky)$ python
	>>> import flask

#Basic Flask application Structure

All flask application needs to create a *application instance*,
The web server pass all the request it get pass to this application object using a protocol called WSGI
The application instance is an object of class **Flask** , the application object is created using the following code

```
from flask import Flask
app = Flask(__name__)
```

The only required parameter to the Flask class is the name of the module or file which is given by the magic variable called __name__ in python.


#Routes and View Functions
The association between the url and the functions in flask that handle the request is called the route, 
Route mapping is done through the decoraters in python app.route

```
@app.route('/')
def index():
	return '<h1> Hello world </h1>'

**note** Decorators are the standard features of the python programming language, they can modify the behaviour of the functions.
Here the function like index() are called the **View** functions.

we can also create the dynamic url mapping, for instance

```
@app.route('/username/<name>')
def username(name):
	return "<h1> welcome to your Dashboard %s" % name
```

The portion enclosed in the angle bracket is the dynamic part.
The dynamic components are string by defaults in url, but we can also specify the type in the url like the **Integer** type, `/user/<int:id>`, this url
will be match if the id equals to the integer value, the flask url supports **int float path**


#Starting up a Server

if __name__ == '__main__':
	app.run(debug=True)
Once the server startup it goes into the loop and only stop after hitting the control + C keystroke.

#Application and request Context

Flask use the **Contexts** to make certain objects globally accessibles,
Context enables flask to make access to the certain threads globally without intefering the other threads

Multithreaded web server starts with a **pool** of thread and select the thread from the pool to serve the incomming thread.

##Context in Flask
There are two context in flask

- **Application Context**
- **Request Context**
