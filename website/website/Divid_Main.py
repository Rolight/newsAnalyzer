#encoding=utf-8
import jieba
import urllib
import urllib2
import os
import re
import cookielib
from Divid_Chose import Divid_Chose
from Divid_Cnt import Divid_Cnt
import datetime
import sqlite3
import time


def CUT(f):
	s = jieba.cut_for_search(f)
	return ' '.join(s)

def gao(Time,Title):
	s = CUT(Title)
	s.encode('utf-8')
	SS = Divid_Chose(s)
	Time = str(Time)
	Divid_Cnt(SS,Time)