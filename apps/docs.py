from flask import Blueprint
from apps import response
from models.docs import Docs

bp = Blueprint('doc', __name__, url_prefix='/api/v1')


@bp.route('/list/doc')
def doc_list():
    return response(Docs.query.filter_by(is_hidden=0).order_by(Docs.sort).all())
