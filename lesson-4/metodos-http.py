"""
Métodos HTTP
"""

from flask import Flask
from flask.globals import request
from json import dumps

app = Flask('__name__', static_folder='static')

@app.route('/login', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        #return dumps(request.form)
        request.form['nome']
    return 'OKK GET'

@app.route('/add2/', methods=['POST', 'GET'])
def add2():
    if request.method == 'POST':
        return '%s LOGOU usando POST' %request.form['nome']
    else:
        return '%s RELOGOU usando GET' %request.form['nome']

if __name__=='__main__':
    app.run(debug=True)