from flask import Blueprint, make_response, jsonify, request

from controllers.update import update_task_by_id

update_bp = Blueprint("update_bp", __name__)


@update_bp.route('/update', methods=['PUT'])
def update_by_id():
    id = request.form.get("id", -1)
    title = request.form.get("title", None)
    description = request.form.get("description", "")
    status = request.form.get("status", 0)
    if(id == -1):
        return make_response(jsonify({"error": "id is required!"}), 400)
    elif(not title):
        return make_response(jsonify({"error": "title is required!"}), 400)
    res = update_task_by_id(id, title, description, status)
    if(not res):
        return make_response(jsonify({"error": "Something went wrong!"}), 500)
    return make_response(jsonify({"update_id": id}), 200)
