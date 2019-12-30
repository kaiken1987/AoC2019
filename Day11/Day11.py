import math
class panel :
	def __init__(self,x,y) :
		self.x = x
		self.y = y 
		self.white = False
	def __eq__(self,value) :
		return self.x == value.x and self.y == value.y
	def __str__(self) :
		return "({},{}), white:{}".format(self.x, self.y,self.white)
	
class computer :
	turn = math.pi/2
	def __init__(self, ints):
		self.finished = False
		self.ints = ints.copy()
		for i in range(len(ints), 1024) :
			self.ints.append(0)
		self.pos = 0
		self.base  = 0
		self.move = False
		self.x = 0
		self.y = 0
		self.hdg = 0
		self.input = panel(0,0)
		self.input.white = True
		self.panels = [self.input]
		self.paintCnt = 0

		
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
				a = self.getPos(self.pos+1,modes[0])
				try :
					pt = panel(self.x,self.y)
					idx = self.panels.index(pt)
					self.input = self.panels[idx]
				except :
					self.input = pt
				if(self.input.white):
					self.ints[a] = 1
				else:
					self.ints[a] = 0
				self.pos += 2
			elif (opcode== 4):
				a = self.getParam(self.pos+1,modes[0])
				if self.move :
					#move panel
					if a == 0:
						self.hdg -= computer.turn
					else:
						self.hdg += computer.turn
					if( self.hdg>math.pi):
						self.hdg-=math.pi*2
					if( self.hdg<-math.pi):
						self.hdg+=math.pi*2
					self.x += round(math.sin(self.hdg))
					self.y -= round(math.cos(self.hdg))
				else:
					#paint panel
					pt = panel(self.x,self.y)
					idx = len(self.panels)
					try :
						idx = self.panels.index(pt)
					except :
						self.paintCnt += 1
						self.panels.append(pt)
					if a == 0:
						self.panels[idx].white = False
					else :
						self.panels[idx].white = True

					#print( str(self.panels[idx]) )
				self.move = not self.move
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
		print("Reached end of code")
		return True

	
inital = [3,8,1005,8,314,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,28,2,2,16,10,1,1108,7,10,1006,0,10,1,5,14,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,65,1006,0,59,2,109,1,10,1006,0,51,2,1003,12,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,101,1006,0,34,1,1106,0,10,1,1101,17,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,135,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1001,8,0,156,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1001,8,0,178,1,108,19,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,204,1,1006,17,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,230,1006,0,67,1,103,11,10,1,1009,19,10,1,109,10,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,101,0,8,268,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,290,2,108,13,10,101,1,9,9,1007,9,989,10,1005,10,15,99,109,636,104,0,104,1,21101,48210224024,0,1,21101,0,331,0,1105,1,435,21101,0,937264165644,1,21101,0,342,0,1105,1,435,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,235354025051,0,1,21101,389,0,0,1105,1,435,21102,29166169280,1,1,21102,400,1,0,1105,1,435,3,10,104,0,104,0,3,10,104,0,104,0,21102,709475849060,1,1,21102,1,423,0,1106,0,435,21102,868498428684,1,1,21101,434,0,0,1105,1,435,99,109,2,21201,-1,0,1,21101,0,40,2,21102,1,466,3,21101,456,0,0,1105,1,499,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,461,462,477,4,0,1001,461,1,461,108,4,461,10,1006,10,493,1101,0,0,461,109,-2,2106,0,0,0,109,4,2102,1,-1,498,1207,-3,0,10,1006,10,516,21102,1,0,-3,21201,-3,0,1,21201,-2,0,2,21102,1,1,3,21102,535,1,0,1106,0,540,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,563,2207,-4,-2,10,1006,10,563,21202,-4,1,-4,1106,0,631,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21101,582,0,0,1105,1,540,22102,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,601,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,623,22102,1,-1,1,21101,623,0,0,105,1,498,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]
#inital = [104,1,104,0,103,1,104,0,104,0,104,1,104,0,104,1,104,0,103,1,104,0,104,1,104,1,104,0,104,1,104,0,99]
memory = inital.copy()
for i in range(len(memory),4096) :
	memory.append(0)
comp = computer(memory)
comp.intercode()
grid = [[],[],[],[],[],[],[],[],[],[],[],[]]
for y in range(6):
	str = ''
	for x in range(40) :
		pt = panel(x,y)
		try:
			idx = comp.panels.index(pt)
			pt = comp.panels[idx]
		except:
			idx = -1
		if(pt.white):
			str += ' '
		else:
			str +='■'
	print(str)

if(comp.finished):
	print("Run success %d panels painted"% (comp.paintCnt) )
else:
	print("Run failed")