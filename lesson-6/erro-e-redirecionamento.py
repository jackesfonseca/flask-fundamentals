"""
erro e redirecionamento
"""

from flask import Flask, request, abort, redirect, url_for

app = Flask('__name__')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['pass'] == 'admin':
            redirect(url_for('sucesso'), code=302) # 302 - redirecionamento
        else:
            abort(401) # 401 - não autorizado
    else:
        abort(403) # 403 - proibido

if __name__ == '__main__':
    app.run()