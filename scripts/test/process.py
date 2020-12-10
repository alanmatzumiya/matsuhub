import os, subprocess

bots_dir = ['./scripts', './static', './templates', './downloads']
for j in range(0, len(bots_dir)):
    f = open(bots_dir[j] + '/bot.py', 'w')
    f.write('print("hello")')
    f.close()
    os.system('python3 ' + bots_dir[j] + '/bot.py')
