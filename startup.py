import os
import core
import urllib.request
import urllib.parse
import re
import sys

#dct = None

def main():
	#global dct
	idct = input("dir> ")

	dct = idct
	create(dct)

def create(dct):
	location = input("srh> ")

	data = "{}\n{}".format(dct, location)

	core.log('info', data)

	if len(location) < 1:
		search()

	create(dct)

def search():
	linesa = core.split(core.read('info'))
	i = len(linesa)
	ii = 1
	while i > 1:
		location = linesa[ii]
		i = i - 2
		ii = ii + 2

		query_string = urllib.parse.urlencode({"search_query" : location})
		html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
		search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
		core.log('videos', "http://www.youtube.com/watch?v=" + search_results[0])

	log('videos', 'log')

	download()

	core.write('videos', '')
	core.write('info', '')

	sys.exit()

def download():
	linesb = core.split(core.read('videos'))
	linesc = core.split(core.read('info'))
	iiii = len(linesc)
	i = len(linesb)
	ii = 1
	iii = 1
	while i > 0:
		download = linesb[ii]
		dct = linesc[iii]
		i = i - 1
		ii = ii + 1
		iii = iii + 2

		os.system("cd {}".format(dct))
		os.system("youtube-dl {}".format(download))



def log(filefrom, fileto):
	x = core.read(filefrom)
	core.log(fileto, x)

main()

#search()
