from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/login', methods = ["GET", "POST"])  # '/' for the default page
def login():
	if request.method = "GET":
  	return render_template('login.html')
  else:
  	Username = request.form["username"]
  	Password = request.form["password"]

  	return redirect(url_for('home', un=Username, Pass=Password))

@app.route('/')
def home():
	render_template('home.html', friends=facebook_friends)

@app.route('/friend_exists/<string:name>')
def friend_exists(name):
	flag = true
	if name in facebook_friends:
		return render_template("friend_exists.html", flag=flag)
	else:
		flag = false
		return render_template("friend_exists.html", flag=flag)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)