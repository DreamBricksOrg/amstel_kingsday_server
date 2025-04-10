from flask import Flask

app = Flask(__name__)

@app.route('/alive')
def home():
    return "alive"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", ssl_context='adhoc')
