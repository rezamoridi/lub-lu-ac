from flask import Blueprint, render_template

views = Blueprint('views', __name__)


#define a view
@views.route('/')
def home():
    return render_template("home.html")