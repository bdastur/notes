# Flask Notes:

## Routes and View functions
The association maintained between a URL and the function that handles it is
called a route.

Clients like web browsers send requests to the web server, which in turn sends
them to the Flask application instance. The application instance needs to know
what code needs to run for each URL requested, so it keeps a mapping of URLs
to python functions.

In Flask the @app.route decorator exposed by the application instance,
 is used to define a route.

 ```
@app.route("/")
def index():
    return '<h1>Hello World</h1>'
 ```

 In this example the function index() is registered as a handler for the
 application's root URL. Functions like index() are called view functions.


## Application and Request Contexts
When flask receives a request from a client, it needs to make a few objects
available to the view function that will handle it. One of them is the *request*
object, which encapsulates the HTTP request sent by the client.

Flask uses contexts to temporarily make certain objects globally accessible.
This way useful objects need not be passed to view functions like arguments.

```
from flask import request

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return "<H1>Your Browser is %s</H1>" % User-Agent

```
Note how the view function can access request as if it was a global variable.
In reality request cannot be a global variable if you consider that in a
multithreaded server the threads are working on different requests from
several different clients at the same time.

Contexts enable Flask to make certain variables globally accessible to a thread
without interfering with other threads.

There are two contexts in Flask. Application context and request context.
Flask activates the application and request contexts before dispatching  a
request and then removes them when the request is handled. When the application
context is pushed, the current_app and g variabels become available to the
thread. Similarly when the request context is pushed, request and session
become available as well.

## Request Dispatching:
When the application receives a request from a client, it needs to find the
view function to invoke to service it. For this, Flask looks up the URL given
in the request in the application's URL map, which contains a mapping of URLs to
the view functions that handle them.

Flask builds this URL map using the app.route decorator or equivalent API
app.add_url_rule().

First app:
https://github.com/bdastur/notes/blob/master/python/flask/first/first.py

```
>>> from first import app
>>> app.url_map
Map([<Rule '/' (HEAD, OPTIONS, GET) -> index>,
 <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
 <Rule '/user/<name>' (HEAD, OPTIONS, GET) -> user>])
>>>

```

In our flask add we only added two Routes '/'   and '/user/<name>'.
The /static/<filename> route is a special route added by Flask to give access
to static files.

The HEAD, OPTIONS, GET elements shown in the URL map are request methods
that are handled by the route. The HEAD and OPTIONS methods are managed
automatically by Flask.

## Request Hooks:
Flask provides a way to execute some code before or after each request is
processed. For eg, you might need to create a DB connection or authenticate
a user when handling a request. Instead of duplicating the code in the
view function, Flask gives you an option to register common functions to
be invoked before or after a request is dispatched to the view function.

Request hooks are implemented as decorators.
There are 4 hooks supported:
1. before_first_request: Register a function to run before the first request
                         is handled.
2. before_request:       Register a function to run before each request.
3. after_request:        Register a function to run after each request, if no
                         unhandled exceptions occured.
4. teardown_request:     Register a function to run after each request, equivalent
                         if unhandled exceptions occured.

A common pattern to share data between the request hook functions and view
functions is to use the g context global. For example, a before_request handler
can load the logged-in user from the database and store it in g.user. Later
when the view function is invoked, it can access the user from there.

## Responses:
When Flask invokes a view function, it expects its return value to be the
response to the request. In most cases the response is a simple string that is
sent back to the client as an HTML page.

But HTTP protocol requires more than a string as a response to a request.
A very important part of the HTTP response is the status code, which Flask by
default sets to 200, the code that indicates the request was carried out
successfully.

When the view function needs to respond with a different status code, it can
add the numeric code as a second return value after the response text.

```
@app.route('/')
def index():
    return '<h1>Bad Request</h1>', 400

```
Responses returned by the view function can also take a third argument,
a dictionary of headers that are added to the HTTP response.

* Instead of returning one, two or three values as a tuple, Flask view functions
  have the option of returning a Response object.
* The make_response() function takes one, two or three arguments,
  the same values that can be returned from a view function, and returns
  a Response object.

  ```
  @app.route('/cookie/')
  def setcookie():
      response = make_response(
      '<h1>Set Cookie</h1>')
      response.set_cookie('answer', '42')
      return response
  ```

A redirect is indicated with a 302 response status code and the URL to redirect
to, given in the Location header. Flask provides a redirect() function
that creates this response.

```
from flask import redirect

@app.route('/redirectme')
def redirect_handler():
    return redirect('/')

```

Another special response is the abort. Flask provides an abort() function which
is used for error handling.
NOTE: that abort does not return control back to the view function. Instead it
gives the control back to the web server by raising an exception.
```
from flask import abort_test

@app.route('/abortonodd/<number>')
def abort_test(number):
    if int(number) % 2 != 0:
        abort(500)
    return '<h2>Numer %s is even</h2>' % number

```


## Blueprints:

### Functional structure:
```
yourapp/
    __init__.py
    static/
    templates/
        home/
        admin/
    views/
        __init__.py
        home.py
        admin.py
    models.py

```

In the functional structure, each file under views/ is a seperate blueprint.
You would import those blueprints in your yourapp/__init__.py and register
them on your Flask() object.


### Divisional structure
```
yourapp/
    __init__.py
    home/
        __init__.py
        views.py
        static/
        templates/
    admin/
        __init__.py
        views.py
        static/
        templates/
    models.py
```

In the divisional structure, each subfolder under yourapp/ is a separate
blueprint. All the blueprints are applied to the Flask() app at the
yourapp/__init__.py.

Choose the one that makes sense for your application.

If your app has largely independent pieces that only share things like
models and configuration, then divisional structure might be better. blueprints
in divisional structure have their own static files and templates completely
separate from other blueprints.

However, if the components in your application flow together a little more,
it might be better to have a functional structure.


The Blueprintexample1 shows a functional structure.


## Flask Forms.

To install this extension:

```
pip install flask-wtf
```

### Cross-Site Request Forgery (CSRF) Protection:
By default, Flask-WTF protects all forms against CSRF attacks. A CSRF attack
occurs when a malicious website sends requests to a different website on
which the victing is logged in.

To implement CSRF protection, Flask-WTF needs the application to configure
an encryption key. Flask-WTF uses this key to generate encrypted tokens
that are used to verify the authenticity of requests with form data.

## Useful links:

* [Slides for flask](http://haifux.org/lectures/294/modern-web-applications.pdf)
* [Flask Restful](https://flask-restful.readthedocs.io/en/latest/quickstart.html)
* [Flask application factories](https://flask.palletsprojects.com/en/1.0.x/patterns/appfactories/)
* [Flask-graphql-mysql-starter-kit](https://medium.com/free-code-camp/how-to-develop-a-flask-graphql-graphene-mysql-and-docker-starter-kit-4d475f24ee76)
* [flask-login](https://scotch.io/tutorials/authentication-and-authorization-with-flask-login)
* [fullstack python flask](https://www.fullstackpython.com/flask.html)
* [How to serve static files with python](https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask)
* [Why do we pass name to flask class](https://blog.miguelgrinberg.com/post/why-do-we-pass-name-to-the-flask-class)
