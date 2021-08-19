from flask import Flask, make_response, jsonify, request

from db import create_table
import controller

app = Flask(__name__)

#
@app.route('/api/all', methods=['GET'])
def get_all_task():
    data = controller.get_all_task()
    if(not data):
        return make_response(jsonify({"error":"Something went wrong!"}), 400)
    return make_response(jsonify(data), 200)


@app.route('/api/<id>', methods=['GET'])
def get_task_by_id(id):
    data = controller.get_task_by_id(id)
    if(not data):
        return make_response(jsonify({"error": "Invalid id!"}), 404)
    return make_response(jsonify(data), 200)


@app.route('/api/create', methods=['POST'])
def create_task():
    title = request.form.get("title", None)
    description = request.form.get("description", "")
    if(not title):
        return make_response(jsonify({"error": "title is required!"}), 400)
    insert_id = controller.create_task(title, description)
    if(not insert_id):
        return make_response(jsonify({"error": "Something went wrong!"}), 400)
    return make_response(jsonify({"insert_id": insert_id}), 201)


@app.route('/api/update', methods=['PUT'])
def update_task_by_id():
    id = request.form.get("id", -1)
    title = request.form.get("title", None)
    description = request.form.get("description", "")
    status = request.form.get("status", 0)
    if(id==-1):
        return make_response(jsonify({"error": "id is required!"}), 400)
    elif(not title):
        return make_response(jsonify({"error": "title is required!"}), 400)
    res = controller.update_task_by_id(id, title, description, status)
    if(not res):
        return make_response(jsonify({"error": "Something went wrong!"}), 400)
    return make_response(jsonify({"update_id": id}), 200)


@app.route('/api/delete/<id>', methods=['GET'])
def delete_task_by_id(id):
    res = controller.delete_task_by_id(id)
    if(not res):
        return make_response(jsonify({"error": "Something went wrong!"}), 400)
    return make_response(jsonify({"delete_id": id}), 200)


if __name__ == '__main__':
    create_table()
    app.run(debug=True)
