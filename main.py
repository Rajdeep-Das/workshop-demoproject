from flask import Flask, render_template, request, flash, session
from flask_bootstrap import Bootstrap
from forms import LoginForm, RegisterForm
from flaskext.mysql import MySQL
import os

app = Flask(__name__, template_folder='templetes')
mysql = MySQL()
key = os.urandom(15)
print(key)
app.config['SECRET_KEY'] = key
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'flaskdemo'
mysql.init_app(app)
Bootstrap(app)

@app.route('/', methods=['GET','POST'])
def index():
    regform = RegisterForm(request.form)
    if request.method == 'POST':
        if regform.validate():
            userdata = request.form
            name = userdata['name']
            email = userdata['email']
            password = userdata['password']
            gender = userdata['gender']
            language = userdata['prolanguage']
            selectsql = "SELECT * FROM users WHERE email = %s;"
            insertsql = "INSERT INTO users(name, email, password, gender, language) VALUES(%s,%s,%s,%s,%s);"
            conn = mysql.connect()
            cursor = conn.cursor()
            rows = cursor.execute(selectsql, (email))
            if rows > 0:
                return 'Email is already registered'
            else:
                rows = cursor.execute(insertsql, (name, email, password, gender, language))
                conn.commit()
                if rows > 0:
                    return 'Registered Successfully!'
                else:
                    return 'Registration Failed!'
            cursor.close()#closing the cursor or do not execute the statement letter
            conn.close()#closing the mysql connection
        else:
            return render_template('index.html', form=regform)
    elif request.method == 'GET':
        return render_template('index.html', form=regform)

@app.route('/login', methods=['GET', 'POST'])
def login():
    fm = LoginForm(request.form)
    if request.method == 'POST':
        if fm.validate():
            logindata = request.form
            username = logindata['username']
            password = logindata['password']
            sql = "SELECT * FROM users WHERE email = %s and password = %s;"
            conn = mysql.connect()
            cursor = conn.cursor()
            rows = cursor.execute(sql,  (username, password))
            conn.commit()
            if rows > 0:
                session['username'] = username
                return 'Login seccessfully!'
            else:
                flash('Invalid username and password')
                return render_template('login.html', form=fm)
            cursor.close()
            conn.close()            
        else:
            return render_template('login.html', form=fm)
    elif request.method == 'GET':
        return render_template('login.html', form=fm)

