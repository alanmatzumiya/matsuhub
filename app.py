from scripts import Server
from flask import Flask, request, redirect, url_for, render_template
import yaml
import subprocess

Server = Server.Server()
routes = Server.ROUTES
app = Flask(__name__)

app.add_url_rule(routes['base'], 'base', Server.base, methods=['GET'])
app.add_url_rule(routes['login'], 'login', Server.login, methods=['GET', 'POST'])
app.add_url_rule(routes['home'], 'home', Server.home)
app.add_url_rule(routes['apps'], 'apps', Server.apps)
app.add_url_rule(routes['music'], 'music', Server.music)
app.add_url_rule(routes['images']['root'], 'images', Server.images)
app.add_url_rule(routes['documents'], 'documents', Server.documents)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html', libs=Server.LIBS), 404

@app.route('/youtube_downloads/', methods=['GET'])
def downloads():

    url = request.args.get("url")
    #workers_path = './scripts/id_workers.yml'
    #workers_file = open(workers_path)
    #workers_dict = yaml.load(workers_file, Loader=yaml.FullLoader)
    workers = {'youtube_download': 'wait', 'other': 'wait'}
    workers['youtube_download'] = url
    worker_file = 'youtube_download: ' + workers['youtube_download'] + '\n'
    worker_file += 'other: ' + workers['other']

    f = open('./scripts/id_workers.yml', 'w')
    f.write(worker_file)
    f.close()

    return redirect(url_for('music'))


if __name__ == '__main__':
    app.run(Server.HOST, Server.PORT, debug=False)
