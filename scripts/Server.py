import subprocess
import os
import json
from random import randint
from flask import render_template, request, jsonify, redirect, url_for, Response
from werkzeug.utils import secure_filename
import yaml


class Server:
    """Class to build Server for using api.

    """

    def __init__(self):
        config_path = './scripts/_config.yml' 
        config_file = open(config_path)
        config_dict = yaml.load(config_file, Loader=yaml.FullLoader)

        self.SETTINGS = config_dict['SETTINGS']
        self.SERVICES = config_dict['SERVICES']
        self.LIBS = config_dict['LIBS']
        self.ROUTES = config_dict['ROUTES']

        self.active_logging = False

        self.HOST = self.SETTINGS['HOST']
        self.PORT = self.SETTINGS['PORT']

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
                render_template("index.html", libs=self.LIBS, routes=self.ROUTES, title='Home'), 200)
        else:
            return redirect('login')

    def apps(self):


        return Response(render_template("apps.html", libs=self.LIBS, routes=self.ROUTES, title='Apps'), 200)

    def music(self):
        music_list_path = './scripts/DATABASE/music.yml'
        music_file = open(music_list_path)
        music_dict = yaml.load(music_file, Loader=yaml.FullLoader)

        self.VIDEO_LIST = music_dict['music']
        LIBS = {'css': '../' + self.LIBS['css'], 'js': '../' + self.LIBS['js'], 'img': '../' + self.LIBS['img']}

        return Response(render_template('music.html', libs=LIBS, routes=self.ROUTES, files=self.VIDEO_LIST, title='Music'), 200)

    def images(self):

        images_list_path = './scripts/DATABASE/images.yml'
        images_file = open(images_list_path)
        self.IMAGES_LIST = yaml.load(images_file, Loader=yaml.FullLoader)

        LIBS = {'css': '../' + self.LIBS['css'], 'js': '../' + self.LIBS['js'], 'img': '../' + self.LIBS['img']}

        return Response(render_template('images.html', libs=LIBS, files=self.IMAGES_LIST, routes=self.ROUTES, title='Images'), 200)


    def documents(self):
        docs_list_path = './scripts/DATABASE/documents.yml'
        docs_file = open(docs_list_path)
        self.DOCS_LIST = yaml.load(docs_file, Loader=yaml.FullLoader)

        LIBS = {'css': '../' + self.LIBS['css'], 'js': '../' + self.LIBS['js'], 'img': '../' + self.LIBS['img']}
        return Response(render_template("documents.html", libs=LIBS, files=self.DOCS_LIST, routes=self.ROUTES, title='Documents'), 200)

    def app_service(self, service):

         if service == "upload":
            if request.method == 'POST':
                # obtenemos el archivo del input "archivo"
                f = request.files['archivo']
                filename = secure_filename(f.filename)
                # Guardamos el archivo en el directorio "Archivos PDF"
                f.save(os.path.join(self.settings['UPLOADS_FOLDER'], filename))
            # Retornamos una respuesta satisfactoria
            return redirect(url_for('home'))

         elif service == "response":
         # Retrieve the name from url parameter
            dict_script = request.args.get("code")

            response = {}

            # Check if user sent a name at all
            if not dict_script:
                response["ERROR"] = "no name found, please send a script."
            # Check if the user entered a number not a name
            elif str(dict_script).isdigit():
                response["ERROR"] = "code can't be numeric."
            # Now the user entered a valid name
            else:
                response["result"] = dict_script
                file_name = self.settings['SCRIPTS_FOLDER'] + "/result.json"
                #self.save_file(response, file_name)
            # Return the response in json format
            return redirect(url_for('index'))
