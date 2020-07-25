from wtforms import Form, TextField, PasswordField, validators

class LoginForm(Form):
    username = TextField('Username', [validators.Email('Please enter your valid email')])
    password = PasswordField('Password', [validators.Length(min=6, max=15, message='Password should be 6 to 15 characters')])