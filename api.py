from flask import Flask, render_template, request
from derivativesolver import *
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/answer', methods=['POST'])
def answer():
    # show the post with the given id, the id is an integer
    # derivativesolver.solve_derivative(function)
    # flask - Calling a python function with a button
    function = request.form['function']
    derivative = solve_derivative(function)
    return render_template('answer.html', function=function, answer=derivative)

# app.send_static_file("./view/index.html")

if __name__ == '__main__':
    app.run(debug=True)
