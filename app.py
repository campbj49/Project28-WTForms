"""Adoption Center application."""

from flask import Flask,render_template, redirect, flash, session, request, jsonify
from models import *
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickenz"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost:5432/adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route("/")
def start():
    """Render landing page with initial list of pets
    """
    
    pets = Pet.query.all()
                  
    return render_template("start.html",
        header = "Adoption Center",
        title = "Choose New Pet",
        pets = pets)
        
@app.route("/add", methods = ['GET', 'POST'])
def add_pet():
    add_pet_form = AddPetForm()
    if add_pet_form.validate_on_submit():
        new_pet = Pet(name = add_pet_form.name.data,
                      species = add_pet_form.species.data,
                      photo_url = add_pet_form.photo_url.data,
                      age = add_pet_form.age.data,
                      notes = add_pet_form.notes.data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")    
        
    return render_template("add.html",
        header = "Adoption Center",
        title = "Choose New Pet",
        form = add_pet_form)
        
@app.route("/<pet_id>",methods = ['GET', 'POST'])
def view_pet(pet_id):
    pet = Pet.query.get(pet_id)
    form = EditPetForm(photo_url=pet.photo_url,
                        notes = pet.notes,
                        available = pet.available)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data 
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect("/") 
        
    return render_template("edit.html",
        title = "Adoption Center",
        header= pet.name,
        form = form,
        pet = pet)