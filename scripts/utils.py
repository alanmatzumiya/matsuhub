import os
import subprocess
import yaml
from pytube import YouTube, Playlist
from pytube.exceptions import RegexMatchError

def server_setup():
  
    config_path = './scripts/_config.yml' 

    config_file = open(config_path)
    config_dict = yaml.load(config_file, Loader=yaml.FullLoader)

    settings = config_dict['settings']
    sections = config_dict['sections']

    return settings, sections
    
def usercheck(ID, KEY):
  
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

def hosting(host='127.0.0.1', port='8080'):
    DIRS = subprocess.getoutput('ls')
    subprocess.getoutput('ls -d */')

    config = ' --host=' + host + ' --port=' + port
    os.system('jekyll serve' + config)


def git_push(branch='master'):

    os.system('git init')
    FILES = subprocess.getoutput('ls').split()
    FILES.remove('_site')
    for FILE in FILES:
        os.system('git add ' + FILE)
        
    os.system('git commit -m ' + '"automatic"')
    os.system('git remote add origin ' + branch)
    os.system('git push origin ' + branch)
    
    os.system(USERNAME)
    os.system(PASSWORD)

def save_file(file, file_name):
    with open(file_name, 'w') as f:
        # f.write(json.loads(response))
        json.dump(file, f, indent=4, sort_keys=True, ensure_ascii=True)

def write_file(file_name=None):
    f = open("index.html", "r")
    sty1 = open("static/css/normalize.css", "r")
    sty2 = open("static/css/skeleton.css", "r")
    normal = BeautifulSoup(sty1, 'html.parser').prettify()
    skel = BeautifulSoup(sty2, 'html.parser').prettify()
    html = BeautifulSoup(f, 'html.parser')
    html.find(id="normalize").string.replace_with(normal)
    html.find(id="skeleton").string.replace_with(skel)
    f.close()
    sty1.close()
    sty2.close()
    #f = open("test2.html", "w")
    #f.write(g.prettify())
    #f.close()
    return html.prettify()


def pyTube():
    urls = Playlist('https://www.youtube.com/watch?v=J1ue6MjfTJ0&list=PL8CEFD80260364769')
    i = 49
    for j in range(i, len(urls)):
        print(j)
        try:
            YouTube(urls[j]).streams.first().download()
        except RegexMatchError:
            continue