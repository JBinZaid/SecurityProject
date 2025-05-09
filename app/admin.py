from flask import Blueprint, render_template
from flask_login import login_required
from app.utils import admin_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
@login_required
@admin_required
def admin_panel():
    return render_template('admin.html', title='Admin Panel')