# All imports
from flask import Flask
from flask import render_template

# Initialising the app
app = Flask(__name__)

# Defining the hello world test function
@app.route("/")
def main_page():
	return render_template("main_page.html")

# Testing on localhost
#if __name__ == "__main__":
#	app.run(host="0.0.0.0")
