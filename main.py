from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

class LoginForm(FlaskForm):
    username = StringField('id Астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль Астронавта', validators=[DataRequired()])
    username_cap = StringField('id Капитана', validators=[DataRequired()])
    password_cap = PasswordField('Пароль Капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('index.html', title='Миссия колонизации марса', form=form)


if __name__ == '__main__':
    print('http://127.0.0.1:8080/login')
    app.run(port=8080, host='127.0.0.1')