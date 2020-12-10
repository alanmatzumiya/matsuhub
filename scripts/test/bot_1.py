import subprocess

list_images = subprocess.getoutput('ls ./static/home/images/PARTYS').split('\n')
images = 'images:'
for j in range(len(list_images)):
    images += '\n  - ' + list_images[j]

f = open('images.yml', 'w')
f.write(images)
f.close()
