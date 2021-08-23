from flask import Blueprint, make_response, jsonify, request

from controllers.read import get_all_task, get_task_by_id 


read_bp = Blueprint("read_bp", __name__)





@read_bp.route('/all', methods=['GET'])
def get_all():
    data = get_all_task()
    if(not data):
        return make_response(jsonify({"error": "Something went wrong!"}), 500)
    return make_response(jsonify(data), 200)


@read_bp.route('/<id>', methods=['GET'])
def get_by_id(id):
    data = get_task_by_id(id)
    if(not data):
        return make_response(jsonify({"error": "Invalid id!"}), 404)
    return make_response(jsonify(data), 200)
    
@read_bp.route('/', methods=['GET'])
def get():
    return make_response(jsonify({"error": "id required"}), 400)
    
