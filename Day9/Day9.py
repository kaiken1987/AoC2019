
lastout = 0

class computer :
	def __init__(self, ints):
		self.finished = False
		self.ints = ints.copy()
		for i in range(len(ints), 1024) :
			self.ints.append(0)
		self.pos = 0
		self.base  = 0
		self.lastout = 0
		self.inputs = []

	def getParam(self, idx, mode ) :
		a = self.ints[idx]
		if( mode == '0'):
			a = self.ints[a]
		if( mode == '2'):
			a = self.ints[a+self.base]
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
				if( len(self.inputs)==0 ):
					print('Not enough inputs')
					print('Pos: '+str(self.pos))
					print('Dumping Memory\n'+str(self.ints))
					return True
				self.ints[c] = self.inputs[-1]
				self.inputs = self.inputs[:-1]
				self.inputs = self.inputs[:-1]
				if(c!=self.pos):
					self.pos += 2
			elif (opcode== 4):
				a = self.getParam(self.pos+1,modes[3])
				lastout = int(a)
				print( str( a ) )
				self.pos += 2
				#return False
			elif (opcode== 5):
				a = self.getParam(self.pos+1,modes[3])
				b = self.getParam(self.pos+2,modes[2])
				if a != 0 :
					self.pos = b
				else :
					self.pos+=3
			elif (opcode== 6):
				a = self.getParam(self.pos+1,modes[3])
				b = self.getParam(self.pos+2,modes[2])
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
			elif (opcode== 9):
				a = self.getParam(self.pos+1,modes[3])
				self.base += int(a)
				self.pos += 2
			elif (opcode==99):
				self.finished = True
				return True
				break
			else:
				print("Unknow value encountered")
				return True
				break
		return True

memory = []*1024
inital = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
testa = computer(inital)
inital = [1102,34915192,34915192,7,4,7,99,0]
testb = computer(inital)
inital = [104,1125899906842624,99]
testc = computer(inital)
print( "TESTS")
testa.intercode()
testb.intercode()
testc.intercode()

print( "Day 9A")
inital.clear()
f = open("opcodes.txt", "r")
for x in f:
	inital.append( int(x) )

comp = computer(inital)
comp.inputs = [1]
comp.intercode()
