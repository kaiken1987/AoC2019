ints = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
	1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
	999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

input = 0
inputa = 1
inputb = 5

def getParam( pos, mode ) :
	a = ints[pos]
	if( mode == '0'):
		a = ints[a]
	return a

def intercode():
	pos = 0
	while pos < len(ints) :
		opcode = ints[pos] % 100
		modes = str(ints[pos]/100+1000)
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
			ints[c] = input
			if(c!=pos):
				pos += 2
		elif (opcode== 4):
			a = getParam(pos+1,modes[3])
			print( str( a ) )
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
			print("DONE")
			return True
			break
		else:
			print("Unknow value encountered")
			return False
			break
	return False

ints.clear()
inital = []
f = open("C:\code\python\AdventOfCode\Day5\opcodes.txt", "r")
for x in f:
	ints.append( int(x) )
input = inputa
intercode()
