from flask import Flask, jsonify,request
app=Flask(__name__)

products=[
    {'id':1,'name':'Mobile','price':25000},
     {'id':2,'name':'Tv','price':125000},
     {'id':3,'name':'Charger','price':250},
     {'id':4,'name':'Speakers','price':5000}
]

@app.route('/all', methods=['GET'])
def get_all():
    return jsonify(products)

@app.route('/<int:id>', methods=['GET'])
def get_product(id):
    prod=[prod for prod in products if prod['id']==id]
    return jsonify(prod)

@app.route('/update/<int:id>', methods=['PUT'])
def update_product(id):
    new_product=request.get_json()
    prod=[prod for prod in products if prod['id'] == id]
    if prod:
        prod[0].update(new_product)
        return jsonify({"message":"Product updated"},{"product":prod})
    else:
        return jsonify({"message":"No product found"})

@app.route('/delete/<int:id>', methods=['DELETE'])
def del_product(id):
    prod=[p for p in products if p['id']==id]
    if prod:
        products.remove(prod[0])
        return jsonify({"message":"Product deleted"},{"product":prod})
    else:
        return jsonify({"message":"No product found"})

@app.route('/add', methods=['POST'])
def add():
    new_prod=request.get_json()
    if 'id' not in new_prod or 'name' not in new_prod or 'price' not in new_prod:
        return jsonify({"message":"Invalid data"})
    if any(p['id']==new_prod['id'] for p in products):
        return jsonify({"message":"User already exists"})
    else:
        products.append(new_prod)
        return jsonify({"message":"Product added","product":new_prod})







if __name__=="__main__":
    app.run(debug=True)
