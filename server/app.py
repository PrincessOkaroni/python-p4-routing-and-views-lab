#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Route 1: Home
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route 2: Print
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  
    return parameter 

# Route 3: Count
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = ""
    for i in range(parameter):
        numbers += f"{i}\n"
    return numbers

# Route 4: Math
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

