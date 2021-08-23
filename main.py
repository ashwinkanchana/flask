from flask import Flask, make_response, jsonify, request

from utils.db import create_table

from routes.create import create_bp
from routes.read import read_bp
from routes.update import update_bp
from routes.delete import delete_bp

app = Flask(__name__)

app.register_blueprint(create_bp)
app.register_blueprint(update_bp)
app.register_blueprint(read_bp, url_prefix='/read')
app.register_blueprint(delete_bp, url_prefix='/delete')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
