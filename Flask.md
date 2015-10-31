#Working with Flask

```python
virtualenv flasky
$ source bin activate
(flasky)$ pip install flask
```

#Basic Flask application Structure

All flask application needs to create a *application instance*,
The web server pass all the request it get pass to this application object using a protocol called WSGI
The application instance is an object of class **Flask** , the application object is created using the following code

```python
from flask import Flask
app = Flask(__name__)
```

The only required parameter to the Flask class is the name of the module or file which is given by the magic variable  name 
called **__name__** in python.


#Routes and View Functions

The association between the url and the functions in flask that handle the request is called the route, 
Route mapping is done through the decoraters in python app.route

```python
@app.route('/')
def index():
	return '<h1> Hello world </h1>'
```


> **note: ** Decorators are the standard features of the python programming language, they can modify the behaviour of the functions. Here the function like index() are called the **View** functions.


we can also create the dynamic url mapping, for instance

```python
@app.route('/username/<name>')
def username(name):
	return "<h1> welcome to your Dashboard %s </h1>" % name
```

The portion enclosed in the angle bracket is the dynamic part.
The dynamic components are string by defaults in url, but we can also specify the type in the url like the **Integer** type, `/user/<int:id>`, this url
will be match if the id equals to the integer value, the flask url supports **int float path**


#Starting up a Server
```python
if __name__ == '__main__':
	app.run(debug=True)
```

Once the server startup it goes into the loop and only stop after hitting the control + C keystroke.

Now we can run our app by invoking our python interpreter as,
`python hello.py`

#Application and request Context

Flask use the **Contexts** to make certain objects globally accessibles,
Context enables flask to make access to the certain threads globally without intefering the other threads

Multithreaded web server starts with a **pool** of thread and select the thread from the pool to serve the incomming thread.

##Context in Flask
There are two context in flask

- **Application Context**
- **Request Context**

##Application Contexts

variable_name |  Description
------------- |-------------
current_app	  | The application instance for the running application
get			| An object that can be used by the application for the temporary storage


##Request Context

variable_name | Description
------------  |	------------
request 	  | The request object which encapsulate the content carried by the http request
session 	  |  It is the dictionary that is used to remember the users session

			  
