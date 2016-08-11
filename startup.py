import os
import core
import urllib.request
import urllib.parse
import re
import sys

globalInteger = 0

def main():
	create()
	data = core.read('info')
	core.log('log', data)
	data = core.split(data)

	createPlaylist()
	playlistUrls = core.read('playlistUrls')
	core.log('log', playlistUrls)
	playlistUrls = core.split(playlistUrls)

	#playlist(playlistUrls)
	search(data)

	videos = core.read('playlistUrls')
	core.log('log', videos)
	videos = core.split(videos)

	download(data, videos)

	clear()

def create():
	global globalInteger
	location = 'Placeholder'

	while len(location) > 0:
		idct = input("Directory>")
		if len(idct) > 0:
			dct = idct
		location = input("Keyword> ")
		if len(location) > 0:
			globalInteger = globalInteger + 1
			data ="{}\n{}".format(dct, location)
			core.log('info', data)

	data = core.read('info')
	
	return

def createPlaylist():
	global globalInteger
	playlistUrl = 'Placeholder'
	while len(playlistUrl) > 0:
		idct = input("Directory>")
		if len(idct) > 0:
			dct = idct
		playlistUrl = input("Playlist Url> ")
		if len(playlistUrl) > 0:
			globalInteger = globalInteger + 1
			playlistUrls ="{}\n{}".format(dct, playlistUrl)
			core.log('playlistUrls', playlistUrls)
			playlist(playlistUrl)

	playlistUrls = core.read('playlistUrls')
	
	return



def search(data):
	global globalInteger
	il = globalInteger
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

	return

def playlist(playlistUrl):
	print("****************" + playlistUrl)
	#query_string = urllib.parse.urlencode({playlistUrls})
	html_content = urllib.request.urlopen(playlistUrl)
	#print("***************" + html_content.read().decode())
	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
	#print("*****************" + ', '.join(search_results))

	localInteger = len(search_results)
	searchInteger = 0
	while localInteger > 0:
		core.log('videos', search_results[searchInteger])
		localInteger = localInteger - 1
		searchInteger = searchInteger + 1

		return

def download(data, videos):
	global globalInteger
	string = 'cd {}' + '\n' + 'youtube-dl {}'
	il = globalInteger
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