# Imports
from flask import Flask, render_template, request
import logging

# Setup
app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html'
    )


@app.route('/Statistics')
def stats():
    return render_template(
        'statistics.html'
    )


@app.route('/About')
def about():
    return render_template(
        'about.html'
    )

# Every thing is good- Lets go!
app.run(debug=True)