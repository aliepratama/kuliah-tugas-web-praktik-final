from flask import Flask, render_template, request, redirect
from bardapi import Bard
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import requests, os, replicate


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
    
if __name__ == '__main__':
    app.run(debug=True)
    