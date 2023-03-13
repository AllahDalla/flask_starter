from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, TextAreaField, SelectField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired

class CreateProperty(FlaskForm):
    propertyTitle = StringField("Title", validators=[InputRequired()])
    propertyDescription = TextAreaField("Description", validators=[InputRequired()])
    numberRooms = StringField("No. of Rooms", validators=[InputRequired()])
    numberBathrooms = StringField("No. of Bathrooms", validators=[InputRequired()])
    price = StringField("Price", validators=[InputRequired()])
    propertyType = SelectField("Property Type", choices=[("House", "House"), ("Apartment", "Apartment")])
    location = StringField("Location", validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    addPropertyButton = SubmitField("Add Property")