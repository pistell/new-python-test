#--Flask Hello World--#

#import flask
from flask import Flask

#create application object
app = Flask(__name__)

#error handling
app.config["DEBUG"] = True

#use decorators to link the functions to a URL 
@app.route("/")
@app.route("/hello")


#define the view using a function, which returns a string 
def hello_world():
	return "Hello World???????!"

#dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

@app.route("/integer/<int:value>")
def int_type(value):
	print value + 1
	return "correct"

#dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
	print value
	return value

@app.route("/name/<name>")
def index(name):
	if name.lower() == "mike" :
		return "Hello, {}".format(name), 200
	else :
		return "Not Found", 404


#Start the development server using the run() method 
if __name__ == "__main__":
	app.run()