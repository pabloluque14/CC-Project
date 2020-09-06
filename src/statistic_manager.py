from flask import Flask, request, Response, abort, make_response, jsonify
from bson import json_util
import os
from datamanager import DataManager

app = Flask(__name__)

DM = DataManager(os.environ['DB_URI'], 'cc', 'statistics')

@app.route('/stats', methods=['GET'])
def get_stats():
    result = DM.find_all() 
    if result == False:
        return  make_response(jsonify({'error': 'No statistics avaible'}), 404)
    return Response(json_util.dumps(result), status=200, mimetype="application/json")

@app.route('/stats/<nombre>', methods=['GET'])
def get_stat(nombre):
    result=DM.find_trans(nombre)
    if result == False:
        return  make_response(jsonify({'error': 'Statistic does not exist'}), 404)
    return Response(json_util.dumps(result), status=200, mimetype="application/json")

@app.route('/stats', methods=['PUT'])
def put_stat():
    
    if not request.json:
        abort(400)
    if not 'nombre_t' in request.json:
        abort(400)
    if not 'ventas' in request.json:
        abort(400) 
    if not 'puntuacion' in request.json:
        abort(400)

    trans = {
        'nombre_t': request.json['nombre_t'],
        'ventas': request.json['ventas'],
        'puntuacion': request.json['puntuacion']
        
    }

    if DM.save_trans(trans) == True:
        return Response(json_util.dumps('Ok. Statistic saved.'), status=200, mimetype="application/json")