from app import app
from app.crud_view.urls import Whatsapp_bot_1_blueprint, Whatsapp_bot_2_blueprint

app.register_blueprint(Whatsapp_bot_1_blueprint)
app.register_blueprint(Whatsapp_bot_2_blueprint)
