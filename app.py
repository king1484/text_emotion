from flask import Flask
import text2emotion as te

app = Flask(__name__)

@app.route("/")
def get():
    return "Hello world"

if __name__ == "__main__":
    app.run()
