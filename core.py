import os
	
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

def split(x):
	lines = x.split('\n')

	return lines


#	os.system("echo {} | espeak".format(x))

#Calling area
#main()