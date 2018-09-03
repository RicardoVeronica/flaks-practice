from flask import Flask, flash, redirect, render_template, request, url_for

from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '06764f14ecad75b8853f1b75e129a965'


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@admin.com' and \
                                                form.password.data == '1234':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unseccessful, please check your email and password',
                  'error')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
