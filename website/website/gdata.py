#encoding=utf-8
from Get_News_Word import Get_News_Word
import os

def get_data(begin_time, end_time, top_n):
    ret = Get_News_Word(begin_time, end_time, top_n)
    rstr = ''
    for (key, value) in ret.items():
        tmp = '{text:\"' + key.decode('gbk').encode('utf-8') + '\", weight: ' + value.decode('gbk').encode('utf-8') + '}, '
        rstr = rstr + tmp
    return rstr
