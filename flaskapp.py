from os import abort
from flask import Flask, render_template, url_for, flash , redirect
from matplotlib.pyplot import title
from requests import post
from forms import RegistrationForm , LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd5a1ef9b6078f0b084f7273c71965c6e'
posts = [
    {
        'author':'Aditya',
        'date' : '19',
        'title' : 'edf',
        'content' : 'aef'
    },
    {
        'author':'Aditya',
        'date' : '19',
        'title' : 'edf',
        'content' : 'aef'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html' , posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register" , methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'ACCOUNT CREATED for {form.username.data} !' , 'success')
        return redirect(url_for('home'))

    return render_template('register.html' , title='Register' , form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html' , title='Login' , form=form)    


if __name__ == '__main__':
    app.run(debug=True)