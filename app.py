# # from flask_jwt_extended import JWTManager, jwt_required, create_access_token
# # from flask_sqlalchemy import SQLAlchemy
# # from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
# #
# # app= Flask(__name__)
# # app.secret_key = 'your_secret_key'
# # # #Basic for routing
# # # # @app.route('/')
# # # # def hello():
# # # #     return "Flask Application"
# # # #
# # # # @app.route('/a')
# # # # def cs():
# # # #     return "Cs Learning Flask"
# # #
# # # #Rendering the templete
# # # @app.route('/')
# # # def home():
# # #     return render_template('index.html', message='Hello from Flask!')
# # #
# # # @app.route('/homes')
# # # def homes():
# # #     return "Welcome to the Home Page!"
# # #
# # # @app.route('/about')
# # # def about():
# # #     return f"Go to Home: <a href='/'>{url_for('homes')}</a>"
# # #
# # # from flask import Flask, render_template
# # # from flask_wtf import FlaskForm
# # # from wtforms import StringField, SubmitField
# # # from wtforms.validators import DataRequired
# # #
# # # app = Flask(__name__)
# # # app.config['SECRET_KEY'] = 'mysecretkey'
# # #
# # # class MyForm(FlaskForm):
# # #     name = StringField('Name', validators=[DataRequired()])
# # #     submit = SubmitField('Submit')
# # #
# # # @app.route('/', methods=['GET', 'POST'])
# # # def index():
# # #     form = MyForm()
# # #     if form.validate_on_submit():
# # #         return f'Hello, {form.name.data}!'
# # #     return render_template('test.html', form=form)
# # #
# # # if __name__ == "__main__":
# # #     app.run(debug=True)
# # #
# # # #Create routes with parameters:
# # #
# # # # @app.route('/')
# # # # def hello():
# # # #     return "Flask Application"
# # # #
# # # # @app.route('/user/<name>')
# # # # def user(name):
# # # #     return f"Hello {name}!!"
# # #
# # # #Create a route to handle the form submission:
# # # # @app.route('/greet',methods=['POST'])
# # # # def  greet():
# # # #     name=request.form['name']
# # # #     return f'Hello {name} Welcome'
# # #
# # # #Using Flask with Databases
# # # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# # # db = SQLAlchemy(app)
# # # #
# # # # class User(db.Model):
# # # #     id = db.Column(db.Integer, primary_key=True)
# # # #     name = db.Column(db.String(100), nullable=False)
# # # #
# # # # @app.route('/add_user', methods=['POST'])
# # # # def add_user():
# # # #     name = request.form['name']
# # # #     new_user = User(name=name)
# # # #     db.session.add(new_user)
# # # #     db.session.commit()
# # # #     flash(f'User {name} added successfully!') #flash msg purpose
# # # #     return redirect(url_for('home'))
# # # #
# # # # @app.route('/users')
# # # # def users():
# # # #     users = User.query.all()
# # # #     return render_template('users.html', users=users)
# # #
# # # with app.app_context():
# # #     db.create_all()
# # #
# # # #Error Handling and Flash Messages
# # # @app.errorhandler(404)
# # # def not_found(error):
# # #     return render_template('error.html'),404
# #
# # #API Development with Flask (Building REST APIs)
# #
# # # @app.route('/api/users', methods=['GET'])
# # # def get_users():
# # #     users=[{"id":1,"name":"Sekhar"},
# # #            {"id":2,"name":"Sai"}
# # #            ]
# # #     return jsonify(users)
# #
# # #Using Flask with a Database for API
# # # class User(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True)
# # #     name = db.Column(db.String(100), nullable=False)
# # #
# # # @app.route('/api/users', methods=['GET'])
# # # def get_users():
# # #     users = User.query.all()
# # #     users_list = [{"id": user.id, "name": user.name} for user in users]
# # #     return jsonify(users_list)
# # #
# # # @app.route('/api/add_user', methods=['POST'])
# # # def add_user_api():
# # #     data = request.get_json()
# # #     name = data.get('name')
# # #     if not name:
# # #         return jsonify({"error": "Name is required"}), 400
# # #     new_user = User(name=name)
# # #     db.session.add(new_user)
# # #     db.session.commit()
# # #     return jsonify({"message": f"User {name} added successfully!"}), 201
# #
# # #Authentication and Authorization in Flask
# # USERS = {"admin": "password123"}
# # #@app.route('/api/login', methods=['POST'])
# # # def login():
# # #     data = request.get_json()
# # #     username = data.get('username')
# # #     password = data.get('password')
# # #
# # #     if not username or not password:
# # #         return jsonify({"error": "Username and password are required"}), 400
# # #
# # #     if USERS.get(username) == password:
# # #         return jsonify({"message": "Login successful!"}), 200
# # #     else:
# # #         return jsonify({"error": "Invalid credentials"}), 401
# #
# # #Token based
# # # app.config['JWT_SECRET_KEY'] = 'your_secret_key'
# # # jwt = JWTManager(app)
# # # @app.route('/api/protected', methods=['GET'])
# # # @app.route('/api/login', methods=['POST'])
# # # def login():
# # #     data = request.get_json()
# # #     username = data.get('username')
# # #     password = data.get('password')
# # #
# # #     if not username or not password:
# # #         return jsonify({"error": "Username and password are required"}), 400
# # #
# # #     if USERS.get(username) == password:
# # #         access_token = create_access_token(identity=username)
# # #         return jsonify({"access_token": access_token}), 200
# # #     else:
# # #         return jsonify({"error": "Invalid credentials"}), 401
# # #
# # # @jwt_required()
# # # def protected():
# # #     return jsonify({"message": "You accessed a protected route!"}), 200
# #
# # @app.route('/')
# # def home():
# #     return render_template('index.html')
# # @app.route('/get_data')
# # def get_data():
# #     return jsonify(message="Hello from Flask!")
# # if __name__ == '__main__':
# #     app.run(debug=True)
# # #
# #
# # from flask import Flask, request, jsonify, render_template
# # import joblib
# # import numpy as np
# #
# # app = Flask(__name__)
# #
# # # Load the trained model
# # model = joblib.load('C:/Users/bansekha/OneDrive - Capgemini/Desktop/ML Practice/logistic_regression_model.pkl')
# #
# # @app.route('/')
# # def home():
# #     return render_template('index.html')
# #
# # @app.route('/predict', methods=['POST'])
# # def predict():
# #     try:
# #         # Get input from the form
# #         input_data = request.form['input_data']
# #         # Convert input to numpy array and reshape for prediction
# #         input_array = np.array([float(x) for x in input_data.split(',')]).reshape(1, -1)
# #
# #         # Make prediction
# #         prediction = model.predict(input_array)
# #
# #         # The prediction is either 0 or 1. You can display more meaningful labels.
# #         if prediction[0] == 1:
# #             result = 'Class 1 (Predicted label: 1)'  # Replace with more meaningful interpretation
# #         else:
# #             result = 'Class 0 (Predicted label: 0)'  # Replace with more meaningful interpretation
# #
# #         # Return the result to be shown in the HTML template
# #         return render_template('index.html', prediction=result)
# #
# #     except Exception as e:
# #         return f"Error during prediction: {str(e)}"
# # if __name__ == '__main__':
# #     app.run(debug=True)
#
# # from flask import Flask
# #
# # app = Flask(__name__)
# #
# # @app.route("/")
# # def home():
# #     return "Hello, Flask is running!"
# #
# from flask import Flask, render_template, request
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "Hello, Flask is running!"
#
# @app.route("/support-form", methods=["GET", "POST"])
# def support_form():
#     if request.method == "POST":
#         cust_id = request.form["cust_id"]
#         wifi_name = request.form["wifi_name"]
#         description = request.form["description"]
#         return f"✅ Ticket raised for Wi-Fi {wifi_name} (Customer ID: {cust_id})"
#
#     return """
#     <h2>Raise a Support Ticket</h2>
#     <form method="post">
#         Customer ID: <input type="text" name="cust_id"><br>
#         Wi-Fi Name: <input type="text" name="wifi_name"><br>
#         Description: <textarea name="description"></textarea><br>
#         <input type="submit" value="Submit">
#     </form>
#     """
#
# if __name__ == "__main__":
#     app.run(port=5000)
#
#
# if __name__ == "__main__":
#     app.run(port=5000)  # Run on port 5000
#
#

from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel
import os
import uvicorn

app = FastAPI()

# Load model and scaler from the correct path inside the Docker container
model_path = os.path.join(os.getcwd(), "Log_Reg.pkl")
scaler_path = os.path.join(os.getcwd(), "scaler.pkl")

with open(model_path, "rb") as file:
    model = pickle.load(file)

with open(scaler_path, "rb") as file2:
    scaler = pickle.load(file2)

# Define request body format
class InputData(BaseModel):
    age: int
    estimated_salary: float

# Define prediction endpoint
@app.post("/predict/")
def predict(data: InputData):
    # Convert input to NumPy array
    input_data = np.array([[data.age, data.estimated_salary]])

    # Apply scaling
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_scaled)

    # Return response
    return {"prediction": int(prediction[0])}

# Ensure the app runs on PORT 8080 inside the container
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))  # Read PORT from environment (default 8080)
    uvicorn.run(app, host="0.0.0.0", port=port)
