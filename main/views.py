from flask import Blueprint, render_template

views = Blueprint('views', __name__)


# root view
@views.route('/')
def home():
    return render_template("home.html")

# library view
@views.route('/library')
def library():
    return render_template("library.html")

# Associations view
@views.route('/associations')
def associations():
    return render_template("associations.html")

# Advanture view
@views.route('advanture')
def advanture():
    return render_template("advanture.html")

# project detail view
@views.route('/project')
def project_detail():
    return render_template("project_detail.html")