from flask import Blueprint

from flask_restful import Api
from .resources import WhatsappBot

Whatsapp_bot_1_blueprint = Blueprint('Whatsapp_bot_1', __name__, url_prefix='/')

api = Api(Whatsapp_bot_1_blueprint)
api.add_resource(WhatsappBot, '/')



