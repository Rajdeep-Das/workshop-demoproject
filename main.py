from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import LoginForm

app = Flask(__name__, template_folder='templetes')
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    fm = LoginForm()
    return render_template('login.html', form=fm)

