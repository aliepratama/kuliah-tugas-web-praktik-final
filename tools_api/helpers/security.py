from flask_cors import CORS
from tools_api.app_init import app

cors = CORS(app, resources={r"/account/*": {"origins": "*"}})
cors = CORS(app, resources={r"/auth/*": {"origins": "*"}})