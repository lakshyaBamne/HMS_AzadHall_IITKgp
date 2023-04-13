###############################################################################
# MAIN FLASK APPLICATION ENRTY POINT
###############################################################################

from flask import Flask, render_template,request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

###############################################################################
# Initializing the WSGI application
app = Flask(
    __name__,
    template_folder='templates'
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hms.db'

# creating the class object to make models
db = SQLAlchemy(app)

###############################################################################
# Models for the data base

class Student(db.Model):
    """
        Model represents a Student.
    """
    roll_number = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(20), nullable=False)
    
    student_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    enroll_year = db.Column(db.DateTime, nullable=False)

# class Employee(db.Model):
#     """
#         Model represents an Employees.
#     """

# class Department(db.Model):
#     """
#         Model represents a Department.
#     """

# class AcademicProgram(db.Model):
#     """
#         Model represents an Academic Program.
#     """


# class Secretarypositions(db.Model):
#     """
#         Model represents a Secretary position.
#     """

# class StudentSecretary(db.Model):
#     """
#         Model represents a Student Secretary.
#     """

with app.app_context():
    db.create_all()


###############################################################################
# decorators and their handlers for the flask application

@app.route('/', methods=['GET','POST'])
def index():
    return render_template(
        'index.html'
    )

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == "GET":
        return render_template(
            'signup.html'
        )

    # a new entry is created for the user
    if request.method == "POST":
        new_entry = Student(
            roll_number = request.form['username'],
            password = request.form['password'],
            student_name = request.form['sname'],
            email = request.form['email'],
            contact_number = request.form['cno'],
            enroll_year = request.form['enyear']
        )

        try:
            db.session.add(new_entry)
            db.session.commit()
            return redirect('/signin/')
        except:
            return """[ERROR] Could not create an entry!!"""

@app.route('/signin/', methods=['GET','POST'])
def signin():
    if request.method == "GET":
        return render_template(
            'signin.html'
        )

    if request.method == "POST":
        # let us get the details given by the user
        uname = request.form["username"]
        pword = request.form["password"]
        utype = request.form["user_type"]

        # first we need to check if the given user is in the data base or not

        return render_template(
            'user.html',
            uname=uname,
            utype=utype
        )


@app.route('/user/', methods=['GET','POST'])
def user():
    if request.method == "GET":
        return render_template(
            'user.html'
        )



###############################################################################
# running the application
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True
    )

###############################################################################
