from flask import Flask

PORT = 8000

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/test')
def hello2():
    return "Hola prueba!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)