from flask import Flask

# flask -> название библиотеки
# Flask -> это название метода который позволит получить доступ к возможностям back-end
app = Flask(__name__)


# route
@app.route("/")
def home():
    a = 3
    b = 4
    return str(a + b)


@app.route("/about")
def about1():
    return "It is about page"


@app.route("/about/<param1>")
def about2(param1):
    return "It is about page " + param1


@app.route("/about/<param1>/<param2>")
def about3(param1, param2):
    return "It is about page " + param1 + " " + param2


# /parametrs
# /contacts -> it is contacts page
# /products -> it is products page
if __name__ == "__main__":
    app.run()
