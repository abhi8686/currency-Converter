import urllib
import json
import datetime
import re

data={}
class Display(object):
	def show(self):
		global data
		i=1
		for x in data['rates']:
			print i,':', x 
			i+=1
	def getdata(self):
		global data
		url = urllib.urlopen('http://api.fixer.io/latest')
		data = json.load(url)
		url.close()

	def user_input(self):
		print "please select the currency u want to convert"
		a.show()
		b=input()

		print "please select the currency u want to convert to"
		a.show()
		c=input()

		print "please enter the ammount u want to convert"
		d=raw_input()
		Convert(b,c,d)
		print "do u want to continue?"
		print "press 0 to exit and 1 to continue"
		e=input()
		return e
class Convert(object):
	def __init__(self, b ,c,d):
		global data
		first_cur, firs_value = data['rates'].items()[b-1]
		second_cur, sec_value = data['rates'].items()[c-1]
		rate = (sec_value*float(d))/firs_value
		print d, first_cur, "= ", rate, second_cur


a = Display()
a.getdata()
e=1
while(e!=0):
	e =  a.user_input() 




