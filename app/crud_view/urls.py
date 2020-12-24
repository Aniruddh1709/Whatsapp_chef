from flask import Blueprint

from flask_restplus import Api
from .resources import WhatsappBot, WhatsappBot2

Whatsapp_bot_1_blueprint = Blueprint('Whatsapp_bot_1', __name__, url_prefix='/Whatsapp_bot_1')
Whatsapp_bot_2_blueprint = Blueprint('Whatsapp_bot_2', __name__, url_prefix='/Whatsapp_bot_2')
api = Api(Whatsapp_bot_1_blueprint)
api.add_resource(WhatsappBot, '/')


api1=Api(Whatsapp_bot_2_blueprint)
api1.add_resource(WhatsappBot2, '/')


