from flask import Flask

app = Flask("moshe")


@app.route('/')
def hello_world():
    return 'Hello! I am a Flask application'


app.run(host='0.0.0.0', port="8080")
