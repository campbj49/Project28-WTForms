from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", 
            validators = [InputRequired()])
    species = StringField("Species", 
            validators = [InputRequired(), AnyOf(['Cat','Dog','Porcupine'])])
    photo_url = StringField("Photo URL", 
            validators = [Optional(), URL()])
    age = IntegerField("Age", 
            validators = [Optional(), NumberRange(min = 0, max = 30)])
    notes = StringField("Notes", 
            validators = [Optional()])
            
class EditPetForm(FlaskForm):
    """Form for editing pets."""
    
    photo_url = StringField("Photo URL", 
            validators = [Optional(), URL()])
    notes = StringField("Notes", 
            validators = [Optional()])
    available = BooleanField("Availabe")
    
    