from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello world</h1>"

@app.route('/hello', methods=['POST', 'GET'])
def hello():
    response = make_response("HELLO WORLD\n")
    response.status_code = 202
    response.headers['content-type'] = 'application/octet-stream'
    return response

@app.route('/hello1', methods=['POST', 'GET'])
def hello1():
    return "Hello GET\n", 201
    
@app.route('/hello2', methods=['POST', 'GET'])
def hello2():
    if request.method == 'GET':
        return "Hello GET\n"
    elif request.method == 'POST':
        return "Hello POST\n"
    else:
        return 'You will never see this message\n'

@app.route('/great/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f"{greeting} {name}"
    else:
        return "some params are missing"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)

