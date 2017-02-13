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

def exists_create_newfile(filename):
	text = open(filename,'r')
	new_file = raw_input('name new_file: ')
	sec_checker(new_file,text,filename)

def sec_checker(new_file,text,filename):
	if os.path.isfile(new_file):
		print 'file name already existing, use existing and add new content?'
		yn = raw_input('yes or no: ')
		if yn == 'yes':
			text2 = open(new_file,'r+')
			z = ""
			for x in text2:
				z += x
			text2.seek(0)
			text2.write(z + exists(filename))
		elif yn == 'no':
			new_file1 = raw_input('name new_file: ')
			while os.path.isfile(new_file1):
				fn = raw_input('file still exists, enter new filename')
				new_file1 = fn
			fn2 = open(new_file1,'a+')
			fn2.write(exists(filename))
	else:
		text2 = open(new_file,'w+')
		text2.write(exists(filename))



def exists(filename):
	text = open(filename,'r')
	return save(text)

def save(text):
	t = "" 
	for x in text:
		t += x
	return t
	

def not_exists_createfile(filename):
	print 'not existing'
	create = open(filename,'w+')
	y = add_content()
	create.write(y)

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

