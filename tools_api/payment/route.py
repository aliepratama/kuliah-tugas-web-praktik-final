from flask import request
from tools_api.app_init import app
from tools_api.helpers.res_message import ErrorMessage
import tools_api.payment.controller as ctrl
import tools_api.helpers.response as res
import flask_jwt_extended as jwt


@app.route('/payment/create', methods=['POST'])
@jwt.jwt_required()
def create_payment():
    user_id = jwt.get_jwt_identity()
    if request.method == 'POST':
        return ctrl.create_payment(user_id)
    return res.bad_request([ErrorMessage.EM1])

@app.route('/payment/verify', methods=['POST'])
def verify_payment():
    if request.method == 'POST':
        return ctrl.verify_payment()
    return res.bad_request([ErrorMessage.EM1])

@app.route('/payment/check', methods=['POST'])
def check():
    if request.method == 'POST':
        return ctrl.check()
    return res.bad_request([ErrorMessage.EM1])
