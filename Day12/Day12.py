import numpy

class planet :
	def __init__(self,x,y,z) :
		self.x = x
		self.y = y
		self.z = z
		self.vx = 0
		self.vy = 0
		self.vz = 0	
	def __str__(self) :
		return "pos=<x={}, y={}, z={}>, vel=<x={}, y={}, z={}>".format(self.x, self.y, self.z,self.vx,self.vy,self.vz)
	def hash(self) :
		return "%03x%03x%03x%03x%03x%03x"% (self.x, self.y, self.z,self.vx,self.vy,self.vz)
	def __eq__(self,value) :
		return self.x == value.x and self.y == value.y and self.z == value.z and self.vx == value.vx and self.vy == value.vy and self.vz == value.vz	
	def copy(self) :
		p = planet(self.x,self.y,self.z)
		p.vx = self.vx
		p.vy = self.vy
		p.vz = self.vz
		return p
	def gravity(self,comp):
		if(self.x<comp.x):
			self.vx+=1
			comp.vx-=1
		elif(self.x>comp.x):
			self.vx-=1
			comp.vx+=1
		if(self.y<comp.y):
			self.vy+=1
			comp.vy-=1
		elif(self.y>comp.y):
			self.vy-=1
			comp.vy+=1
		if(self.z<comp.z):
			self.vz+=1
			comp.vz-=1
		elif(self.z>comp.z):
			self.vz-=1
			comp.vz+=1
	def move(self):
		self.x += self.vx
		self.y += self.vy
		self.z += self.vz

planets = [
	#test
	#planet(-1,0,2),
	#planet(2,-10,-7),
	#planet(4,-8,8),
	#planet(3,5,-1)
	#test2
	#planet(-8, -10, 0),
	#planet(5, 5, 10),
	#planet(2, -7, 3),
	#planet(9, -8, -3)
	#real
	planet(14, 9, 14),
	planet(9, 11, 6),
	planet(-6, 14, -4),
	planet(4, -4, -3)
	]
def hash(sats):
	hashs = ['','','']
	for s in sats :
		hashs[0]+=("%03x%03x"% (s.x, s.vx) )
		hashs[1]+=("%03x%03x"% (s.y, s.vy) )
		hashs[2]+=("%03x%03x"% (s.z, s.vz) )
	return hashs

prev = []
count = 0
inital = hash(planets)
period = []
for i in inital :
	period.append(0)
while period.count(0)>0 :
	idx = 1
	curr = hash(planets)
	for i in range(len(curr)) :
		if(period[i]==0) and (curr[i]==inital[i]):
			period[i] = count
	#	iter += (hash)
	#if prev.count(iter) == 1 :
	#	break
	#prev.append(iter)
	count +=1
	#apply gravity
	for p in planets :
		rest = planets[idx:4]
		idx +=1
		for p2 in rest :
			p.gravity(p2)
	for p in planets :
		p.move()
#part a
energy = 0
for p in planets :
	pe = abs(p.x)+abs(p.y)+abs(p.z)
	ke = abs(p.vx)+abs(p.vy)+abs(p.vz)
	energy += pe*ke
print( "Energy: " + str(energy))
#part b
print( "Periods: " + str(period) )
sysPeriod = numpy.lcm.reduce(period)
print( "System Period: " + str( sysPeriod ) )