from flask import Flask, render_template, request
import sys, os

par_dir = os.path.abspath(os.path.curdir)
print(par_dir)
sys.path.append(os.path.join(par_dir))
from mediaEventManager import MediaEventManager


class WebApp:
    app = Flask(__name__)

    @app.route("/sound/request", methods=["POST"])
    def userInput():
        request_form = request.form
        print(f"user requested: {request.form.get('videoUrl')}")
        print(request.form)
        # send data to mediaEventManager
        if MediaEventManager.build_media(request_form):
            return render_template("user_request_success.html")
        else:
            return render_template("user_request_fail.html")

    @app.get("/")
    def home():
        return render_template("index.html")

    def start_server(debugMode=False):
        WebApp.app.run(host="0.0.0.0", port=1337, debug=debugMode)


if __name__ == "__main__":
    WebApp.start_server(debugMode=True)
