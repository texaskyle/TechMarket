from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError

from market.models import User


class RegisterForm(FlaskForm):
    # validating is another user has registered using the same username
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user and user != current_user:  # Assuming you have a current_user object
            raise ValidationError("Username already exists! Try using another username.")
    # validating is another user has registered using another email
    
    def validate_email_address(self, email_address_to_check):
        user = User.query.filter_by(email_address=email_address_to_check.data).first()
        if user and user != current_user:  # Assuming you have a current_user object
            raise ValidationError("Email already exists! Try another email address.")

    username = StringField("username", validators=[Length(min=4, max=25), DataRequired()])
    email_address = StringField('email address', validators=[Email(), Length(min=6), DataRequired()])
    password1 = PasswordField("password", validators=[Length(min=4, max=35), DataRequired()])
    password2 = PasswordField("Confirm Password", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField("Create Account")


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("Sign In")