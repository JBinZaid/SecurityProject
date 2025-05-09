from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    username = input("Enter the username to promote to admin: ")

    user = User.query.filter_by(username=username).first()

    if not user:
        print(f"User '{username}' not found.")
    else:
        user.role = 'admin'
        db.session.commit()
        print(f"User '{username}' has been promoted to admin.")
