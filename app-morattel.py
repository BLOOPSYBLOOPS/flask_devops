from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """Bonjour je m'appelle Bryan Morattel - Test du Pipline Batman PRIME 
              Bonjour ajout depuis la branche Kevin"""

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
