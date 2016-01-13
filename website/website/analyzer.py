#encoding=utf-8
import jieba
import urllib
import urllib2
import os
import re
import cookielib
from Chose import *
from Cnt import *
import datetime
import sqlite3

def CUT(f):
	s = jieba.cut_for_search(f)
	return ' '.join(s)


def gao(Day,Title,F2):
	F = 'T_Divid_' + Day +'.txt'
	F1 = 'T_Rm_Again_' + Day + '.txt'

	FF = open(F,'w')
	s = CUT(Title)
	s = s.encode('utf-8')
	FF.write(s)
	FF.close()

	f = open(F,'r')
	FF1 = open(F1,'a')
	f = Chose(f,FF1)
	f.close()
	FF1.close()


def nong(Begin,End):
	print Begin, End

	F2 = Begin +'to'+ End + '.txt'
	cx = sqlite3.connect('text.db')
	cx.text_factory = str
	cu = cx.cursor()
	Year_Begin = int(Begin[0:4])
	Month_Begin = int(Begin[6:7])
	Day_Begin = int(Begin[9:10])
	Begin_Day = datetime.date(Year_Begin,Month_Begin,Day_Begin)
	Year_End = int(End[0:4])
	Month_End = int(End[6:7])
	Day_End = int(End[9:10])
	End_Day = datetime.date(Year_End,Month_End,Day_End)
	while(Begin_Day<=End_Day):
		SS = str(Begin_Day)
		SSS = 'select * from Day where Accurate_time = \'%s\'' % SS
		cu.execute(SSS)
		T = cu.fetchall()
		for i in T:
			T_str = str(i[0])
			gao(SS,T_str,F2)
		Begin_Day += datetime.timedelta(days=1)
	F1 = 'T_Rm_Again_' + SS + '.txt'
	F = 'T_Divid_' + SS +'.txt'
	f = open(F1,'r')
	FF2 = open(F2,'a')
	Cnt(f,FF2)
	f.close()
	FF2.close()
	os.remove(F)
	os.remove(F1)
	cx.close()

# Path = os.getcwd()
# Path_list = os.listdir(Path)
# for i in Path_list:
# 	ii = os.path.join(Path,i)
# 	if os.path.isfile(ii):
# 		continue;
# 	gao(i)
