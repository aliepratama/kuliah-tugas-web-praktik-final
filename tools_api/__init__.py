from tools_api.app_init import app
from tools_api.helpers.security import cors
import tools_api.account

if __name__ == '__main__':
    app.run(debug=True)
