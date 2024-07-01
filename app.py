from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    course = StringField('Course', validators=[DataRequired()])
    short_answer = TextAreaField('Short-form Answer')
    long_answer = TextAreaField('Long-form Answer')
    satisfaction = SelectField('Overall Satisfaction', choices=[
        ('Very Satisfied', 'Very Satisfied'),
        ('Satisfied', 'Satisfied'),
        ('Neutral', 'Neutral'),
        ('Dissatisfied', 'Dissatisfied'),
        ('Very Dissatisfied', 'Very Dissatisfied'),
    ])
    recommendation = RadioField('Would you recommend this course to others?', choices=[
        ('Yes', 'Yes'),
        ('No', 'No'),
    ])
    suggestions = TextAreaField('Suggestions for Improvement')
    submit = SubmitField('Submit')

@app.route('/FeedbackForm/', methods=['GET', 'POST'])
def index():
    form = FeedbackForm()
    if form.validate_on_submit():
        # Process the form data (e.g., save to a database)
        name = form.name.data
        course = form.course.data
        # ... (Access other fields)

        # Redirect or display a success message
        return 'Thank you for your feedback!'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)