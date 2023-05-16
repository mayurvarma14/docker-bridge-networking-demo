from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello from Service 1!'

@app.route('/helloworld')
def helloworld():
    return 'Hello World from Service 1!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
