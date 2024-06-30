from flask import Blueprint, render_template

employee_view = Blueprint('employee_view', __name__)

@employee_view.route('/')
def index():
    return render_template('index.html')
