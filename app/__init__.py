from flask import Flask
from app.utils.credentials import SECRET_KEY

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY

from app.controllers.room_controllers import *
from app.controllers.routers import *
from app.controllers.template_controllers import *
from app.authentication.authentication import *
from app.utils.auth import *
from app.utils.query import *
