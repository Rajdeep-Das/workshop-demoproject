from wtforms import Form, TextField, PasswordField, RadioField, SelectField, validators

class LoginForm(Form):
    username = TextField('Username', [validators.Email('Please enter your valid email')])
    password = PasswordField('Password', [validators.Length(min=6, max=15, message='Password should be 6 to 15 characters')])

class RegisterForm(Form):
    name = TextField('Name')
    email = TextField('Email')
    password = PasswordField('Password')
    #('C','C') = ('Value','Label')
    gender = RadioField('Gender', choices=[('Male','Male'),('Female','Female')])
    prolanguage = SelectField('Language', choices=[('C','C'),('CPP','C++'),('Java','Java'),('Python','Python')])
