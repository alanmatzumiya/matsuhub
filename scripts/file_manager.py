import os, subprocess


def hosting(host='127.0.0.1', port='8080'):
    
    config = ' --host=' + host + ' --port=' + port
    os.system('jekyll serve' + config)


def git_push(branch='master'):
    r = "pip freeze > requirements.txt"
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


def testing_backup():
    COPY_DIR = 'COPY_FILES'
    RM_FILE = 'NO_FILE'
	COPY_IMG = 'BACKUP_REAL/images'
	COPY_PDF = 'BACKUP_REAL/PDFs'
	COPY_MUSIC = 'BACKUP_REAL/music'
	DESTINATE = 'TEST'

	paths = subprocess.getoutput('ls ' + COPY_DIR).split('\n')
	d = 0
	subpaths = ['']
	while d < len(paths):
		PATH = COPY_DIR + '/' + paths[d] 
		t1 = subprocess.getoutput('find ' + PATH + ' | grep "\.m4a$"').split('\n')
		t2 = subprocess.getoutput('find ' + PATH + ' | grep "\.mp4$"').split('\n')
		t3 = subprocess.getoutput('find ' + PATH + ' | grep "\.pdf$"').split('\n')
		t4 = subprocess.getoutput('find ' + PATH + ' | grep "\.wma$"').split('\n')
		
		if t1 != [''] or t2 != [''] or t3 != [''] or t4 != ['']:
		    os.system('mv -n ' + PATH + ' ' + DESTINATE) 
		
		d +=1
	   

        
def test_filetype(tag='.pdf', DESTINATE=COPY_PDF):
    for j in subpaths:
        os.system('mv -n ' + NEW_PATH + j + ' ' + DESTINATE)
        if j.endswith(':'):
            print(j)
            NEW_PATH = j.replace(':', '/')
         
        else: 
            if j.endswith(tag) or j.endswith(tag.upper()):
                print(j)
                os.system('mv -n ' + NEW_PATH + j + ' ' + DESTINATE)




def clean_backup():
    for j in subpaths:
        PATH = COPY_DIR + '/' + j

        dirs = subprocess.getoutput('ls ' + PATH).split('\n')
        if dirs == []:
            subprocess.getoutput('mv ' + PATH + ' ' + RM_FILE)
        else:
            for j in dirs:
                try:
                    t = j[j.index('.'):]
                    fileTypes.append(t)
                except ValueError:
                    pass
    print(set(fileTypes))

def upper_filetype():
    for i in subpaths:
        NEW_PATH = COPY_DIR + '/' + i

        dirs = subprocess.getoutput('ls ' + NEW_PATH).split()
        for j in dirs:
            try:
                TEST = j
                
                if TEST.endswith('.JPEG') or TEST.endswith('.JPG') or TEST.endswith('.PNG'):
   
                    subprocess.getoutput('mv -n ' + NEW_PATH + '/' + j + ' ' + COPY_IMG)
            
                elif TEST.endswith('.PDF'):
    
                    subprocess.getoutput('mv -n ' + NEW_PATH + '/' + j + ' ' + COPY_PDF)
             
                else:
              
                    if TEST.endswith('.MP3') or TEST.endswith('.MP4'):

                        subprocess.getoutput('mv -n ' + NEW_PATH + '/' + j + ' ' + COPY_MUSIC)
               
            except ValueError:
                pass
               
                    
def lower_filetype():
    for i in subpaths:
        NEW_PATH = COPY_DIR + '/' + i

        dirs = subprocess.getoutput('ls ' + NEW_PATH).split()
        for j in dirs:
            try:
                TEST = j
                
                if TEST.endswith('.jpeg') or TEST.endswith('.jpg') or TEST.endswith('.png'):
   
                    subprocess.getoutput('mv -n ' + NEW_PATH + '/' + j + ' ' + COPY_IMG)
            
                elif TEST.endswith('.pdf'):
    
                    subprocess.getoutput('mv -n ' + NEW_PATH + '/' + j + ' ' + COPY_PDF)
             
                else:
              
                    if TEST.endswith('.mp3') or TEST.endswith('.mp4'):

                        subprocess.getoutput('mv -n ' + NEW_PATH + '/' + j + ' ' + COPY_MUSIC)
               
            except ValueError:
                pass
             

