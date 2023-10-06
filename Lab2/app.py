from flask import Flask 
from auth import auth_bp 
app = Flask(__name__) 
app.config.from_pyfile('config.py')
app.register_blueprint(auth_bp) 
if __name__=='__main__': 
    app.run()
    