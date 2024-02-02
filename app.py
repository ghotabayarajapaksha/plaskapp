from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def hello():
    requests.get("https://test-0qs4.onrender.com/")
    requests.get("https://kk-k7rgdman.b4a.run/")
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
