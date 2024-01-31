'''
redirecionamento de url
'''

from flask import Flask, redirect, url_for

app = Flask('_name__')

@app.route('/admin')
def admin():
    return '<h1>Admin<h1>'

@app.route('/guest/<name>')
def guest(name):
    return 'Ola guest <b>%s</b>' % name

@app.route('/user/')
@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', name=name))

if __name__=='__main__':
    app.run()