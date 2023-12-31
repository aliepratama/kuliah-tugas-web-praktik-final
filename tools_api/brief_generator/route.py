from flask import request
from tools_api.app_init import app
from tools_api.helpers.res_message import ErrorMessage
import tools_api.brief_generator.controller as ctrl
import tools_api.helpers.response as res
import flask_jwt_extended as jwt


@app.route('/brief', methods=['POST'])
@jwt.jwt_required()
def brief():
    user_id = jwt.get_jwt_identity()
    if request.method == 'POST':
        get_data = request.get_json()
        print('GET DATA>>>>>>>>>>', get_data)
        if get_data['type'] == 'logo':
            return ctrl.get_brief_logo(user_id)
        elif get_data['type'] == 'website':
            return ctrl.get_brief_website(user_id)
    return res.bad_request([ErrorMessage.EM1])

@app.route('/brief/init', methods=['POST'])
def bard_init():
    if request.method == 'POST':
        return ctrl.initialize_bard()
    return res.bad_request([ErrorMessage.EM1])
