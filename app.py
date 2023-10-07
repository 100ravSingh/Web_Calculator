from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/calculate', methods=['POST'])
def add():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    result = num1 + num2

    # Return a partial HTML response
    return jsonify(result=result)

@app.route('/subtract', methods=['POST'])
def subtract():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    result = num1 - num2

    # Return a partial HTML response
    return jsonify(result=result)

@app.route('/multiply', methods=['POST'])
def multiply():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    result = num1 * num2

    # Return a partial HTML response
    return jsonify(result=result)

@app.route('/divide', methods=['POST'])
def division():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Can't divide by Zero"

    # Return a partial HTML response
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
