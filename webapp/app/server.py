from flask import Flask, render_template
import sys
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

def start_server(debugMode=False):
    app.run(debug=debugMode)

if __name__ == "__main__":
    start_server(True)
