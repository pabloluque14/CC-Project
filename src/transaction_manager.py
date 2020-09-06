from flask import Flask, request, Response, abort, make_response, jsonify
from bson import json_util
import os
from datamanager import DataManager

app = Flask(__name__)

DM = DataManager(os.environ['DB_URI'], 'cc', 'sales')

@app.route('/trans', methods=['GET'])
def get_trans():
    result = DM.find_all() 
    if result == False:
        return  make_response(jsonify({'error': 'No transactions avaible'}), 404)
    return Response(json_util.dumps(result), status=200, mimetype="application/json")

@app.route('/trans/<nombre>', methods=['GET'])
def get_tran(nombre):
    result=DM.find_trans(nombre)
    if result == False:
        return  make_response(jsonify({'error': 'Shop does not exist'}), 404)
    return Response(json_util.dumps(result), status=200, mimetype="application/json")

@app.route('/trans', methods=['PUT'])
def put_tran():
    
    if not request.json:
        abort(400)
    if not 'nombre_t' in request.json:
        abort(400)
    if not 'nombre_p' in request.json:
        abort(400) 
    if not 'cantidad' in request.json:
        abort(400)
    if not 'comprador' in request.json:
        abort(400)

    sale = {
        'nombre_t': request.json['nombre_t'],
        'nombre_p': request.json['nombre_p'],
        'cantidad': request.json['cantidad'],
        'comprador': request.json['comprador']
    }

    if DM.save_trans(sale) == True:
        return Response(json_util.dumps('Ok. Sale saved.'), status=200, mimetype="application/json")