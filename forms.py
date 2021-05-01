# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField, BooleanField
# from wtforms.validators import DataRequired, Length, Email, EqualTo

# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min = 2, max = 45)])
#     email = StringField('email', validators = [DataRequired(), Email()])
#     password = PasswordField('Password', validators = [DataRequired()])
#     confirm_password = PasswordField('Confirm', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up')

# class LoginForm(FlaskForm):
#     email = StringField('email', validators = [DataRequired(), Email()])
#     password = PasswordField('Password', validators = [DataRequired()])
#     remember = BooleanField('Remember Me')
#     login = SubmitField('Log In')