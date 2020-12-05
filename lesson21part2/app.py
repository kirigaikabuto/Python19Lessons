from flask import Flask, render_template, url_for
from livereload import Server

app = Flask(__name__)


@app.route("/")
def index():
    firstName = "Yerassyl"
    lastName = "TLeugazy"
    return render_template("index.html", name=firstName, last_name=lastName)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


@app.route("/products/<name>")
def products(name):
    response = f"product {name}"
    return response


if __name__ == "__main__":
    app.debug = True
    server = Server(app.wsgi_app)
    server.serve()
