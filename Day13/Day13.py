import curses

screen = curses.initscr()
#screen = curses.newwin(26,40,0,0)
screen.clear()

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
		self.outmode = 0
		self.x = 0
		self.y = 0
		self.score = 0
		self.paddle = (0,0)
		self.ball = (0,0)

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
	def printScreen(self) :
		screen.addstr(21,0, "Score: {}".format(self.score))
		screen.refresh()
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
				c = self.getPos(self.pos+1,modes[0])
				#self.printScreen()
				screen.addstr(21,0, "Score: {}".format(self.score))
				screen.refresh()
				stick = 3
				while stick == 3 :
					#key = screen.getkey()
					if self.ball[0]<self.paddle[0] :#key[0]=='a' :
						stick = -1
					elif self.ball[0]==self.paddle[0] :#key[0]=='s' :
						stick = 0
					elif self.ball[0]>self.paddle[0] :#key[0]=='d' :
						stick = 1
				self.ints[c] = stick
				if(c!=self.pos):
					self.pos += 2
			elif (opcode== 4):
				a = self.getParam(self.pos+1,modes[0])
				if self.outmode == 0 :
					self. x = a
					self.outmode = 1
				elif self.outmode == 1 :
					self.y = a
					self.outmode = 2
				else:
					if( self.x == -1 ):
						self.score = a 
					else:
						if a == 0 :
							screen.addch(self.y,self.x,' ')
						elif a == 1 :
							screen.addch(self.y,self.x,'X')
						elif a == 2 :
							screen.addch(self.y,self.x,'■')
						elif a == 3 :
							screen.addch(self.y,self.x,'♣')
							self.paddle = (self.x,self.y)
						elif a == 4 :
							screen.addch(self.y,self.x,'O')
							self.ball = (self.x,self.y)
						else:
							screen.addch(self.y,self.x, str(a))
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

blocks = 0

comp.printScreen()

print( "Blocks: " + str(blocks) )