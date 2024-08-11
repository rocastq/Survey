from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField

class MyForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    student_number = StringField('Student Number:', validators=[DataRequired()])
    email = StringField('Email Address:', validators=[DataRequired(), Email()])
    grades = TextAreaField('What are your current grades in your courses?', validators=[DataRequired()])
    satisfaction = SelectField('How would you rate your overall satisfaction with your academic experience at GIC?',
                               choices=[('very-satisfied', 'Very Satisfied'), ('satisfied', 'Satisfied'),
                                        ('neutral', 'Neutral'), ('dissatisfied', 'Dissatisfied'),
                                        ('very-dissatisfied', 'Very Dissatisfied')], validators=[DataRequired()])
    suggestions = TextAreaField('Do you have any suggestions for improving the academic experience at GIC?')
    comments = TextAreaField('Is there anything else you\'d like to share about your experience at GIC?')
    submit = SubmitField('Submit')