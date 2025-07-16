from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def call_app2():
    try:
        response = requests.get('http://app2:5001/')
        return f"Response from app2: {response.text}"
    except Exception as e:
        return f"Error connecting to app2: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
