import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# Tabla PLANETAS
class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    description = Column(String)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String)
    population = Column(Integer)
    climate = Column(String)
    terrain = Column(String)
    surface_water = Column(Integer)
    created = Column(Date)
    edited = Column(Date)
    photo = Column(String)
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
class Characters(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    description = Column(String)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(Date)
    gender = Column(String)
    created = Column(Date)
    edited = Column(Date)
    photo = Column(String)
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
class Fav_Planet(Base):
    __tablename__ = "fav_planet"
    id_FavPlanets = Column(Integer, primary_key=True)
    id_Planets = Column(Integer, ForeignKey("planet.id"))
    id_Username = Column(Integer, ForeignKey("user_table.uid"))

    def serialize(self):
        return {
            "id_FavPlanets": self.id_FavPlanets,
            "id_Planets": self.id_Planets,
            "id_Username": self.id_Username
        }

#Tabla FAVORITOS PERSONAJES
class Fav_Character(Base):
    __tablename__ = "fav_character"
    id_FavCharacters = Column(Integer, primary_key=True)
    id_Character = Column(Integer, ForeignKey("characters.id"))
    id_Username = Column(Integer, ForeignKey("user_table.uid"))

    def serialize(self):
        return {
            "id_FavCharacters": self.id_FavCharacters,
            "id_Characters": self.id_Characterss,
            "id_Username": self.id_Username
        }

# Tabla USUARIOS
class User(Base):
    __tablename__ = "user_table"
    uid = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    prophile_photo = Column(String)
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