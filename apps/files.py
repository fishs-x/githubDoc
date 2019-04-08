import os
from flask import Blueprint
from apps import response

bp = Blueprint('feedback', __name__, url_prefix='/api/v1')


@bp.route('/<path>/files', methods=['GET'])
def get_files(path):
    root_dir = '/home/www/test'
    files = os.listdir(root_dir + path)
    return response(files)
