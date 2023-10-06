from flask import Flask
from config import Config

app = Flask(__name__)
config = Config()
app.config.from_object(config)

@app.route('/')
def home():
    return ('Hello World')
if __name__== '__main__':
    app.run()
