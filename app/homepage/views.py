from flask import render_template

from . import homepage

@homepage.route('/')
@homepage.route('/home')
def home():
    return render_template('home.html')