from flask import  Flask, render_template, url_for, flash, redirect
from registeration import RegForm,LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='d35604163ea17368193d893066d9328a'

posts=[{ 'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
'date_posted': 'April 20, 2018'},
         {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
}
      ]

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')
@app.route("/register",methods=['GET','POST'])
def register():
    form=RegForm()
    if form.validate_on_submit():
        flash(f'Account created for{form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('registeration.html',title='Registration',form=form)

@app.route("/login")
def login():
    form=LoginForm() 
    return render_template('login.html',title='login',form=form)