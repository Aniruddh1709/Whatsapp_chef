import os
import re
import requests
import urllib.parse
from io import BytesIO
from PIL import Image
from app import app
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from flask import request,jsonify
from flask_restful import Resource
from flask_restful import reqparse
from app.prediction import predict_image
from twilio.rest import Client 
from twilio.twiml.messaging_response import  Message, MessagingResponse
from app.prediction.search import search , get_links


account_sid = os.environ.get('TWILIO_ACCOUNT_SID') 
auth_token = os.environ.get('TWILIO_AUTH_TOKEN') 

client = Client(account_sid,auth_token ) 


class WhatsappBot(Resource):
    
    
    parser = reqparse.RequestParser()

    def post(self):
        
        try:
            print("debug 0")
            res=request.values.get('Body')
            # resp = MessagingResponse()
            if(res=="Hello" or res=="Hi" or res=="hello" or res=="hi"):
                print("debug 1")
                message = client.messages \
                .create(
                        
                        from_='whatsapp:YOUR_TWILIO_NUMBER',
                        body='Hi,I am your virtual chef.Send a picture or name of the dish that you would like to cook today',
                        to='whatsapp:YOUR_NUMBER'
                       )
                print("1")
                # resp.append(Message('This is an SMS message from Twilio!'))
                # return str(resp)
                return "True"
            elif request.values['NumMedia'] != '0':
                print("debug 2")
                print(request.values['MediaUrl0'])
                image_url = request.values['MediaUrl0']
                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))
                fi=predict_image(img)
                g_search,youtubelink=search(fi)
                message = client.messages \
                    .create(
                    
                        from_='whatsapp:YOUR_TWILIO_NUMBER',
                        body='Here are some links for recipes',
                        to='whatsapp:YOUR_NUMBER'
                    )
                message = client.messages \
                    .create(
                    
                        from_='whatsapp:YOUR_TWILIO_NUMBER',
                        body=(list(g_search)[0]),
                        to='whatsapp:YOUR_NUMBER'
                    )
                message = client.messages \
                    .create(
                    
                        from_='whatsapp:YOUR_TWILIO_NUMBER',
                        body=(list(g_search)[1]),
                        to='whatsapp:YOUR_NUMBER'
                    )
                message = client.messages \
                    .create(
                    
                        from_='whatsapp:YOUR_TWILIO_NUMBER',
                        body=(list(g_search)[2]),
                        to='whatsapp:YOUR_NUMBER'
                    )
                    
                    
                return "True"
                
                
            else:
                print("debug 3")
                
                g_search = []
                y_search = []
                g_search, y_search = search(str(res))
                message = client.messages \
                        .create(
                        
                            from_='whatsapp:YOUR_TWILIO_NUMBER',
                            body='Here are some links for recipes',
                            to='whatsapp:YOUR_NUMBER'
                       )
                message = client.messages \
                    .create(
                        
                        from_='whatsapp:YOUR_TWILIO_NUMBER',
                        body=(list(g_search)[0]),
                        to='whatsapp:YOUR_NUMBER'
                       )
                message = client.messages \
                    .create(
                        
                        from_='whatsapp:YOUR_TWILIO_NUMBER',
                        body=(list(g_search)[1]),
                        to='whatsapp:YOUR_NUMBER'
                       )
                message = client.messages \
                    .create(
                        
                        from_='whatsapp:YOUR_TWILIO_NUMBER',
                        body=(list(g_search)[2]),
                        to='whatsapp:YOUR_NUMBER'
                       )
                
                return "True"
                

                    
                
        except:
            message = client.messages \
                    .create(
                        
                        from_='whatsapp:YOUR_TWILIO_NUMBER',
                        body="Invalid Message,Try again later",
                        to='whatsapp:YOUR_NUMBER'
                       )
                    
            return "True"

        
        
        
        
        
        
        
        
        
        
        
        
            
 
        
    
    

