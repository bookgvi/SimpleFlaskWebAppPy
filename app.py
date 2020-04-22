from flask import Flask
from flask import flash, request, session, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main_page():
    if not session.get('logged_in'):
        return render_template('./login.html')
    else:
        return render_template('./hello.html')


@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] == 'admin' and request.form['password'] == 'pa$$w0rD':
        session['logged_in'] = True
    else:
        flash('Incorrect authentication')
        return main_page()


@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    return main_page()


if __name__ == '__main__':
    app.run()
