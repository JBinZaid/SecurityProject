from flask import Blueprint, render_template
from flask_login import login_required
from app.models import User
from app.utils import sanitize_input

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@login_required
def index():
    return render_template('dashboard.html', title='Dashboard')