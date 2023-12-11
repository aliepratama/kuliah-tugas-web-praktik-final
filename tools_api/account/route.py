from flask import request
from tools_api.app_init import app
from tools_api.helpers.res_message import ErrorMessage
import tools_api.account.controller as ctrl
import tools_api.helpers.response as res
import flask_jwt_extended as jwt

@app.route('/account', methods=['POST'])
def account_general():
    if request.method == 'POST':
        return ctrl.add_account()
    return res.bad_request([ErrorMessage.EM1])

@app.route('/account/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@jwt.jwt_required()
def account_details(id):
    current_user = jwt.get_jwt_identity()
    print('CURRENT USER>>>>>', current_user)
    if current_user == id:
        if request.method == 'GET':
            return ctrl.get_account_by_id(id)
        elif request.method == 'PATCH':
            return ctrl.edit_account(id)
        elif request.method == 'DELETE':
            return ctrl.delete_account(id)
        return res.bad_request([ErrorMessage.EM1])
    return res.bad_request([ErrorMessage.EM9])

@app.route('/auth/login', methods=['POST'])
def auth_login():
    if request.method == 'POST':
        return ctrl.login_account()
    return res.bad_request([ErrorMessage.EM1])

