from flask import request
from tools_api.helpers.db import supabase
from tools_api.helpers.res_message import SuccessMessage, ErrorMessage
import tools_api.helpers.response as res
from tools_api.payment.config import PaymentConfig as cfg
import requests, time, hmac, hashlib, json

def check():
    response = supabase.table('plans').select('*').eq('id', 1).execute()
    print('RES>>>>>>>', response.data)
    return res.ok(response.data, 'cek')

def create_payment(user_id):
    plan_id = request.form.get('plan_id')
    if plan_id:
        count_trx = supabase.table('transactions').select('*', count='exact').execute()
        print('TRX>>>>>>>', count_trx.count)
        data_plan = supabase.table('plans').select('*').eq('id', plan_id).execute()
        print('PLAN>>>>>>>', data_plan)
        data_user = supabase.table('users').select('*').eq('id', user_id).execute()
        print('USER>>>>>>>', data_plan)
        if len(data_plan.data) == 0 and len(data_user.data) == 0:
            return res.bad_request(ErrorMessage.EM12)
        data_plan = data_plan.data[0]
        data_user = data_user.data[0]
        try:
            apiKey     = cfg.API_KEY
            privateKey = cfg.PRVT_KEY

            merchant_code = cfg.MERCH_CODE
            merchant_ref  = f"INV{str(count_trx.count).zfill(5)}"
            amount        = data_plan['price']

            expiry = int(time.time() + (24*60*60))

            signStr = "{}{}{}".format(merchant_code, merchant_ref, amount)
            signature = hmac.new(bytes(privateKey,'latin-1'), bytes(signStr,'latin-1'), hashlib.sha256).hexdigest()

            payload = {
                'method': 'QRIS2',
                'merchant_ref': merchant_ref,
                'amount': amount,
                'customer_name': f"{data_user['first_name']}",
                'customer_email': data_user['email'],
                'customer_phone': '081234567890',
                'return_url': 'https://domainanda.com/redirect',
                'expired_time': expiry,
                'signature': signature
            }

            order_items = [
                {
                'sku': data_plan['plan_code'],
                'name': data_plan['name'],
                'price': data_plan['price'],
                'quantity': 1,
                },
            ]

            i = 0
            for item in order_items:
                for k in item:
                    payload['order_items['+ str(i) +']['+ str(k) +']'] = item[k]
                i += 1

            print('PAYLOAD>>>', payload)
            headers = { "Authorization": "Bearer " + apiKey }

            result = requests.post(url="https://tripay.co.id/api-sandbox/transaction/create", data=payload, headers=headers)
            print('RAW_PAYMENT>>>>>', result.text)
            response = json.loads(result.text)
            response = response['data']
            print('PAYMENT>>>>>', response)
            res_trx = supabase.table('transactions').insert({
                'user_id': user_id,
                'plan_id': plan_id,
                'total_price': amount,
                'referral': response['reference'],
                'status': response['status'],
                'qr_url': response['qr_url']
            }).execute()
            print('RES_TRX>>>>>>>', res_trx)
            return res.ok(res_trx.data, SuccessMessage.SM5)
        except Exception as e:
            return res.server_error()

def verify_payment():
    ref_trx = request.json.get('reference')
    print('REQ>>>>>>', ref_trx)
    if ref_trx:
        try:
            res_trx = supabase.table('transactions').update({
                    'status': 'PAID'
                }).eq('referral', ref_trx).execute()
            print('RES_TRX>>>>>>>', res_trx)
            get_id = supabase.table('transactions').select('user_id, plan_id') \
                        .eq('referral', ref_trx).execute()
            print('GET ID>>>>>>>', get_id)
            res_token = supabase.table('plans').select('token') \
                        .eq('id', get_id.data[0]['plan_id']).execute()
            print('RES TOKEN>>>>>>>', res_token)
            res_user_token = supabase.table('users').select('token') \
                        .eq('id', get_id.data[0]['user_id']).execute()
            print('RES USER TOKEN>>>>>>>', res_user_token)
            res_topup = supabase.table('users').update({
                    'token': res_user_token.data[0]['token'] + res_token.data[0]['token']
                }).eq('id', get_id.data[0]['user_id']).execute()
            print('RES TOPUP>>>>>>>', res_topup)
            return res.ok(res_trx.data, SuccessMessage.SM5)
        except:
            pass
    return res.server_error()
