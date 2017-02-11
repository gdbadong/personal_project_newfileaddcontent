#!/usr/bin/env python

import os
import sys

#check if your file exists
# if your file exists then continue if not
# then it asks you to give a filename and content

# class file



filename = raw_input('type filename with extension: ')
# text2.write(exists(filename))
t = ""
t2 = ""
sample = ""
sample2 = ""
def check_exists(filename):
	if not os.path.isfile(filename):
		not_exists_createfile(filename)
	else:
		exists_create_newfile(filename)

		# sample2 += exists(filename)
		# print sample2


def exists_create_newfile(filename):
	text = open(filename,'r')
	new_file = raw_input('name new_file: ')
	if os.path.isfile(new_file):
		text2 = open(new_file,'r')
		print text2.write(exists(filename))
	else:
		text2 = open(new_file,'w+')
	# y = exists(filename)
		print text2.write(exists(filename))
	# print text2.write(y)



def exists(filename):
	text = open(filename,'r')
	t = ''
	for x in text:
		t += x
	text.seek(0)
	t += text.read()
	return t
	

def not_exists_createfile(filename):
	print 'not existing'
	create = open(filename,'w+')
	y = add_content()
	create.write(y)
	# print create.write(y)

def add_content():
	t = ""
	x = 0
	while x == 0:
		content = raw_input('add content? yes/no ')
		if	content == 'yes':
			content1 = raw_input('type content: ')
			t = t + content1 +'\n'
			x+=0
		else:
			content == 'no'
			x+=1
	return t




check_exists(filename)

