import os
import core
import urllib.request
import urllib.parse
import re
import sys

i = 0

def main():
	data = create()
	core.log('log', data)
	data = core.split(data)

	videos = search(data)
	core.log('log', videos)
	videos = core.split(videos)

	download(data, videos)

	clear()

def create():
	global i
	location = 'Placeholder'

	while len(location) > 0:
		idct = input("dir>")
		if len(idct) > 0:
			dct = idct
		location = input("srh> ")
		if len(location) > 0:
			i = i + 1
			data ="{}\n{}".format(dct, location)
			core.log('info', data)

	data = core.read('info')
	
	return data



def search(data):
	global i
	il = i
	ii = 1
	while il > 0:
		location = data[ii]
		query_string = urllib.parse.urlencode({"search_query" : location})
		html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
		search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
		core.log('videos',("http://www.youtube.com/watch?v=" + search_results[0]))
		ii = ii + 2
		il = il - 1

	videos = core.read('videos')

	return videos

def download(data, videos):
	global i
	string = 'cd {}' + '\n' + 'youtube-dl {}'
	il = i
	di = 0
	vi = 1

	while il > 0:
		dct = data[di]
		download = videos[vi]
		os.system(string.format(dct, download))
		il = il - 1
		di = di + 2
		vi = vi + 1

def log(filefrom, fileto):
	x = core.read(filefrom)
	core.log(fileto, x)

def clear():
	core.write('info', '')
	core.write('videos', '')

main()