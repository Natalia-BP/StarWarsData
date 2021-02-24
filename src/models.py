import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

# Tablas
# Tabla PLANETAS
class Planets(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)

# Tabla PLANETAS DETALLADOS
class PlanetsFocused(Base):
    __tablename__ = "planets_focused"
    id = Column(Integer, primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    name = Column(String)
    url = Column(String)
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
    planets = relationship("Planets")

# Tabla PERSONAJES
class Characters(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    child_charactersFocused = relationship("CharactersFocused")

#  Tabla PERSONAJES DETALLADOS
class CharactersFocused(Base):
    __tablename__ = "characters_focused"
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    name = Column(String)
    url = Column(String)
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
    characters = relationship("Characters")

# Tabla USUARIOS
class User(Base):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    prophile_photo = Column(String)

# Tabla FAVORITOS
class Favorites(Base):
    __tablename__ = "favorites_table"
    id = Column(Integer, primary_key=True) 
    id_Planets = Column(Integer, ForeignKey('planets.id'))
    id_People = Column(Integer, ForeignKey('characters.id'))
    id_Username = Column(Integer, ForeignKey('user_table.id'))
    planets = relationship("Planets")
    characters = relationship("Characters")
    user_table = relationship("User")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')