from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(28), default='user')
    
    def set_password(self, password):
        """create hashed password"""
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        """checks hashed password"""    
        return check_password_hash(self.password_hash, password)
        
    def __repr__(self):
        return f'<User {self.username}>'
    
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

