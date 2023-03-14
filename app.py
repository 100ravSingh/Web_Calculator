from flask import Flask, request

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    # Get the numbers to add from the request body
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']

    # Calculate the result
    result = num1 + num2

    # Return the result in the response
    return {'result': result}

@app.route('/subtract', methods=['POST'])
def subtract():
    # Get the numbers to add from the request body
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']

    # Calculate the result
    result = num1 - num2

    # Return the result in the response
    return {'result': result}

@app.route('/multiply', methods=['POST'])
def multiply():
    # Get the numbers to add from the request body
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']

    # Calculate the result
    result = num1 * num2

    # Return the result in the response
    return {'result': result}

@app.route('/div', methods=['POST'])
def div():
    # Get the numbers to add from the request body
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']

    # Calculate the result
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Invalid Dividend "

    # Return the result in the response
    return {'result': result}

if __name__ == '__main__':
    app.run()
