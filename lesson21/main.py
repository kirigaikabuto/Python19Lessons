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
def about():
    return "It is about page"

#/contacts -> it is contacts page
#/products -> it is products page
if __name__ == "__main__":
    app.run()
