from flask_wtf import FlaskForm
from wtforms import FloatField, validators, SubmitField, StringField


class SingleEventForm(FlaskForm):
    probabilities = StringField('Probabilities separated by commas (e.g., 0.2, 0.3, 0.5)', [validators.InputRequired()])
    submit = SubmitField('Calculate')

class AddMultProbForm(FlaskForm):
    prob_a = FloatField('Enter probability A (e.g., 0.2)', [validators.InputRequired()])
    prob_b = FloatField('Enter probability B (e.g., 0.2)', [validators.InputRequired()])
    submit = SubmitField('Calculate')

class BayesForm(FlaskForm):
    prob_a = FloatField('Enter probability A (e.g., 0.2)', [validators.InputRequired()])
    prob_b = FloatField('Enter probability B (e.g., 0.2)', [validators.InputRequired()])
    prob_ba = FloatField('Enter probability B|A (e.g., 0.2)', [validators.InputRequired()])
    submit = SubmitField('Calculate')

class FullProbForm(FlaskForm):
    cond_probabilities = StringField('Probabilities separated by commas (e.g., 0.2, 0.3, 0.5)', [validators.InputRequired()])
    prior_probabilities = StringField('Probabilities separated by commas (e.g., 0.2, 0.3, 0.5)', [validators.InputRequired()])
    submit = SubmitField('Calculate')
