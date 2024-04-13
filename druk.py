from flask import Flask, session, render_template, redirect, request, url_for
from datetime import date
import requests
import json
import jwt
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'NEWsupersecretkey111'  # os.urandom(24)

server1 = 'https://api.druk.ua'
server2 = 'https://api.stage.druk.ua'


def generate_token(data):
    secret_key = app.config['SECRET_KEY']
    token = jwt.encode(data, secret_key, algorithm='HS256')
    return token.decode('utf-8')


def decode_token(token):
    secret_key = app.config['SECRET_KEY']
    try:
        data = jwt.decode(token, secret_key, algorithms=['HS256'])
        return data
    except jwt.ExpiredSignatureError:
        return None


def login(mail, pswd):
    session.clear()
    server = request.form.get('server')  # Получить выбранный сервер из запроса
    if server == 'test':
        domain = server2
    else:
        domain = server1

    session['domain'] = domain

    payload = {
        'email': mail,
        'password': pswd
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en",
        "Cache-Control": "no-cache",
        "Currency-Code": "UAH",
        "Pragma": "no-cache",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"
    }
    res = requests.post(f'{domain}/api/employees/auth/login', json=payload)
    if res.status_code == 200:
        token = json.loads(res.content)['token']
        session['token'] = token
        session['typographyid'] = \
        json.loads(res.content)['employee']['typography']['id']
        session['typographyname'] = \
        json.loads(res.content)['employee']['typography']['title']
        headers.update({'Authorization': 'Bearer ' + token})
        session['headers'] = headers
        if json.loads(res.content)['employee']['avatar']:
            session['avatar'] = json.loads(res.content)['employee']['avatar']
        session['avatarname'] = json.loads(res.content)['employee']['name']
        session['worker_id'] = json.loads(res.content)['employee']['id']
        session['production-statuses'] = getproductionstatuses()
        filterreset()
        return True
    else:
        session['loginerror'] = res.content.decode('utf-8')[28:-2]
        return False


@app.route('/')
def job_list():
    if 'job_materials' in session: clearspend()
    if 'token' not in session or 'typographyid' not in session:  # Если не авторизован - перенаправляем на страницу авторизации
        return redirect(url_for('auth'))
    if 'printer' not in session:
        return redirect(url_for('printer_select'))
    joblist = getlist()
    if 'savestatus' in session:
        message = session['savestatus']
        session.pop('savestatus', None)
        return render_template('job_list.html', joblist=joblist,
                               message=message)
    else:
        return render_template('job_list.html', joblist=joblist)


@app.route('/printer_select', methods=['GET', 'POST'])
def printer_select():
    if 'headers' not in session:
        return redirect(url_for('auth'))
    headers = session.get('headers')
    domain = session.get('domain')
    typographyid = session.get('typographyid')
    url = f'{domain}/api/typographies/{typographyid}/equipments'
    printerlist = requests.get(url, headers=headers).json()
    konicalist = []


    for printer in printerlist['list']:
        id = printer['id']
        title = printer['title']
        if "konica" in title or "Konica" in title:
            konicalist.append({"title": title, "id": id})
    if request.method == 'POST':
        session['printer'] = request.form['printer']
        return render_template('login.html')
    return render_template('PrinterIndex.html', printerlist=konicalist)


@app.route('/printerfilter', methods=['GET', 'POST'])
def printerfilter():
    if request.method == 'POST':
        printer = request.form['printer']
        session['printer'] = printer
        session['equipment_input'] = printer
    return redirect(url_for('job_list'))


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        mail = request.form['email']
        password = request.form['password']
        if login(mail, password):
            return redirect(url_for('job_list'))
        else:
            error = 'Error: ' + session['loginerror']
            session.pop('loginerror', None)
            return render_template('login.html', error=error)
    return render_template('login.html')


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('token', None)
    return redirect(url_for('auth'))


if name == '__main__':
    app.run(debug=True)
