from flask import Flask, render_template, request
from mediaEventManager import MediaEventManager


class WebApp:
    app = Flask(__name__)

    @app.route("/sound/request", methods=["POST"])
    def userInput():
        request_form = request.form
        del request_form["submitButton"]
        print(f"user requested: {request.form.get('videoUrl')}")
        # send data to mediaEventManager
        if MediaEventManager.build_media(request_form):
            return render_template("user_request_success.html")
        else:
            return render_template("index.html")

    @app.get("/")
    def home():
        return render_template("index.html")

    def start_server(debugMode=False):
        WebApp.app.run(debug=debugMode, port=1337)

    if __name__ == "__main__":
        start_server(debugMode=True)
