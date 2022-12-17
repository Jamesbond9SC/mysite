# All imports
from flask import Flask

# Initialising the app
app = Flask(__name__)

# Main domain
@app.route("/")

# Defining the hello world test function
def hello_world():
	return "Hello World..."
