'''
urls dinâmicas
'''

from flask import Flask

app = Flask('__name__')

'''
no exemplo abaixo o serão aceitos os endpoints
1. /hello ou /hello/ - bidirecionamento
2. /hello/<nome>

OBS.: importante colocar a variavle nome como default vazio
'''
@app.route('/hello/')
@app.route('/hello/<nome>')
def hello(nome=''):
    return '<h1>ola {}<h1>'.format(nome)

@app.route('/blog/')
@app.route('/blog/<int:postID>')
def blog(postID = -1):
    if postID > 0:
        return 'Post info {}'.format(postID)
    else:
        return 'Post TODO'

if __name__ == '__main__':
    app.run()