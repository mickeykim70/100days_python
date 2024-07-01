from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h2>Hello, World!</h2>"


@app.route("/bye")
def bye():
    return "<h2>Bye!</h2>"

@app.route("/username/<name>")
def greet(name):
    return f"<h2>Hello... there...{name}!</h2>"


if __name__ == "__main__":
    app.run(debug=True)


