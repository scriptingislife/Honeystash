from flask import Flask, render_template, redirect, request, url_for
from app import app


# Define a route for the default URL, which loads the form
@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')
