from flask import Flask
import multiprocessing
import requests
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Return a simple string as the content to be displayed
    return 'Hello, World!'

def run_exblog():
    print('Starting exblog...')

    urls = ["https://test-0qs4.onrender.com/", "https://kk-k7rgdman.b4a.run/"]
    
    while True:
        [requests.get(url) for url in urls]
        time.sleep(600)  # 10 minutes = 600 seconds

if __name__ == '__main__':
    # Start a new process to run_exblog
    exblog_process = multiprocessing.Process(target=run_exblog)
    exblog_process.start()

    # Run the Flask app with '0.0.0.0' as the host to make it externally accessible
    app.run(host='0.0.0.0', port=5000)

    # Ensure that the process is properly terminated when the application exits
    exblog_process.join()
