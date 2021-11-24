from logging import debug
from flask import Flask
import flask
from flask import Flask

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

if __name__ == '__main__':
    print("Runing the application.....................................")
    app.run(debug=True)