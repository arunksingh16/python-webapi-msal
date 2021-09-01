
from flask.json import jsonify
import requests
from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session
import msal
import app_config

# creating instance of Flask class
app = Flask(__name__)
app.config.from_object(app_config)

# using route decorator we will inform flask what url should trigger the function
@app.route('/name/<string:name>/', methods=['GET','POST'])
def welcome(name):
    return "Hello " + name, 200


@app.route('/person/', methods=['GET','POST'])
def person():
    return jsonify({'name':'arun','address':'India'})

@app.route('/numbers/', methods=['GET','POST'])
def print_num():
    # you can send  custom status code as well
    return jsonify(list(range(5))), 200

# the special variable which takes the value of script name. It ensures that our flask app runs only when
# it is executed in the main file
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

