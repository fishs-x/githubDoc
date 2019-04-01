from flask import Blueprint
from apps import response
from models.docs import Docs

bp = Blueprint('doc', __name__, url_prefix='/api/v1')


@bp.route('/doc/list')
def doc_list():
    return response(Docs.query.all())
