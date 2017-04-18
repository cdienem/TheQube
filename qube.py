import numpy as np

vectors = [3,2,3,2,2,4,2,3,2,3,2,3,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,3,4,2,2,2,4,2,3,2,2,2,2,2,2,2,2,2,4,2]

matrix = []



def inPath(needle,hay):
	for h in hay:
		#print "Comparing: "+str(needle) + " " +str(h)
		if (needle==h).all():
			return True
		else:
			r = False
			pass
	return r

def checkPos(needle):
	if needle[0] not in range(0,4) or needle[1] not in range(0,4) or needle[2] not in range(0,4):
		return True
	else:
		return False


def vec(path, ind, direct):
	l = vectors[ind]
	
	operators = [
		[np.array([0,0,-1]),np.array([0,0,1]),np.array([0,-1,0]),np.array([0,1,0])],
		[np.array([-1,0,0]),np.array([1,0,0]),np.array([0,0,-1]),np.array([0,0,1])],
		[np.array([-1,0,0]),np.array([1,0,0]),np.array([0,-1,0]),np.array([0,1,0])]
	]

	ser = [] #this is used to collect possible series
	
	# go through allowed operators and create new positions based on the length of the next brick

	for op in operators[direct[-1]]:
		positions = []
		i = 1
		while i < vectors[ind]:
			pos = path[-1] + i*op
			
			if inPath(pos,path) or checkPos(pos):
				positions = []
				break
			else:
				positions.append(pos)
				i = i+1
		#print positions
		if len(positions) > 0:
			ser.append(positions)
			# add the new direction to the end of the array for later.
			directions = {"[ True  True False]":2, "[ True False  True]":1, "[False  True  True]":0}
			compare = str(positions[0] == path[-1])
			positions.append(directions[compare])
	#print ser
	#print len(ser)
	if len(ser) > 0:
		index = ind+1
		for item in ser:
			temp = []
			# read out the direction
			di = direct+[item[-1]]
			#delete it
			del(item[-1])
			# make updated path
			temp = path+item
			#print "Current ("+str(len(temp))+"): "+str(temp)
			#raw_input("...")
			if len(temp) < 64:
				#print "Too short: "+str(len(temp))
				vec(temp, index, di)
			else:
				print "Good: "+str(len(temp))+" -> "+str(temp)


for a in range(0,4):
	for b in range(0,2):
		for c in range(0,2):
			vec([np.array([a,b,c])],0,[0])
