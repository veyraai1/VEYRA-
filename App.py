from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>VEYRA AI IS LIVE!</h1><p>Your AI works for everyone now. No download needed!</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
