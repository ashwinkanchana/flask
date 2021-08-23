from flask import Blueprint, make_response, jsonify, request

from controllers.delete import delete_task_by_id

delete_bp = Blueprint("delete_bp", __name__)


@delete_bp.route('/<id>', methods=['GET'])
def delete_one_by_id(id):
    res = delete_task_by_id(id)
    if(not res):
        return make_response(jsonify({"error": "Something went wrong!"}), 500)
    return make_response(jsonify({"delete_id": id}), 200)


@delete_bp.route('/', methods=['GET'])
def delete():
    return make_response(jsonify({"error": "id required"}), 400)
