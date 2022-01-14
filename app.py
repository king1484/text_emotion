from flask import Flask
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def get():
    return str(TextBlob("Hey its working").polarity)
    

if __name__ == "__main__":
    app.run()
