from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify

app= Flask(__name__)
app.secret_key = 'your_secret_key'
#Basic for routing
# @app.route('/')
# def hello():
#     return "Flask Application"
#
# @app.route('/a')
# def cs():
#     return "Cs Learning Flask"

#Rendering the templete
@app.route('/')
def home():
    return render_template('index.html', message='Hello from Flask!')



#Create routes with parameters:

# @app.route('/')
# def hello():
#     return "Flask Application"
#
# @app.route('/user/<name>')
# def user(name):
#     return f"Hello {name}!!"

#Create a route to handle the form submission:
# @app.route('/greet',methods=['POST'])
# def  greet():
#     name=request.form['name']
#     return f'Hello {name} Welcome'

#Using Flask with Databases
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#
# @app.route('/add_user', methods=['POST'])
# def add_user():
#     name = request.form['name']
#     new_user = User(name=name)
#     db.session.add(new_user)
#     db.session.commit()
#     flash(f'User {name} added successfully!') #flash msg purpose
#     return redirect(url_for('home'))
#
# @app.route('/users')
# def users():
#     users = User.query.all()
#     return render_template('users.html', users=users)

with app.app_context():
    db.create_all()

#Error Handling and Flash Messages
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'),404

#API Development with Flask (Building REST APIs)

# @app.route('/api/users', methods=['GET'])
# def get_users():
#     users=[{"id":1,"name":"Sekhar"},
#            {"id":2,"name":"Sai"}
#            ]
#     return jsonify(users)

#Using Flask with a Database for API
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#
# @app.route('/api/users', methods=['GET'])
# def get_users():
#     users = User.query.all()
#     users_list = [{"id": user.id, "name": user.name} for user in users]
#     return jsonify(users_list)
#
# @app.route('/api/add_user', methods=['POST'])
# def add_user_api():
#     data = request.get_json()
#     name = data.get('name')
#     if not name:
#         return jsonify({"error": "Name is required"}), 400
#     new_user = User(name=name)
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({"message": f"User {name} added successfully!"}), 201

#Authentication and Authorization in Flask
USERS = {"admin": "password123"}
#@app.route('/api/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')
#
#     if not username or not password:
#         return jsonify({"error": "Username and password are required"}), 400
#
#     if USERS.get(username) == password:
#         return jsonify({"message": "Login successful!"}), 200
#     else:
#         return jsonify({"error": "Invalid credentials"}), 401

#Token based
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)
@app.route('/api/protected', methods=['GET'])
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if USERS.get(username) == password:
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@jwt_required()
def protected():
    return jsonify({"message": "You accessed a protected route!"}), 200


if __name__ == '__main__':
    app.run(debug=True)

