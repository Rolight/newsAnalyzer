from website.analyzer import nong
import os

def get_data(begin_time, end_time, top_n):
    nong(begin_time, end_time)
    filename = begin_time + 'to' + end_time + '.txt'
    filepath = os.path.join(os.path.dirname(__file__), filename).replace('\\', '/')
    fp = open(filepath)
    fstr = fp.read().split('\n')
    dt = {}
    rstr = ''
    for i in fstr:
        now = i.split(' ')
        tmp = '{text:\"' + i[0] + '\", weight: ' + i[1] + '}, '
        rstr = rstr + tmp
    return rstr
