from flask import request
from tools_api.helpers.db import supabase
from tools_api.helpers.res_message import ErrorMessage, SuccessMessage
from werkzeug.security import check_password_hash, generate_password_hash
import tools_api.helpers.response as res

def add_account():
    email = request.form.get('email')
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    password = request.form.get('password')
    required = [email, first_name, password]
    if all(required):
        try:
            response = supabase.table('users').select('email').eq('email', email)
            print('RESPONSE>>>>>>>', response)
            if response.count > 0:
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
    pass
def logout_account():
    pass
def edit_account(id):
    pass
def delete_account(id):
    pass
