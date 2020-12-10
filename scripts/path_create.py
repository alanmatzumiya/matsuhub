import subprocess

def build_data(path, name):
    list_dirs = subprocess.getoutput('ls ../static/home' + path).split('\n')
    dirs = name + ':'
    for j in range(len(list_dirs)):
        dirs += '\n  - ' + list_dirs[j]

    f = open(name + '.yml', 'w')
    f.write(dirs)
    f.close()


path = '/images/doggys'
name = 'doggys'

yrs = ['2020', '2019']

for yr in yrs:
    build_data(path + '/' + yr, name + '_' + yr)
