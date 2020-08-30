from flask import Flask, request, Response, abort, make_response, jsonify
from bson import json_util
import os
from datamanager import DataManager

app = Flask(__name__)

DM = DataManager(os.environ['DB_URI'], 'cc', 'shops')


@app.route('/shops', methods=['GET'])
def get_shops(): 
    result = DM.find_all() 
    if result == False:
        return  make_response(jsonify({'error': 'No shops avaible'}), 404)
    return Response(json_util.dumps(result), status=200, mimetype="application/json")


@app.route('/shops/<nombre>', methods=['GET'])
def get_shop(nombre):
    result=DM.find_shop(nombre)
    if result == False:
        return  make_response(jsonify({'error': 'Shop does not exist'}), 404)
    return Response(json_util.dumps(result), status=200, mimetype="application/json")


@app.route('/shops', methods=['POST'])
def post_shop():
    
    if not request.json:
        abort(400)
    if not 'nombre' in request.json:
        abort(400)

    result=DM.find_shop(request.json['nombre'])

    if result == False:
        return  make_response(jsonify({'error': 'Shop does not exist'}), 404)
    else:

        # el unico campo necesario es el nombre
        shop = {
            'nombre': request.json['nombre'],
            'descripcion': request.json.get('descripcion', result['descripcion']),
            'direccion': request.json.get('direccion', result['direccion']),
            'info': request.json.get('info', result['info'])
        }

        if DM.update_one(shop) == True:
            return Response(json_util.dumps("Ok. Shop updated"), status=200, mimetype="application/json") 
        else:
            return  make_response(jsonify({'error': 'Shop not found'}), 404)

    
@app.route('/shops', methods=['PUT'])
def put_shop():
    
    if not request.json:
        abort(400)
    if not 'nombre' in request.json:
        abort(400)
    if not 'descripcion' in request.json:
        abort(400) 
    if not 'direccion' in request.json:
        abort(400)

    shop = {
        'nombre': request.json['nombre'],
        'descripcion': request.json['descripcion'],
        'direccion': request.json['direccion'],
        'info': request.json.get('info', ""),
        'productos':[]
    }

    if DM.save_one(shop) == True:
        return Response(json_util.dumps('Ok. Shop saved.'), status=200, mimetype="application/json")
    else:
        return  make_response(jsonify({'error': 'Shop already exist'}), 404)


@app.route('/shops', methods=['DELETE'])
def delete_shop():

    if not request.json:
        abort(400)
    if not 'nombre' in request.json:
        abort(400)

    if DM.delete_one(request.json['nombre']) == True:
       return Response(json_util.dumps({"Ok. Shop deleted."}), status=200, mimetype="application/json")
    else:
        return make_response(jsonify({'error': 'Shop does not exist'}), 404)
    

@app.route('/shops/<nombre>/<nombre_p>', methods=['GET'])
def get_product(nombre, nombre_p):
    
    result = DM.find_product(nombre, nombre_p)
    if result == False:
        return  make_response(jsonify({'error': 'Shop does not exist or product does not exist'}), 404)
    return Response(json_util.dumps(result), status=200, mimetype="application/json")


@app.route('/shops/<nombre>', methods=['PUT'])
def put_product(nombre):

    if not request.json:
        abort(400)
    if not 'nombre_p' in request.json:
        abort(400)
    if not 'descripcion_p' in request.json:
        abort(400)
    if not 'precio' in request.json:
        abort(400)
    if not 'cantidad' in request.json:
        abort(400)
   
    product = {
        'nombre_p': request.json['nombre_p'],
        'descripcion_p': request.json['descripcion_p'],
        'precio': request.json['precio'],
        'cantidad': request.json['cantidad'],
        'online': request.json.get('isOnline', "True") 
    }

    if DM.insert_product(nombre,product) == True:
        return Response(json_util.dumps({"Ok. Product aded."}), status=200, mimetype="application/json")
    else:
        return make_response(jsonify({'error': 'Shop does not exist or product already exist'}), 404)

@app.route('/shops/<nombre>', methods=['POST'])
def post_product(nombre):
    
    if not request.json:
        abort(400)
    if not 'nombre_p' in request.json:
        abort(400)

    result=DM.find_product(nombre, request.json['nombre_p'])

    if result == False:
        return  make_response(jsonify({'error': 'Shop or product does not exist'}), 404)
    else:

        product = {
            'nombre_p': request.json['nombre_p'],
            'descripcion_p': request.json.get('descripcion_p', result['descripcion_p']),
            'precio': request.json.get('precio', result['precio']),
            'cantidad': request.json.get('cantidad', result['cantidad']),
            'online': request.json.get('online', result['online'])
        }

        if DM.update_product(nombre, product) == True:
            return Response(json_util.dumps("Ok. Product updated"), status=200, mimetype="application/json") 
        else:
            return  make_response(jsonify({'error': 'Shop or product not found'}), 404)


@app.route('/shops/<nombre>', methods=['DELETE'])
def delete_product(nombre):

    if not request.json:
        abort(400)
    if not 'nombre_p' in request.json:
        abort(400)

    if DM.delete_product(nombre, request.json['nombre_p']) == True:
       return Response(json_util.dumps({"Ok. Product deleted."}), status=200, mimetype="application/json")
    else:
        return make_response(jsonify({'error': 'Shop or product does not exist'}), 404)
