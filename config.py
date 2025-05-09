import os 
from dotenv import load_dotenv



basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secure-key-123'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_ERL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATION = False
    
    # security settings
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESIRE = 'Lax'
    
    # password hashing
    BCRYPT_LOG_ROUNDS = 12    