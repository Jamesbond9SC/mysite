# All imports
import os
from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import request
from flask import redirect

# Initialising the app
app = Flask(__name__)

# The favicon
@app.route("/favicon.ico")
def favicon():
	return send_from_directory(os.path.join(app.root_path, "static"), "favicon/favicon.ico", mimetype = "image/vnd.microsoft.icon")

# The main page
@app.route("/")
def main_page():
	return render_template("index.html")

# The albums page and sub pages
@app.route("/albums")
def albums_page():
	return render_template("albums.html")
@app.route("/albums/current")
def albums_current():
	cjpgs = os.listdir(os.path.join(app.root_path, "static/media/Current/pictures/jpg"))
	cjpegs = os.listdir(os.path.join(app.root_path, "static/media/Current/pictures/jpeg"))
	return render_template("albums_current.html", cjpgs=cjpgs, cjpegs=cjpegs)
@app.route("/albums/past")
def albums_past():
	pjpgs = os.listdir(os.path.join(app.root_path, "static/media/Past/pictures/jpg"))
	return render_template("albums_past.html", pjpgs=pjpgs)

# The blog page
@app.route("/blog")
def blog_page():
	return render_template("blog.html")

# The about page
@app.route("/about")
def about_page():
	return render_template("about.html")

# The author page (Whole class stuff)
@app.route("/author")
def author_page():
	quotes = []
	quotesfob = open(os.path.join(app.root_path, "static") + "/quotes.txt", "r")
	lines = quotesfob.read().splitlines()
	for line in lines:
		quotes.append(line.split("{diff}"))
	return render_template("author.html", quotes=quotes)

# The credits page
@app.route("/credits")
def credits_page():
	return render_template("credits.html")

# The admin page and sub pages
@app.route("/admin")
def admin_page():
	return render_template("admin.html")

@app.route("/adminblog", methods = ["POST"])
def admin_blog():
	if request.form["password"] == "testpass":
		return render_template("admin_blog.html")
	else:
		return render_template("authfailed.html")

# Testing on localhost
if __name__ == "__main__":
	app.run(host="0.0.0.0")
