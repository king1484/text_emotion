from flask import Flask
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def get():
    return str(TextBlob("Nice").polarity)
    

if __name__ == "__main__":
    app.run()
