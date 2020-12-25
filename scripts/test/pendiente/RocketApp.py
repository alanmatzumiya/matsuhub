class Rocket(Server):
    """Class to build api.

    """

    def __init__(self):
        super(Server, self).__init__()
        self.greetings = print('Hello!!! My name is RocketHub!!!')

    @app.route(sections['login'], methods=['GET', 'POST'])
    def login():
        error = None
        if request.method == 'POST':

            if utils.usercheck(request.form['username'], request.form['password']):
                global active_logging
                active_logging = True

                return redirect('home')

            else:
                error = 'Invalid Credentials. Please try again.'

        return render_template('login.html', error=error)

    @Flask.app.route(sections['base'], methods=['GET'])
    def base():

        if active_logging:
            return redirect('home')
        else:
            return redirect('login')

@app.route(sections['home'])
def home():
    if active_logging:

        return render_template("index.html", path_css=PATH_CSS, path_js=PATH_JS, path_fav=PATH_FAV)
    else:
        return redirect('login')

    def music(self):
        FILES = subprocess.getoutput('ls static/home/music').split("\n")
        r = randint(0, len(FILES))

        return Response(render_template('music.html', path_css=PATH['CSS'], path_js=PATH['JS'], path_fav=PATH['FAV'],
                                        play_now=FILES[r], files=FILES), 200)

    def images(self):
        FILES = subprocess.getoutput('ls static/home/music').split("\n")
        r = randint(0, len(FILES))

        return Response(render_template('music.html', path_css=PATH['CSS'], path_js=PATH['JS'], path_fav=PATH['FAV'],
                                        play_now=FILES[r], files=FILES), 200)



