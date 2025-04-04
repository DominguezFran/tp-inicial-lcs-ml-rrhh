import os

#Especifico la ruta donde se guardara el archivo de la base de datos
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../data/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False