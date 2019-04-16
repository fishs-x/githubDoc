import os
import urllib.parse
from flask import Blueprint,request
from apps import response

bp = Blueprint('files', __name__, url_prefix='/api/v1')
root_dir = '/home/www/markdowns'

@bp.route('/select/file', methods=['POST'])
def get_files():
    print(request.json)
    paths = request.json.get('path')
    title = request.json.get('title')
    path = ''
    data = {'path': '', 'is_dir': False}
    for fname in paths:
        path = fname + '/' + path
        abs_path = os.path.join(root_dir, title, path)
        if abs_path[-1] == '/':
            abs_path = abs_path[:-1]
        abs_path = urllib.parse.unquote(abs_path)
        if not os.path.exists(abs_path):
            continue
        data['is_dir'] = os.path.isdir(abs_path)
        data['path'] = abs_path[len(root_dir):]
        break
    return response(data)


@bp.route('/list/dir', methods=['POST'])
def list_dir():
    data = []
    path = request.json.get('path', '')
    abs_path = root_dir + path
    for item in os.listdir(abs_path):
        if item in  item[-4:] in ['.png', '.git', 'nore', 'ENSE'  '.jpg', 'jpeg']:
            continue
        data.append({"file_name": item, "path": os.path.join(path, item), "is_dir": os.path.isdir(os.path.join(abs_path, item))})
    return response(data)

