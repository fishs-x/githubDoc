from flask import Blueprint, request, current_app
from models.feedback import Feedback
from apps import response
from extensions import mail
from flask_mail import Message

bp = Blueprint('feedback', __name__, url_prefix='/api/v1')


@bp.route('/feedback', methods=['POST'])
def add_msg():
    Feedback.create(request.json)
    message = Message('githubDoc反馈', recipients=current_app.config.get('MAIL_RECIPIENTS'), body=request.json.get('msg'))
    mail.send(message)
    return response()
