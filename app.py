#--Flask Hello World--#

#import flask
from flask import Flask

#create application object
app = Flask(__name__)

#use decorators to link the functions to a URL 
@app.route("/")
@app.route("/hello")

#define the view using a function, which returns a string 
def helloWorld():
	return "Hello World!"

#Start the development server using the run() method 
if __name__ == "__main__":
	app.run()