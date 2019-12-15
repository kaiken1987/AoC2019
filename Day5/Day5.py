ints = [3,0,4,0,99]

input = open('inputs.txt','r')

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
			pos += 4
		elif (opcode== 2):
			a = getParam(pos+1,modes[3])
			b = getParam(pos+2,modes[2])
			c = ints[pos+3]
			ints[c] = a * b
			pos += 4
		elif (opcode== 3):
			ints[ints[pos+1]] = int( input.readline() )
			pos += 2
		elif (opcode== 4):
			a = getParam(pos+1,modes[3])
			print( str( a ) )
			pos += 2
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

intercode()
