from flask import render_template

from . import calc
from .forms import AddMultProbForm, SingleEventForm, BayesForm, FullProbForm
from .formulas import adding_formula, multiplying_formula, single_event_formula, bayes_formula, full_probability_formula


@calc.route('/adding', methods=['GET', 'POST'])
def adding():
    form = AddMultProbForm()
    result = 0

    if form.validate_on_submit():
        prob_a = form.prob_a.data
        prob_b = form.prob_b.data
        result = adding_formula(prob_a, prob_b)

    return render_template('adding.html', form=form, result=result)


@calc.route('/multiplying', methods=['GET', 'POST'])
def multiplying():
    form = AddMultProbForm()

    result = 0

    if form.validate_on_submit():
        prob_a = form.prob_a.data
        prob_b = form.prob_b.data
        result = multiplying_formula(prob_a, prob_b)

    return render_template('multiplying.html', form=form, result=result)

@calc.route('/single_event', methods=['GET', 'POST'])
def single_event():
    form = SingleEventForm()

    result = 0

    if form.validate_on_submit():
        probabilities_string = form.probabilities.data
        probabilities = [float(prob) for prob in probabilities_string.split(',')]
        result = single_event_formula(probabilities)

    return render_template('single_event.html', form=form, result=result)

@calc.route('/bayes', methods=['GET', 'POST'])
def bayes():
    result = 0
    form = BayesForm()


    if form.validate_on_submit():
        prob_a = form.prob_a.data
        prob_b = form.prob_b.data
        prob_ba = form.prob_ba.data

        result = bayes_formula(prob_a, prob_b, prob_ba)

    return render_template('bayes.html', form=form, result=result)

@calc.route('/full_prob', methods=['GET', 'POST'])
def full_prob():
    form = FullProbForm()
    result = 0
    if form.validate_on_submit():
        cond_prop_string = form.cond_probabilities.data
        cond_prop = [float(prob) for prob in cond_prop_string.split(',')]
        prior_prop_string = form.cond_probabilities.data
        prior_prop = [float(prob) for prob in prior_prop_string.split(',')]

        result = full_probability_formula(cond_prop, prior_prop)
    return render_template('full_prob.html', form=form, result=result)
