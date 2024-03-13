from datetime import datetime
from flask import Flask, url_for, request, jsonify
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/route")
def hello_worlds():
    return "<p>Hello, Worlds!</p>"

@app.route("/<param>")
def hello_name(param):
    return f"Hello, {escape(param)}! " 

@app.route("/age/<int:age>", methods = ['GET', 'POST'])
def hello_age(age):
    if request.method == 'POST':
        time = datetime.now()
        print(time.year)
        computed_date = time.year - age 
        return f'You are born in {computed_date}'
    return f"Your age is , {escape(age)}! " 

@app.route("/name", methods = ['GET', 'POST'])
def he():
    if request.method == 'POST':
       data = request.get_json()
       decoded_data = jsonify({"data":data})
    return  decoded_data

@app.route("/login")
def login():
    return "you are loggged in"
@app.route("/logout")
def logout():
    return "logout"

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))

if __name__ == '__main__':
   app.run(debug=True)