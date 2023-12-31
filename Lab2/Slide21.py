from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
app.config.from_pyfile('config.py')
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
