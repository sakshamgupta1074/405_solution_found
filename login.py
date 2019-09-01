# Route for handling the login page logic
from flask import Flask
from flaskext.mysql import MySQL
import os

app = Flask(__name__)
app.config.from_object('config')
from flask import Flask, render_template, redirect, url_for, request
@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'local_health' and request.form['password'] == 'admin':
            return render_template('forms.html')
        elif request.form['username'] == 'state_health' and request.form['password'] == 'admin':
            return render_template('data.html')
        elif request.form['username'] == 'national_health' and request.form['password'] == 'admin':
            return render_template('data.html')
        else:
        	error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)
if __name__ == '__main__':
	app.run()