import os
from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

# Inicializa o aplicativo Flask
app = Flask(__name__)

# Configurações do aplicativo
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy
db = SQLAlchemy(app)

# Habilita CORS
cors = CORS(app, resources={r"/*": {
    "origins": "*",
    "methods": ["GET", "POST", "PUT", "DELETE"],
    "allow_headers": ["Content-Type", "Authorization"],
    "expose_headers": ["Content-Length"],
    "supports_credentials": True
}})

# Configura a API com Flask-RESTX
api = Api(app, version='1.0', title='SWApi Favoritos', description='API para gerenciamento dos seus itens e personagens favoritos de Star Wars')

# Importa os controladores
from app.controllers import FavoritesController


@app.before_request
def initialize_database():
    db.create_all()
