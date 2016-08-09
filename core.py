import os

def main():
	print "hi"

	return
	
def write(x, y):
	w = open(x, 'w')

	w.write(y)

	w.close

	return

def log(x, y):
	w = open(x, 'a')
	
	w.write(y + "\n")

	w.close

	return

def read(y):
	r = open(y, 'r')
	
	z = r.read()
	
	r.close()

	return z

#	os.system("echo {} | espeak".format(x))

#Calling area
#main()
