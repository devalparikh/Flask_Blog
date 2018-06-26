from flask import Flask, render_template
app = Flask(__name__)

#Mock Database Response
posts = [

    {
        'author': 'Deval Parikh',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 25, 2018'
    },
    {
        'author': 'Bob Builder',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 28, 2018'
    },

]


#Back End Route

#Home Page Route
@app.route("/")
@app.route("/home")
def home():
    #Takes in posts data
    return render_template('home.html', posts=posts)

#About Page Route
@app.route("/about")
def about():
    #HTML Header Tag
    return render_template('about.html', title='About')

#Debug Mode if ran via python
if __name__ == '__main__':
    app.run(debug=True)
