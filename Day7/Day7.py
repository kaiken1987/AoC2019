inputs = [0,0]
best =""
lastout = 0

inital = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
class amp :
	def __init__(self, phase, ints):
		self.finished = False
		self.ints = ints.copy()
		self.pos = 0
		self.phase = phase

	def getParam(self, idx, mode ) :
		a = self.ints[idx]
		if( mode == '0'):
			a = self.ints[a]
		return int(a)

	def intercode(self):
		global inputs
		global lastout
		while self.pos < len(self.ints) :
			opcode = self.ints[self.pos] % 100
			modes = str(self.ints[self.pos] // 100+1000)
			if(opcode== 1):
				a = self.getParam(self.pos+1,modes[3])
				b = self.getParam(self.pos+2,modes[2])
				c = self.ints[self.pos+3]
				self.ints[c] = a+b
				if(c!=self.pos):
					self.pos += 4
			elif (opcode== 2):
				a = self.getParam(self.pos+1,modes[3])
				b = self.getParam(self.pos+2,modes[2])
				c = self.ints[self.pos+3]
				self.ints[c] = a * b
				if(c!=self.pos): 
					self.pos += 4
			elif (opcode== 3):
				c = self.ints[self.pos+1]
				if( len(inputs)==0 ):
					print('Not enough inputs')
					print('Pos: '+str(self.pos))
					print('Dumping Memory\n'+str(self.ints))
					exit
				if( self.pos == 0):
					self.ints[c] = self.phase
				else :
					self.ints[c] = lastout
				inputs = inputs[:-1]
				if(c!=self.pos):
					self.pos += 2
			elif (opcode== 4):
				a = self.getParam(self.pos+1,modes[3])
				lastout = int(a)
				#print( str( a ) )
				self.pos += 2
				return False
			elif (opcode== 5):
				a = self.getParam(self.pos+1,modes[3])
				b = self.getParam(self.pos+2,modes[2])
				if a != 0 :
					self.pos = b
				else :
					self.pos+=3
			elif (opcode== 6):
				a = self.getParam(pos+1,modes[3])
				b = self.getParam(pos+2,modes[2])
				if a == 0 :
					self.pos = b
				else :
					self.pos+=3
			elif (opcode== 7):
				a = self.getParam(self.pos+1,modes[3])
				b = self.getParam(self.pos+2,modes[2])
				c = self.ints[self.pos+3]
				if a < b :
					self.ints[c] = 1
				else :
					self.ints[c] = 0
				if(c!=self.pos):
					self.pos += 4
			elif (opcode== 8):
				a = self.getParam(self.pos+1,modes[3])
				b = self.getParam(self.pos+2,modes[2])
				c = self.ints[self.pos+3]
				if a == b :
					self.ints[c] = 1
				else :
					self.ints[c] = 0
				if(c!=self.pos):
					self.pos += 4
			elif (opcode==99):
				self.finished = True
				return True
				break
			else:
				print("Unknow value encountered")
				return True
				break
		return True


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
						phase = [e+5,d+5,c+5,b+5,a+5]
						lastout = 0
						amps = [amp(a+5,inital),amp(b+5,inital),amp(c+5,inital),amp(d+5,inital), amp(e+5,inital)]
						while not amps[-1].finished:
							for x in amps :
								inputs = [lastout,x.phase]
								x.intercode()
						if(lastout>maxout):
							maxout = lastout
							best = str(phase)
	return maxout

#ints.clear()
#f = open("opcodes.txt", "r")
#for x in f:
#	inital.append( int(x) )

inital =[3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
max = runAmps()
print("Test Max: "+str(max)+ " seq: " + best)
print("Should be: 139629729 Pass: "+str(max==139629729))

inital =[3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
max = runAmps()
print("Test Max: "+str(max)+ " seq: " + best)
print("Should be: 18216 Pass: "+str(max==18216))

inital.clear()
f = open("opcodes.txt", "r")
for x in f:
	inital.append( int(x) )
max = runAmps()
print("Output Max: "+str(max)+ " seq: " + best)

	