from . import db


class PropertyInfo(db.Model):
    __tablename__ = 'property_information'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(80))
    rooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price = db.Column(db.Integer)
    type = db.Column(db.String(80))
    location = db.Column(db.String(80))
    photo = db.Column(db.String(80))

    def __init__(self, title, description, rooms, bathrooms, price, type, location, photo):
       self.title = title
       self.description = description
       self.rooms = rooms
       self.bathrooms = bathrooms
       self.price = price
       self.type = type
       self.location = location
       self.photo = photo

    def is_authenticated(self):
        return True

    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Title %r>' % (self.title)