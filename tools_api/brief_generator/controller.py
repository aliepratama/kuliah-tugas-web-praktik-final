from flask import request
from tools_api.helpers.db import supabase
from tools_api.helpers.res_message import SuccessMessage, ErrorMessage
from tools_api.helpers.bard import bardhelper
import tools_api.helpers.response as res


def check_before_service(func: any, user_id: int) -> any:
    response = supabase.table('bard_token').select('s_1psid, s_1pscc, s_1psts')\
                .order('created_at', desc=True).limit(1).single().execute()
    print('DATA>>>>>>>>>', response)
    if response.data:
        response = response.data
        bardhelper.initial_token(response['s_1psid'], response['s_1pscc'], response['s_1psts'])
        response = supabase.table('users').select('token').eq('id', user_id).execute()
        if len(response.data) > 0:
            token = response.data[0]['token']
            print('TOKEN>>>>>', token)
            if token > 0:
                try:
                    bard_response = func()
                    supabase.table('users').update({'token': token - 1}).eq('id', user_id).execute()
                    return res.ok([bard_response], SuccessMessage.SM5)
                except Exception as e:
                    print(e)
                    return res.server_error()
            return res.bad_request(ErrorMessage.EM10)
    return res.server_error()


def get_brief_logo(user_id: int) -> any:
    return check_before_service(bardhelper.ask_logo_brief, user_id)

def get_brief_website(user_id: int) -> any:
    return check_before_service(bardhelper.ask_website_brief, user_id)

def initialize_bard() -> None:
    s_1psid = request.json.get('id')
    s_1pscc = request.json.get('cc')
    s_1psts = request.json.get('ts')
    if all([s_1psid, s_1pscc, s_1psts]):
        response = supabase.table('bard_token').insert({
            's_1psid': s_1psid,
            's_1pscc': s_1pscc,
            's_1psts': s_1psts,
        }).execute()
        print('DATA>>>>>>>>>', response)
        if response.data:
            return res.success(SuccessMessage.SM5)
        return res.server_error()
    return res.bad_request(ErrorMessage.EM11)