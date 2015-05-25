#!/usr/bin/python

import os
import os.path
rootdir = "/home/zj/Dthreads/src/"

result = file('allLibsDthreadsNeed', 'w')

def fun(path):
	global libList
	for parent,dirnames,filenames in os.walk(path):
		for filename in filenames:
		#	print path + filename
			wholeFilename = parent + '/' + filename
			finput = file(wholeFilename, 'r')
			while True:
				line = finput.readline()
				if len(line) == 0:
					break
				line.strip()
				
				if line.find('#include <') == 0:
					if libList.has_key(line):
						libList[line] = libList[line] + wholeFilename + ';'
					else:
						libList[line] = wholeFilename + ';'
					
			finput.close()

        #        for dirname in dirnames:
	#		print parent + dirname
        #                if dirname.find('.') == 0:
        #                        continue
        #                fun(parent + dirname + '/')


libList = {}
fun(rootdir)
#libList.sort()
#sortedList = sorted(libList.iteritems(), key = lambda d:d[0],reverse =  False)

for key in libList.keys():
#	print line
	result.write(key + libList[key] + '\n')
result.close()
