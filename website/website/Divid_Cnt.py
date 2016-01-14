#encoding=utf-8
import jieba
import urllib
import urllib2
import os
import re
import cookielib
import sqlite3
from datetime import date

cx_word = sqlite3.connect('Word.db')
cx_word.text_factory = str
cu_word = cx_word.cursor()
# cu_word.execute("create table Day(Time date ,Word char(20),Freq int,primary key (Time,Word,Freq))")
# cu_word.execute("create index Word_index on Day(Word)")
L = {}
D = set()
Screen_Table = open('Screen_Table.txt','r')
Screen_Table = Screen_Table.read()
# Screen_Table=Screen_Table.encode('utf-8')
Screen_Table = Screen_Table.split()
for i in Screen_Table:
	if i not in D:
		D.add(i)
def Divid_Cnt(f,Begin):
	f = map(str,f.split())
	for i in f:
		if i in D:
			continue
		if  i not in L:
			L[i] = 1;
		else:
			L[i] += 1
	T = sorted(L.iteritems(), key=lambda d:d[1], reverse = True )
	Sum = 0;
	for i in T:
		if Sum>50:
			break;
		s = str(i[0])+' '+str(i[1])
		Tup = (Begin,str(i[0]),int(i[1]))
		try:
			try:
				cu_word.execute("insert into Day values (?,?,?)",Tup)
				Sum += 1
			except:
				pass
		except:
			pass
	cx_word.commit()

		# F.write(s)
		# F.write('\n')