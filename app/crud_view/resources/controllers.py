from flask import request
from flask_restplus import Resource
from flask_restplus import reqparse
from app import db
from app import app




class WhatsappBot(Resource):
    
    
    parser = reqparse.RequestParser()

    def post(self):
        
        args=WhatsappBot.parser.parse_args()
        
        return "true"
    
    
    def get(self):
        pass

class WhatsappBot2(Resource):
    
    parser = reqparse.RequestParser()
    

    def post(self):
        args=WhatsappBot2.parser.parse_args()
        
        
        return "true"

    def get(self):
        pass

