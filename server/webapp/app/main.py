from app import app


# Define a route for the default URL, which loads the form
@app.route('/')
@app.route('/homepage')
@login_required
def homepage():
    return render_template('homepage.html')
