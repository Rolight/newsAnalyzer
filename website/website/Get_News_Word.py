#encoding=utf-8
import jieba
import urllib
import urllib2
import os
import re
import cookielib
import sqlite3
from datetime import date


def Get_News_Word(Begin,End, top_n):
	cx_word = sqlite3.connect('Word.db')
	cx_word.text_factory = str
	cu_word = cx_word.cursor()
	s = 'select Word,sum(Freq) from Day  where Time >=\'%s\' and Time <=\'%s\' group by Word order by sum(Freq) desc ' % (Begin,End)
	cu_word.execute(s);
	cnt = 1;
	ret = {}
	while(1):
		i = cu_word.fetchone()
		if cnt > top_n:
			break
		ret[str(i[0])] = str(i[1])
		cnt += 1
	return ret
