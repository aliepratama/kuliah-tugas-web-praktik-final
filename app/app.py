from flask import Flask, render_template, request, redirect
from bardapi import Bard
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from supabase import create_client, Client
import requests, os, replicate, urllib.parse, time, hmac, hashlib

load_dotenv()
# print('TOKEN>>>>>>>>>>>', os.environ['TOKEN_BARD_1PSID'])

app = Flask(__name__)
app.config['UPLOAD'] = os.path.join(app.root_path, 'static', 'uploads')

session_bard = requests.Session()
session_bard.cookies.set('__Secure-1PSID', os.environ['TOKEN_BARD_1PSID'])
session_bard.cookies.set('__Secure-1PSIDCC', os.environ['TOKEN_BARD_1PSIDCC'])
session_bard.cookies.set('__Secure-1PSIDTS', os.environ['TOKEN_BARD_1PSIDTS'])
session_bard.headers = {
    "Host": "bard.google.com",
    "X-Same-Domain": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Origin": "https://bard.google.com",
    "Referer": "https://bard.google.com/",
}

url: str = os.environ['SUPABASE_URL']
key: str = os.environ['SUPABASE_KEY']
supabase: Client = create_client(url, key)

@app.route('/')
def index():
    return redirect('/ai')

@app.route('/ai', methods=["POST", "GET"])
def ai():
    if request.method == 'POST':
        inputted_form = request.form['prompt']
        bard_helper = Bard(token=os.environ['TOKEN_BARD_1PSID'], session=session_bard)
        result = bard_helper.get_answer(inputted_form)['content']
        return render_template('index.html', inputted=inputted_form, result=result)
    return render_template('index.html', inputted='', result='')

@app.route('/imgbb', methods=["POST", "GET"])
def imgbb():
    if request.method == 'POST':
        file = request.files['image']
        filename = secure_filename(file.filename)
        img = os.path.join(app.config['UPLOAD'], filename)
        file.save(img)
        response_link = requests.post(url=f'https://api.imgbb.com/1/upload?expiration=15552000&key={os.environ["IMGBB_API_KEY"]}',
                                      files=[
                                    ('image',(filename, open(img,'rb'),file.mimetype))
                                    ])
        os.remove(img)
        return render_template('imgbb.html', result=response_link.json())
    return render_template('imgbb.html', result='')

@app.route('/consult', methods=["POST", "GET"])
def consult():
    if request.method == 'POST':
        prompt = request.form['prompt']
        file = request.files['image']
        filename = secure_filename(file.filename)
        img = os.path.join(app.config['UPLOAD'], filename)
        file.save(img)
        response_link = requests.post(url=f'https://api.imgbb.com/1/upload?expiration=15552000&key={os.environ["IMGBB_API_KEY"]}',
                                      files=[
                                    ('image',(filename, open(img,'rb'),file.mimetype))
                                    ])
        os.remove(img)
        output = replicate.run(
            "cjwbw/internlm-xcomposer:d16df299dbe3454023fcb47ed48dbff052e9b7cdf2837707adff3581edd11e95",
            input={
                "text": prompt,
                "image": response_link.json()['data']['url']
            }
        )
        return render_template('consult.html', inputted=prompt, result=output)
    return render_template('consult.html',inputted='', result='')

@app.route('/search', methods=["POST", "GET"])
def search():
    if request.method == 'POST':
        search_key = request.form['search']
        response = requests.get(url='https://www.googleapis.com/customsearch/v1',
                                params={
                                    'key': os.environ['GOOGLE_API_KEY'],
                                    'cx': os.environ['GOOGLE_CX_KEY'],
                                    'q': urllib.parse.quote(search_key),
                                })
        print('REQUEST>>>>>>>>>>', response.url)
        return render_template('search.html', inputted=search_key, result=response.json())
    return render_template('search.html',inputted='', result='')

@app.route('/pay', methods=["POST", "GET"])
def pay():
    if request.method == 'POST':
        try:
            api_key     = os.environ['TRIPAY_KEY']
            private_key = os.environ['TRIPAY_PRIVATE_KEY']

            merchant_code = "T26785"
            merchant_ref = ''
            amount        = 1000

            expiry = int(time.time() + (1*60*60)) # 1 jam

            signStr = "{}{}{}".format(merchant_code, merchant_ref, amount)
            signature = hmac.new(bytes(private_key,'latin-1'), bytes(signStr,'latin-1'), hashlib.sha256).hexdigest()

            payload = {
                'method': 'QRIS',
                'merchant_ref': merchant_ref,
                'amount': amount,
                'customer_name': 'Nama Pelanggan',
                'customer_email': 'emailpelanggan@domain.com',
                'customer_phone': '081234567890',
                'expired_time': expiry,
                'signature': signature
            }


            headers = { "Authorization": "Bearer " + api_key }

            result = requests.post(url="https://tripay.co.id/api/transaction/create", data=payload, headers=headers)
            response_pay = result.text
            print(response_pay)
            return render_template('payment.html', hasil=response_pay)
        except Exception as e:
            print("Request Error: " + str(e))
    # params = request.args.get('v')
    return render_template('payment.html', hasil='')

@app.route('/db_test')
def db_test():
    plan_result = supabase.table('plan').select('*').execute()
    users_result = supabase.table('users').select('*').execute()
    return render_template('db_test.html', plan=plan_result, user=users_result)
    
if __name__ == '__main__':
    app.run(debug=True)
    