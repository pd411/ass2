from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Regexp, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField(
        label="Username",
        validators=[DataRequired("Please input username")],
        description="username",
        render_kw={
            "class": "input100",
            "placeholder": "Enter username",
        },
    )
    password = PasswordField(
        label='Password',
        validators=[DataRequired("Please input password")],
        description="password",
        render_kw={
            "class": "input100",
            "placeholder": "Enter password",
        },
    )
    remember_me = BooleanField(
        label='Remember me',
        description="Remember Me",
        render_kw={
            "class": "input-checkbox100",
        },
    )

    submit = SubmitField(
        label='login',
        description='submit',
        render_kw={
            "class": "login100-form-btn",
        }
    )

    # def validate_name(self, field):
    #     name = field.data
    #     user = User.query.filter_by(name=name).count()
    #     if user == 1:
    #         raise ValidationError()

class RegisterForm(FlaskForm):
    username = StringField(
        label="Username",
        validators=[DataRequired("Please input username")],
        description="username",
        render_kw={
            "class": "input100",
            "placeholder": "Enter username",
        },
    )

    password = PasswordField(
        label='Password',
        validators=[DataRequired("Please input password")],
        description="password",
        render_kw={
            "class": "input100",
            "placeholder": "Enter password",
        },
    )

    email = StringField(
        label='Email',
        validators=[DataRequired("Please input email")],
        description="email",
        render_kw={
            "class": "input100",
            "placeholder": "Enter email",
        },
    )


    submit = SubmitField(
        label='sign_up',
        description='submit',
        render_kw={
            "class": "login100-form-btn",
        }
    )

    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 1:
            raise ValidationError("Username exist")
