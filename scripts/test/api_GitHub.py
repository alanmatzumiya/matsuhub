from __future__ import unicode_literals
import youtube_dl


f = open('signal.txt', 'r')
test = f.read()
signal = test

while test == signal:
    f = open('signal.txt', 'r')
    signal = f.read()

print(signal, type(signal))
ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([signal])
