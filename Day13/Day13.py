
lastout = 0

class panel :
	def __init__(self,x,y) :
		self.x = x
		self.y = y 
		self.type = 0
	def __eq__(self,value) :
		return self.x == value.x and self.y == value.y
	def __str__(self) :
		return "({},{}), type:{}".format(self.x, self.y,self.type)
	
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
		self.panels = [panel(0,0)]
		self.outmode = 0
		self.x = 0
		self.y = 0
		self.minx = 0
		self.miny = 0
		self.maxx = 0
		self.maxy = 0
		self.screen = []
		for x in range(20) :
			self.screen.append("0000000000000000000000000000000000000000")

	def getPos(self, idx, mode ) :
		a = idx
		if( mode == '0'):
			a = self.ints[a]
		elif( mode == '2'):
			a = self.ints[a]+self.base
		return int(a)
	def getParam(self, idx, mode ) :
		a = self.getPos(idx, mode)
		a = self.ints[a]
		return int(a)

	def intercode(self):
		global inputs
		global lastout
		while self.pos < len(self.ints) :
			opcode = self.ints[self.pos] % 100
			modes = str(self.ints[self.pos] // 100+10000)
			modes = modes[::-1]
			if(opcode== 1):
				a = self.getParam(self.pos+1,modes[0])
				b = self.getParam(self.pos+2,modes[1])
				c = self.getPos(self.pos+3,modes[2])
				self.ints[c] = a+b
				if(c!=self.pos):
					self.pos += 4
			elif (opcode== 2):
				a = self.getParam(self.pos+1,modes[0])
				b = self.getParam(self.pos+2,modes[1])
				c = self.getPos(self.pos+3,modes[2])
				self.ints[c] = a * b
				if(c!=self.pos): 
					self.pos += 4
			elif (opcode== 3):
				c = self.getPos(self.pos+1,modes[0])
				if( len(self.inputs)==0 ):
					print('Not enough inputs')
					print('Pos: '+str(self.pos))
					print('Dumping Memory\n'+str(self.ints))
					return True
				self.ints[c] = self.inputs[-1]
				self.inputs = self.inputs[:-1]
				if(c!=self.pos):
					self.pos += 2
			elif (opcode== 4):
				a = self.getParam(self.pos+1,modes[0])
				if self.outmode == 0 :
					self. x = a
					self.minx = min(a,self.minx)
					self.maxx = max(a,self.maxx)
					self.outmode = 1
				elif self.outmode == 1 :
					self.y = a
					self.miny = min(a,self.miny)
					self.maxy = max(a,self.maxy)
					self.outmode = 2
				else:
					p = panel(self.x, self.y)
					line = self.screen[self.y]
					self.screen[self.y] = line[0:self.x]+str(a)+line[self.x+1:-1]
					try :
						idx = self.panels.index(p)
						self.panels[idx].type = a
					except :
						p.type = a
						self.panels.append(p)
					self.outmode = 0
				self.pos += 2
				#return False
			elif (opcode== 5):
				a = self.getParam(self.pos+1,modes[0])
				b = self.getParam(self.pos+2,modes[1])
				if a != 0 :
					self.pos = b
				else :
					self.pos+=3
			elif (opcode== 6):
				a = self.getParam(self.pos+1,modes[0])
				b = self.getParam(self.pos+2,modes[1])
				if a == 0 :
					self.pos = b
				else :
					self.pos+=3
			elif (opcode== 7):
				a = self.getParam(self.pos+1,modes[0])
				b = self.getParam(self.pos+2,modes[1])
				c = self.getPos(self.pos+3,modes[2])
				if a < b :
					self.ints[c] = 1
				else :
					self.ints[c] = 0
				if(c!=self.pos):
					self.pos += 4
			elif (opcode== 8):
				a = self.getParam(self.pos+1,modes[0])
				b = self.getParam(self.pos+2,modes[1])
				c = self.getPos(self.pos+3,modes[2])
				if a == b :
					self.ints[c] = 1
				else :
					self.ints[c] = 0
				if(c!=self.pos):
					self.pos += 4
			elif (opcode== 9):
				a = self.getParam(self.pos+1,modes[0])
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

memory = [None]*4096
inital = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
testa = computer(inital)
print( "TESTS")
#testa.intercode()

print( "Day 13A")
inital.clear()
f = open("opcodes.txt", "r")
cnt = 0
for x in f:
	memory[cnt]= int(x)
	cnt+=1
	
comp = computer(memory)
comp.intercode()

print( "Day 11A")
blocks = 0
for p in comp.panels :
	if(p.type == 2):
		blocks += 1
for p in comp.screen :
	print( p )


print( "Blocks: " + str(blocks) )