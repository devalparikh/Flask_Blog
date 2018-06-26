from flask import Flask
app = Flask(__name__)

#Back End Route

#Home Page Route
@app.route("/")
def hello():
    #HTML Header Tag
    return "<h1>Home Page<h1>"

#Home Page Route
@app.route("/about")
def about():
    #HTML Header Tag
    return "<h1>About Page<h1>"

#Debug Mode if ran via python
if __name__ == '__main__':
    app.run(debug=True)
