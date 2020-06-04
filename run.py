import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            # Do not use 'debug=True' in actually applications, only when testing, like here! :)
            debug=True)