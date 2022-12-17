# All imports
from flask import Flask

# Initialising the app
app = Flask(__name__)

# Defining the hello world test function
@app.route("/")
def hello_world():
	return "<p>Hello World...</p>"
