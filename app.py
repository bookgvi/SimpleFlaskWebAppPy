from flask import Flask
from flask import flash, request, session, render_template, make_response
import os
import http_statuses

app = Flask(__name__)
app.secret_key = os.urandom(256)


@app.route('/', methods=['GET'])
def main_page():
    if not session.get('logged_in'):
        return render_template('./login.html')
    else:
        return render_template('./hello.html')


@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] == 'asd' and request.form['password'] == 'asd':
        session['logged_in'] = True
    else:
        flash(u'Incorrect authentication', 'error')
    return main_page()


@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    return main_page()


@app.route('/hello/<user>', methods=['GET'])
def hello(user):
    response = app.make_response('<h1>Hello, %s</h1>' % user)
    response.status_code = http_statuses.NOT_AUTHORITATIVE
    response.set_cookie('authorization', '666')
    response.headers['Authorization'] = 'Bearer %s' % os.urandom(512)
    return response


if __name__ == '__main__':
    app.run(debug=True)
