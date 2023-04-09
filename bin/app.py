###############################################################################
# MAIN FLASK APPLICATION ENRTY POINT
###############################################################################

from flask import Flask, render_template

###############################################################################
# Initializing the WSGI application
app = Flask(
    __name__,
    template_folder='templates'
)

###############################################################################
# decorators and their handlers for the flask application

@app.route('/', methods=['GET','POST'])
def index():
    return render_template(
        'index.html'
    )

@app.route('/signin/', methods=['GET','POST'])
def signin():
    return render_template(
        'signin.html'
    )

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    return render_template(
        'signup.html'
    )

###############################################################################
# running the application
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True
    )

###############################################################################
