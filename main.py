from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from forms import LoginForm, RegisterForm

app = Flask(__name__, template_folder='templetes')
Bootstrap(app)

@app.route('/', methods=['GET','POST'])
def index():
    regform = RegisterForm(request.form)
    if request.method == 'POST':
        if regform.validate():
            return 'Registered Successfully!'
        else:
            return render_template('index.html', form=regform)
    elif request.method == 'GET':
        return render_template('index.html', form=regform)

@app.route('/login', methods=['GET', 'POST'])
def login():
    fm = LoginForm(request.form)
    if request.method == 'POST':
        if fm.validate():
            return 'Submitted!'
        else:
            return render_template('login.html', form=fm)
    elif request.method == 'GET':
        return render_template('login.html', form=fm)

