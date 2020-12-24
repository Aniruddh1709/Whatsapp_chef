from flask import Flask, render_template
from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy







def create_app():
        
    app = Flask(__name__)
    app.config.from_object('config')
    
    
    return app




app=create_app()
db = SQLAlchemy(app)
api=Api(app)




# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Build the database:
# This will create the database file using SQLAlchemy


__import__('app.blueprints')

