import os
from random import randint
from flask import render_template, request, redirect, url_for, Response
import yaml
from . import botDriver
from . import api_YouTube
from datetime import datetime


class Server:
    """Class to build Server for using api.

    """

    def __init__(self, app):
        config_path = './scripts/_config.yml' 
        config_file = open(config_path)
        config_dict = yaml.load(config_file, Loader=yaml.FullLoader)
        
        self.app = app
        self.SETTINGS = config_dict['SETTINGS']
        self.LIBS = config_dict['LIBS']
        self.IMAGES_PATH = config_dict['IMAGES-FILES']
        self.MUSIC_PATH = config_dict['MUSIC-FILES']
        self.DOCUMENTS_PATH = config_dict['DOCUMENTS-FILES']
        self.ROUTES = config_dict['ROUTES']

        self.active_logging = True
        self.HOST = self.SETTINGS['HOST']
        self.PORT = self.SETTINGS['PORT']

        self.timer = datetime
        self.family_path = self.IMAGES_PATH['family']
        self.doggys_path = self.IMAGES_PATH['doggys']
        self.partys_path = self.IMAGES_PATH['partys']
        datas_dir = [os.listdir(self.family_path), os.listdir(self.doggys_path), os.listdir(self.partys_path)]
        self.images_files = { 'family' : {}, 'doggys' : {}, 'partys' : {} }
        
        for j in range(len(datas_dir[0])): self.images_files['family'][datas_dir[0][j]] = os.listdir(self.family_path + '/' + datas_dir[0][j])
        for j in range(len(datas_dir[1])): self.images_files['doggys'][datas_dir[1][j]] = os.listdir(self.doggys_path + '/' + datas_dir[1][j])
        for j in range(len(datas_dir[2])): self.images_files['partys'][datas_dir[2][j]] = os.listdir(self.partys_path + '/' + datas_dir[2][j])
        
    def usercheck(self, ID, KEY):

        secrete_path = './scripts/DATABASE/secrets.yml'
        secrete_file = open(secrete_path)
        secrete_dict = yaml.load(secrete_file, Loader=yaml.FullLoader)

        if ID == secrete_dict['admin']['ID'] and KEY == secrete_dict['admin']['KEY']:
            return True
        elif ID in secrete_dict['main_users']['ID']:

            if KEY == secrete_dict['main_users']['KEY'][secrete_dict['main_users']['ID'].index(ID)]:
                return True
            else:
                return False
        else:
            return False
    
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

        os.system('mv *.mp4 ./static/home/music')

        return redirect(url_for('music'))
        
    def base(self):
        if self.active_logging:
            return redirect('home')
        else:
            return redirect('login')


    def login(self):
        error = None
        if request.method == 'POST':

            if self.usercheck(request.form['username'], request.form['password']):
                self.active_logging = True

                return redirect('home')

            else:
                error = 'Invalid Credentials. Please try again.'

        return Response(render_template('login.html', libs=self.LIBS, error=error), 200)


    def home(self):
        if self.active_logging:

            return Response(
                render_template("index.html", timer=self.timer, libs=self.LIBS,
                                routes=self.ROUTES, title='Home'), 200)
        else:
            return redirect('login')

    def music(self):

        music_files = os.listdir(self.MUSIC_PATH)
        if request.args.get('song_play') == None:
            song_play = music_files[randint(0, len(music_files)-1)]
        else:
            song_play = request.args.get("song_play")
        return Response(render_template('music.html', timer=self.timer, song_play=song_play,
                                        libs=self.path_back(self.LIBS), files_path='../' + self.MUSIC_PATH,
                                        files=music_files, routes=self.ROUTES, title='Music'), 200)

    def images(self):
        self.files = []

        for j in range(len(self.images_files['family']['2003'])):
            self.files.append('../' + self.family_path + '/2003/' + self.images_files['family']['2003'][j])
        for j in range(len(self.images_files['family']['2015'])):
            self.files.append('../' + self.family_path + '/2015/' + self.images_files['family']['2015'][j])
        for j in range(len(self.images_files['family']['2017'])):
            self.files.append('../' + self.family_path + '/2017/' + self.images_files['family']['2017'][j])
        for j in range(len(self.images_files['doggys']['2019'])):
            self.files.append('../' + self.doggys_path + '/2019/' + self.images_files['doggys']['2019'][j])
        for j in range(len(self.images_files['partys']['2018'])):
            self.files.append('../' + self.partys_path + '/2018/' + self.images_files['partys']['2018'][j])

        return Response(render_template('images.html',
                                        timer=self.timer, libs=self.path_back(self.LIBS),
                                        files_path=self.path_back(self.IMAGES_PATH), files=self.files,
                                        routes=self.ROUTES, title='Images'), 200)

    def documents(self):
        documents_files = os.listdir(self.DOCUMENTS_PATH)
        return Response(render_template("documents.html", timer=self.timer, libs=self.path_back(self.LIBS),
                                        files_path='../'+self.DOCUMENTS_PATH, files=documents_files,
                                        routes=self.ROUTES, title='Documents'), 200)
