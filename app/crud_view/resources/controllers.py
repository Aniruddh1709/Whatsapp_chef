from flask import request
from flask_restful import Resource
from flask_restful import reqparse
from twilio.rest import Client 
from twilio.twiml.messaging_response import MessagingResponse
from app import db
from app import app


account_sid = 'secret' 
auth_token = 'secret' 

class WhatsappBot(Resource):
    
    
    parser = reqparse.RequestParser()

    def post(self):
        resp=request.values.get('Body')
        
        
        # args=WhatsappBot.parser.parse_args()
        
 
        
        client = Client(account_sid,auth_token ) 
        if(resp=="Hello"):
            message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hi,How can i help you',      
                              to='whatsapp:+919833129922' 
                          )
        elif(resp=="What's your name"):
            message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='I am your virtual chef',      
                              to='whatsapp:+919833129922' 
                          )
            
 
        print(resp)
        
        return "true"
    
    

