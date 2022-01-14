from flask import Flask,request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["POST"])
def get():
    data = request.form.get("text")
    return str(TextBlob(data).polarity)
    

if __name__ == "__main__":
    app.run()
