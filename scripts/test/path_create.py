import subprocess



def build_workers(id_worker='youtube_download', assignature='url'):
    workers = {'youtube_download' : 'wait', 'other' : 'wait'}
    workers[id_worker] = assignature
    worker_file = id_worker + ': ' + assignature + '\n'
    worker_file += 'other' + ': ' + workers['other']

    f = open('test.yml', 'w')
    f.write(worker_file)
    f.close()

build_workers()
