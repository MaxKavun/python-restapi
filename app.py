from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works! Hey you, again'

@app.route('/greet')
def say_hello():
  return 'Hello from Server'
app.run(host='0.0.0.0', port=5000)