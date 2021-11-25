from logging import debug
from flask import Flask, url_for, redirect
import flask


print("Flask version is",flask.__version__)

app = Flask(__name__)


@app.route('/home')
def hello_world():
    print("Routing to /home and Entering into hello_world function")
    return 'HIIIIIIIIIIIIIIIIIIIIII!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'


## read this
'''
https://flask.palletsprojects.com/en/2.0.x/quickstart/#unique-urls-redirection-behavior
'''


@app.route('/home/')
def hello_pranav():
    print("Routing to /about/ and Entering into hello_pranav function")
    return 'HELLLOOO  WELCOME TO THE SECRET PAGE'


@app.route('/guest/<guest>')
def hello_guest(guest):
    print("Entering into hello_guest function")
    return f"Welcome {guest}!"


@app.route('/admin')
def hello_admin():
    print("Entering into hello_admin function")
    return "Welcome admin!!!!!!!"


@app.route('/user/<name>')
def hello_user(name):
    print("Entering into hello_user")
    if name == 'admin':
        print("ADMIN")
        return redirect(url_for('hello_admin'))
    else:
        print("NAME")
        return redirect(url_for('hello_guest', guest = name))


if __name__ == '__main__':
    print("Runing the application.....................................")
    app.run(debug=True)