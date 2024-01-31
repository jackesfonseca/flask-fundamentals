'''
criando rotas usando rules
'''

from flask import Flask

app = Flask(__name__)

def teste():
    return '<p>Testando 1</p>'

app.add_url_rule('/teste', 'teste', teste)

if __name__ == '__main__':
    app.run()