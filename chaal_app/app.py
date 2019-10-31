from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Chaal!"

if __name__ == "___main___":
    app.run(debug=True, host="0.0.0.0")