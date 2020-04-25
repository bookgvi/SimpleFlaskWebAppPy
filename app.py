from flask import Flask
from flask import flash, request, session, render_template, abort
import os
import http_statuses

app = Flask(__name__)
app.secret_key = os.urandom(256)


@app.before_request
def has_session():
    if request.path != '/login':
        if not session.get('logged_in'):
            response = app.make_response(render_template('./login.html'))
            response.status_code = http_statuses.FORBIDDEN
            return response


@app.route('/', methods=['GET'])
def main_page():
    return render_template('./hello.html')


@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] == 'asd' and request.form['password'] == 'asd':
        session['logged_in'] = True
    else:
        flash(u'Incorrect authentication', 'error')
        abort(http_statuses.BAD_REQUEST)
    return main_page()


@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    return render_template('./login.html')


@app.route('/hello/<user>', methods=['GET'])
def hello(user):
    response = app.make_response('<h1>Hello, %s</h1>' % user)
    response.status_code = http_statuses.NOT_AUTHORITATIVE
    response.set_cookie('authorization', '666')
    return response


if __name__ == '__main__':
    app.run(debug=True)
