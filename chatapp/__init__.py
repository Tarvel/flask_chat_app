
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from .events import socketio
from . import routes




app = Flask(__name__)
app.config.from_object(Config)
    
    
app.app_context().push()

db = SQLAlchemy(app)

app.register_blueprint(routes.main)
socketio.init_app(app)

