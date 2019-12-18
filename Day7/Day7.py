inputs = [0,0]
best =""
lastout = 0

ints = []
inital = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

def getParam( pos, mode ) :
	global ints
	a = ints[pos]
	if( mode == '0'):
		a = ints[a]
	return int(a)

def intercode():
	pos = 0
	global inputs
	global lastout
	global ints
	while pos < len(ints) :
		opcode = ints[pos] % 100
		modes = str(ints[pos] // 100+1000)
		if(opcode== 1):
			a = getParam(pos+1,modes[3])
			b = getParam(pos+2,modes[2])
			c = ints[pos+3]
			ints[c] = a+b
			if(c!=pos):
				pos += 4
		elif (opcode== 2):
			a = getParam(pos+1,modes[3])
			b = getParam(pos+2,modes[2])
			c = ints[pos+3]
			ints[c] = a * b
			if(c!=pos): 
				pos += 4
		elif (opcode== 3):
			c = ints[pos+1]
			if( len(inputs)==0 ):
				print('Not enough inputs')
				print('Pos: '+str(pos))
				print('Dumping Memory\n'+str(ints))
				exit
			ints[c] = inputs[-1]
			inputs = inputs[:-1]
			if(c!=pos):
				pos += 2
		elif (opcode== 4):
			a = getParam(pos+1,modes[3])
			lastout = int(a)
			#print( str( a ) )
			pos += 2
		elif (opcode== 5):
			a = getParam(pos+1,modes[3])
			b = getParam(pos+2,modes[2])
			if a != 0 :
				pos = b
			else :
				pos+=3
		elif (opcode== 6):
			a = getParam(pos+1,modes[3])
			b = getParam(pos+2,modes[2])
			if a == 0 :
				pos = b
			else :
				pos+=3
		elif (opcode== 7):
			a = getParam(pos+1,modes[3])
			b = getParam(pos+2,modes[2])
			c = ints[pos+3]
			if a < b :
				ints[c] = 1
			else :
				ints[c] = 0
			if(c!=pos):
				pos += 4
		elif (opcode== 8):
			a = getParam(pos+1,modes[3])
			b = getParam(pos+2,modes[2])
			c = ints[pos+3]
			if a == b :
				ints[c] = 1
			else :
				ints[c] = 0
			if(c!=pos):
				pos += 4
		elif (opcode==99):
			return True
			break
		else:
			print("Unknow value encountered")
			return False
			break
	return False


def runAmps():
	maxout = 0
	global inputs
	global best
	global ints
	global lastout
	for a in range(5) :
		for b in range(5) :
			if(b==a): continue
			for c in range(5) :
				if(c==a or c==b): continue	
				for d in range(5) :
					if(d==a or d==b or d == c): continue	
					for e in range(5) :
						if(e==a or e==b or e==c or e==d): continue
						phase = [e,d,c,b,a]
						lastout = 0
						ints = inital
						for x in phase :
							inputs = [lastout,x]
							intercode()
						if(lastout>maxout):
							maxout = lastout
							best = str(e)+str(d)+str(c)+str(b)+str(a)
	return maxout

#ints.clear()
#f = open("opcodes.txt", "r")
#for x in f:
#	inital.append( int(x) )

max = runAmps()
print("Test Max: "+str(max)+ " seq: " + best)
print("Should be: 43210 Pass: "+str(max==43210))

inital =[3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
max = runAmps()
print("Test Max: "+str(max)+ " seq: " + best)
print("Should be: 54321 Pass: "+str(max==54321))

inital =[3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
max = runAmps()
print("Test Max: "+str(max)+ " seq: " + best)
print("Should be: 65210 Pass: "+str(max==65210))


ints.clear()
f = open("opcodes.txt", "r")
for x in f:
	inital.append( int(x) )
max = runAmps()
print("Output Max: "+str(max)+ " seq: " + best)

	