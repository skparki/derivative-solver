from flask import Flask
import derivativesolver

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the derivative calculator'

@app.route('/<function>')
def derivative_route(function):
    # show the post with the given id, the id is an integer
    return derivativesolver.solve_derivative(function)
