from tools_api.app_init import app
from tools_api.helpers.security import cors
from tools_api.helpers.jwt import jwt
import tools_api.account
import tools_api.brief_generator

if __name__ == '__main__':
    app.run(debug=True)
