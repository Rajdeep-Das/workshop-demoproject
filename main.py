from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from forms import LoginForm

app = Flask(__name__, template_folder='templetes')
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

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

