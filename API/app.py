from flask import Flask, request, jsonify

app = Flask(__name__)


@app.get("/<location>")
def get_weather(location):
    
    
    if __name__ == '__main__':
        app.run(debug=True)