from flask import request
from tools_api.app_init import app
from tools_api.helpers.res_message import ErrorMessage
import tools_api.design_rater.controller as ctrl
import tools_api.helpers.response as res
import flask_jwt_extended as jwt


@app.route('/rater', methods=['POST'])
@jwt.jwt_required()
def rater():
    user_id = jwt.get_jwt_identity()
    if request.method == 'POST':
        return ctrl.consult(user_id)
    return res.bad_request([ErrorMessage.EM1])
