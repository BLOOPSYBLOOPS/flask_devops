from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Bonjour, ceci est mon projet Flask DevOps - morattel test de jenkins WOW WOW WOW cest le deuxième test"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
