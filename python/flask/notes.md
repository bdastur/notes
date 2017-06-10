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
