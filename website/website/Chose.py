#encoding=utf-8
import jieba
import urllib
import urllib2
import os
import re
import cookielib

Number_list = ['0','1','2','3','4','5','6','7','8','9','”','“',':','.','！','。','%','’','‘']

def Judge_letter(s1):
	if re.match('^[0-9a-z]+$',s1):
		return False
	return True

def Judge_number(s1):
	for i in s1:
		if i not in Number_list:
			return True
	return False

def Judge_len(s1):
	if len(s1)<4:
		return False
	return True

# F = open('Temp1.txt','w')
def gao(s,F):
	Origin = map(str,s.split())
	for s1 in Origin:
		if(Judge_len(s1) and Judge_number(s1) and Judge_letter(s1)):
			# s1 = s1.encode('utf-8')
			F.write(s1)
			F.write('   ')
	return F
def Chose(f,F):
	f = f.read()
	return gao(f,F)