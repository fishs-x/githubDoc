from flask import Blueprint, request
from models.feedback import Feedback
from apps import response

bp = Blueprint('feedback', __name__, url_prefix='/api/v1')


@bp.route('/add/feedback', methods=['POST'])
def add_msg():
    Feedback.create(request.json)
    return response()
