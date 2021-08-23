from flask import Blueprint, make_response, jsonify, request

from controllers.create import create_task

create_bp = Blueprint("create_bp", __name__)


@create_bp.route('/create', methods=['POST'])
def create():
    title = request.form.get("title", None)
    description = request.form.get("description", "")
    if(not title):
        return make_response(jsonify({"error": "title is required!"}), 400)
    insert_id = create_task(title, description)
    if(not insert_id):
        return make_response(jsonify({"error": "Something went wrong!"}), 500)
    return make_response(jsonify({"insert_id": insert_id}), 201)
