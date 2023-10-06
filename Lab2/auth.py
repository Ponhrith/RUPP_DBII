from flask import Blueprint 

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth') 

@auth_bp.route('/') 
def index(): 
    return 'This is auth index' 

@auth_bp.route('/register')
def register(): 
    return 'This is to register'
