from flask import Flask, url_for
app = Flask(__name__)
@app.route('/')
def home():
          return 'Home Page'
@app.route('/user/<username>')
def profile(username):
          return f'Progile Page Of {username}'   
if __name__ =='__main__':
    app.run()
    with app.test_request_context():
            home_url = url_for('home')
            print(home_url)

            user_url = url_for('profile', username ='johndoe')
            print(user_url)