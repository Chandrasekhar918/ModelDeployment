from flask import  Flask,jsonify,request
app=Flask(__name__)

data=[
    {'id':1,'Name':'Sekhar1','City':'Bangalore1'},
    {'id':2,'Name':'Sekhar2','City':'Bangalore2'},
    {'id':3,'Name':'Sekhar3','City':'Bangalore3'}
]

@app.route('/all',methods=['GET'])
def get_op():
    return jsonify(data)

@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user= [u for u in data if u['id']==id]
    if user:
        return jsonify(user)
    else:
        return "No User found"

@app.route('/useradd', methods=['POST'])
def add_user():
    new_user=request.get_json()
    if 'id' not in new_user or 'Name' not in new_user or 'City' not in new_user:
        return jsonify({"Message":"Invalid data"})
    if any(u['id']==new_user['id'] for u in data):
        return  jsonify({"message":"User already exists"})
    else:
        data.append(new_user)
        return jsonify({"message": "User added successfully"})




@app.route('/userupdate/<int:id>', methods=['PUT'])
def update_user(id):
    updated_data=request.get_json()
    user=[u  for u in data if u['id']==id]
    if user:
        user[0].update(updated_data)
        return jsonify({"message":"User updated","user":user})
    else:
        return jsonify({"error not found"}),404


@app.route('/userdel/<int:id>', methods=['DELETE'])
def del_user(id):
    user=[u for u in data if u['id']==id]
    if user:
        data.remove(user[0])
        return jsonify({"message":"User deleted","user":user})
    else:
        return "No User with that id found"



if __name__=='__main__':
    app.run(debug=True)


