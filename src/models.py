import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# Tabla PLANETAS
class Planet(db.Model):
    __tablename__ = "planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    gravity = db.Column(db.String)
    population = db.Column(db.Integer)
    climate = db.Column(db.String)
    terrain = db.Column(db.String)
    surface_water = db.Column(db.Integer)
    created = db.Column(db.Date)
    edited = db.Column(db.Date)
    photo = db.Column(db.String)
    liked_by_users = relationship("Fav_Planet", backref="planet")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": f"https://3000-peach-spoonbill-64imvwko.ws-us03.gitpod.io/{self.id}",
            "description": self.description,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "created": self.created,
            "edited": self.edited,
            "photo": self.photo
        }

#Tabla PERSONAJES
class Characters(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String)
    skin_color = db.Column(db.String)
    eye_color = db.Column(db.String)
    birth_year = db.Column(db.Date)
    gender = db.Column(db.String)
    created = db.Column(db.Date)
    edited = db.Column(db.Date)
    photo = db.Column(db.String)
    liked_by_users = relationship("Fav_Characters", backref="characters")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": f"https://3000-peach-spoonbill-64imvwko.ws-us03.gitpod.io/{self.id}",
             "description": self.description,
             "height": self.height,
             "mass": self.mass,
             "hair_color": self.hair_color,
             "skin_color": self.skin_color,
             "eye_color": self.eye_color,
             "birth_year": self.birth_year,
             "gender": self.gender,
             "created": self.created,
             "edited": self.edited,
             "photo": self.photo
        }

#Tabla FAVORITOS PLANETAS
class Fav_Planet(db.Model):
    __tablename__ = "fav_planet"
    id_FavPlanets = db.Column(db.Integer, primary_key=True)
    id_Planets = db.Column(db.Integer, ForeignKey("planet.id"))
    id_Username = db.Column(db.Integer, ForeignKey("user_table.uid"))

    def serialize(self):
        return {
            "id_FavPlanets": self.id_FavPlanets,
            "id_Planets": self.id_Planets,
            "id_Username": self.id_Username
        }

#Tabla FAVORITOS PERSONAJES
class Fav_Character(db.Model):
    __tablename__ = "fav_character"
    id_FavCharacters = db.Column(db.Integer, primary_key=True)
    id_Character = db.Column(db.Integer, ForeignKey("characters.id"))
    id_Username = db.Column(db.Integer, ForeignKey("user_table.uid"))

    def serialize(self):
        return {
            "id_FavCharacters": self.id_FavCharacters,
            "id_Characters": self.id_Characterss,
            "id_Username": self.id_Username
        }

# Tabla USUARIOS
class User(db.Model):
    __tablename__ = "user_table"
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    prophile_photo = db.Column(db.String)
    favorite_planet = relationship("Fav_Planet", backref="user")
    favorite_character = relationship("Fav_Planet", backref="user")

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "prophile_photo": self.prophile_photo
        }


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')