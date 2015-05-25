#!/usr/bin/python

import os
import os.path
rootdirsource = "/home/zj/Dthreads-noinclude/src/source/"
rootdirinclude = "/home/zj/Dthreads-noinclude/src/include/"

totalLine = 0

#result = file('allLibsDthreadsNeed', 'w')

def fun(path):
#	global libList
	global totalLine
	for parent,dirnames,filenames in os.walk(path):
		for filename in filenames:
		#	print path + filename
			wholeFilename = parent + '/' + filename
			finput = file(wholeFilename, 'r')
			foutput = file(wholeFilename + '-noinclude', 'w')
			while True:
				line = finput.readline()
				totalLine = totalLine + 1
				if len(line) == 0:
					break
			#	line.strip()
				
			#	if line.find('#include <') < 0 and line.find('#include<') < 0:
				if line.find('#include') < 0:
					foutput.write(line)
					#if libList.has_key(line):
					#	libList[line] = libList[line] + wholeFilename + ';'
					#else:
					#	libList[line] = wholeFilename + ';'
					
			finput.close()
			os.remove(wholeFilename)
			foutput.close()
			os.rename(wholeFilename + '-noinclude', wholeFilename)

        #        for dirname in dirnames:
	#		print parent + dirname
        #                if dirname.find('.') == 0:
        #                        continue
        #                fun(parent + dirname + '/')

def gccFile(path):
	for parent,dirnames,filenames in os.walk(path):
		for filename in filenames:
			wholeFilename = parent + '/' + filename
			os.system('g++ ' + wholeFilename + ' 2>error_' + filename)


#libList = {}
fun(rootdirsource)
fun(rootdirinclude)

gccFile(rootdirsource)
gccFile(rootdirinclude)

print totalLine
#libList.sort()
#sortedList = sorted(libList.iteritems(), key = lambda d:d[0],reverse =  False)

#for key in libList.keys():
#	print line
#	result.write(key + libList[key] + '\n')
#result.close()
