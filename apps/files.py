import os
import urllib.parse
from flask import Blueprint
from apps import response

bp = Blueprint('feedback', __name__, url_prefix='/api/v1')


@bp.route('/<path>/files', methods=['GET'])
def get_files(path):
    root_dir = '/home/www/test'
    files = os.listdir(root_dir + urllib.parse.unquote(path, encoding='utf-8', errors='replace'))
    return response(files)
