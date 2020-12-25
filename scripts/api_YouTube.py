from __future__ import unicode_literals
import youtube_dl
from time import sleep
import yaml

'''''
def worker():
    while True:
    workers_file = open('id_workers.yml')
    workers_dict = yaml.load(workers_file, Loader=yaml.FullLoader)

    sleep(1)
    test = workers_dict['youtube_download']
    signal = test
    while test == signal:
        workers_file = open('id_workers.yml')
        workers_dict = yaml.load(workers_file, Loader=yaml.FullLoader)
        signal = workers_dict['youtube_download']
    sleep(1)
    workers_file = open('id_workers.yml')
    workers_dict = yaml.load(workers_file, Loader=yaml.FullLoader)
    signal = workers_dict['youtube_download']

    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([signal])
'''''


def YouTubeDown(url):
    print(url)
    ydl_opts = {}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


