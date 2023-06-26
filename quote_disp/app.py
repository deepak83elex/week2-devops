import random

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/health")
def health():
    return "healthy"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_quote")
def quote():
    # quote = requests.get("http://week2-devops-web1-1:5000/quote").text
    hosts = [
        "http://week2-devops-web1-1:5000/quote",
        "http://week2-devops-web1-2:5000/quote"
    ]

    quote = "Quote service is unvailable"

    for host in hosts:
        r = requests.get(host)
        if r.status_code == 200:
            quote = r.text
            break
    
    print("quote - ", quote)

    return render_template("quote.html", quote=quote)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
