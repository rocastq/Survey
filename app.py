from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

@app.route('/')
def home():
    return render_template('Welcome Page.html')

@app.route('/about')
def about():
    return render_template('About us.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        # Handle form submission
        return 'Form submitted successfully!'
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)