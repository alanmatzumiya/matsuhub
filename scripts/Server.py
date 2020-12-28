from flask import render_template, request, redirect, url_for, Response
import yaml
from . import botDriver
from . import api_YouTube
from datetime import datetime


class Server:
    """Class to build Server for using api.

    """

    def __init__(self, app):

        config_dict = yaml.load(open('./scripts/_config.yml'), Loader=yaml.FullLoader)

        self.files = []
        self.files.extend(list(yaml.load(open('./scripts/DATABASE/images.yml'), Loader=yaml.FullLoader).values()))
        self.music_dict = yaml.load(open('./scripts/DATABASE/music.yml'), Loader=yaml.FullLoader)

        self.app = app
        self.SETTINGS = config_dict['SETTINGS']
        self.LIBS = config_dict['LIBS']
        self.ROUTES = config_dict['ROUTES']

        self.HOST = self.SETTINGS['HOST']
        self.PORT = self.SETTINGS['PORT']
        self.timer = datetime
    
    def error404(self):

        return Response(render_template('404.html', libs=self.LIBS), 404)
        
    @staticmethod
    def path_back(libs):

        names = list(libs.keys())
        for name in names:
            libs[name] = '../' + libs[name]
        return libs
        
    def ytDown(self):

        song = request.args.get("song")
        url = botDriver.driverTube(str(song))
        api_YouTube.YouTubeDown(url)

        return redirect(url_for('music', song_play="The Dø - Anita No! (Live on KEXP)-Cv8EsAajC70.mp4"))
        
    def base(self):

            return redirect('home')

    def home(self):

            return Response(render_template("index.html", timer=self.timer, libs=self.LIBS,
                                routes=self.ROUTES, title='Home'), 200)

    def music(self):

        if request.args.get('song_play') == None:
            song_play = "The Dø - Anita No! (Live on KEXP)-Cv8EsAajC70.mp4"
        else:
            song_play = request.args.get("song_play")
        return Response(render_template('music.html', timer=self.timer, song_play=song_play,
                                        libs=self.path_back(self.LIBS), files_dict=self.music_dict,
                                        files=list(self.music_dict.keys()), routes=self.ROUTES, title='Music'), 200)

    def images(self):

        return Response(render_template('images.html',
                                        timer=self.timer, libs=self.path_back(self.LIBS), files=self.files,
                                        routes=self.ROUTES, title='Gallery'), 200)

    def documents(self):

        return Response(render_template("documents.html", timer=self.timer, libs=self.path_back(self.LIBS),
                                        routes=self.ROUTES, title='Documents'), 200)
