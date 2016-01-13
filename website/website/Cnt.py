#encoding=utf-8
import jieba
import urllib
import urllib2
import os
import re
import cookielib
L = {}
D = set()
Screen_Table = ['中国','男子','女子','今年','明年','发生','价格','调查','问题','事故','国家','巴基','巴基斯','现场','已致','导致','万元','亿元','视屏']

for i in Screen_Table:
	if i not in D:
		D.add(i)
		# print i

def Cnt(f,F):
	f = f.read()
	f = map(str,f.split())
	for i in f:
		if i in D:
			continue
		if  i not in L:
			L[i] = 1;
		else:
			L[i] += 1
	T = sorted(L.iteritems(), key=lambda d:d[1], reverse = True )
	for i in T:
		s = str(i[0])+' '+str(i[1])
		F.write(s)
		F.write('\n')
