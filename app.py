from scripts import Server
from flask import Flask

app = Flask(__name__)
Server = Server.Server(app)
routes = Server.ROUTES

app.add_url_rule(routes['base'], 'base', Server.base, methods=['GET'])
app.add_url_rule(routes['login'], 'login', Server.login, methods=['GET', 'POST'])
app.add_url_rule(routes['home'], 'home', Server.home, methods=['GET', 'POST'])
app.add_url_rule('/404', '404', Server.error404)
app.add_url_rule(routes['music'], 'music', Server.music, methods=['GET', 'POST'])
app.add_url_rule(routes['images'], 'images', Server.images, methods=['GET', 'POST'])
app.add_url_rule(routes['documents'], 'documents', Server.documents)
app.add_url_rule('/ytDown/', 'ytDown', Server.ytDown, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(Server.HOST, Server.PORT, debug=True)
