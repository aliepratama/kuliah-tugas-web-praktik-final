from flask_jwt_extended import JWTManager
from tools_api.app_init import app
import os

app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
jwt = JWTManager(app)
