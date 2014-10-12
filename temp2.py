#!/usr/bin/python

import hashlib
import os
from functools import partial

def start():
	print ("""This is a program created to analyze change in data in a file.  
The program till need a sourcefile and a destination file.
Be carefull not to overwrite any file when typing filename's """)
	print "\n"
	print "\n"

#check if source is valid
def validSource(source):		 
	while not os.path.isfile(source):
		print "Source-File does not exist"
		print "Try again"
		print "\n"
		print "Enter source-file"
		source = raw_input()

#Check if dest.file is valid, if not create file
def validDest(dest):		
	while(dest == source):
		print "******************************************"
		print "Desination cannot be same as source"
		print "******************************************" + "\n"
		print "Enter name of destination"
		dest = raw_input()
	else:
		while not os.path.isfile(dest):
			open(dest,'a')

#Create the checksum
def makeSum(data):
	md5 = hashlib.md5()
	md5.update(data)
	return md5.hexdigest()

#Write the Checksum to file
def writeSum(data):
	#open destFile
	global destFile
	destFile = open(dest, 'a')
	md5 = makeSum(data)
	destFile.write(md5 + '\n')
	#destFile.close()	

#Initialize

start()

#collect info from user
print "Enter name of sourcefile"	 
source = raw_input()

#collect info from user
print "Enter name of destination file"
dest = raw_input()

validDest(dest)

#open File to read
readFile = open(source, 'r')
read = partial(readFile.read, 511)

#Read eachBlock and create a sum
read_block = partial(readFile.read, 511)
for block in iter(read_block, ''):
	writeSum(block)

readFile.close()
destFile.close()

