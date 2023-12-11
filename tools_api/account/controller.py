from flask import request
from datetime import timedelta
from tools_api.helpers.db import supabase
from tools_api.helpers.res_message import ErrorMessage, SuccessMessage
from werkzeug.security import check_password_hash, generate_password_hash
import tools_api.helpers.response as res
import flask_jwt_extended as jwt

def add_account():
    email = request.form.get('email')
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    password = request.form.get('password')
    if all([email, first_name, password]):
        try:
            response = supabase.table('users').select('email').eq('email', email).execute()
            print('RESPONSE>>>>>>>', response)
            if len(response.data) > 0:
                return res.bad_request(ErrorMessage.EM5)
        except:
            pass
        try:
            response = supabase.table('users').insert([{
                        'email': email,
                        'first_name': first_name,
                        'last_name': last_name,
                        'password': generate_password_hash(password),
                    }]).execute()
            print('DATA>>>>>>', response.data[0])
            column = ['id', 'email', 'first_name', 'last_name']
            data = {}
            for i in column:
                data[i] = response.data[0][i]
            print('RESULT>>>>>>', data)
            return res.ok([data], SuccessMessage.SM1)
        except:
            return res.server_error()
    response_msg = []
    if email is None:
        response_msg.append(ErrorMessage.EM2)
    if first_name is None:
        response_msg.append(ErrorMessage.EM3)
    if password is None:
        response_msg.append(ErrorMessage.EM4)
    return res.bad_request(response_msg)

def get_id_by_account():
    pass
def get_account_by_id(id):
    pass
def login_account():
    email = request.form.get('email')
    password = request.form.get('password')
    if all([email, password]):
        try:
            response = supabase.table('users').select('*').eq('email', email).execute()
            print('RESPONSE>>>>>>>', response)
            if len(response.data) > 0:
                print('CHECK PWD>>>>>>>', check_password_hash(response.data[0]['password'], password))
                if check_password_hash(response.data[0]['password'], password):
                    column = ['id', 'email', 'first_name', 'last_name']
                    data = {}
                    for i in column:
                        data[i] = response.data[0][i]
                    expires = timedelta(days=1)
                    expires_refresh = timedelta(days=3)
                    data['access_token'] = jwt.create_access_token(response.data[0]['id'],
                                                                    fresh=True, expires_delta=expires)
                    data['refresh_token'] = jwt.create_refresh_token(response.data[0]['id'],
                                                                        expires_delta=expires_refresh)
                    return res.ok([data], SuccessMessage.SM2)
                return res.bad_request(ErrorMessage.EM7)
        except:
            pass
        return res.bad_request(ErrorMessage.EM6)
    response_msg = []
    if email is None:
        response_msg.append(ErrorMessage.EM2)
    if password is None:
        response_msg.append(ErrorMessage.EM4)
    return res.bad_request(response_msg)
            
def logout_account():
    pass
def edit_account(id):
    pass
def delete_account(id):
    pass
