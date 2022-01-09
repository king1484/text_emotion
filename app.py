from flask import Flask
import text2emotion as te

app = Flask(__name__)

@app.route("/")
def get():
    return str(te.get_emotion("hi friends))
if __name__ == "__main__":
    app.run()
