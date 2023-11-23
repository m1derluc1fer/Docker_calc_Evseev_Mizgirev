from flask import Flask, request, jsonify

app = Flask(__name__)

nobody = 0

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = data['num1'] + data['num2']
    return jsonify({'result': result})

@app.route('/pass', methods=['POST'])
def add():
    pass

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    result = data['num1'] - data['num2']
    return jsonify({'result': result})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    result = data['num1'] * data['num2']
    return jsonify({'result': result})

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    num2 = data['num2']
    
    if num2 == 0:
        return jsonify({'error': 'Divide by zero'})
    
    result = data['num1'] / num2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
