from app import db
import datetime
# Define a base model for other database tables to inherit
class Base(db.Model):
    
    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())
    
    #TODO FIGURE OUT IF DB FUNCTIONS ARE ENOUGH
    @classmethod
    def create(cls,**kwargs):
        item=cls()
        
        item.date_created = datetime.datetime.now()
        return item
    
    @classmethod
    def update(cls,**kwargs):
        item=cls()
        item.date_modified=datetime.datetime.now()
        return item