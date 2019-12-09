from bisect import bisect_left 

class pt3d:
	def __init__( self, x, y ):
		self.x = x
		self.y = y
		self.z = 0
	def __init__( self, x, y, z ):
		self.x = x
		self.y = y
		self.z = z
	def __eq__ ( self, p ):
		return self.x==p.x and self.y==p.y
	def __ne__ ( self, p ):
		return not (self==p)
	def distance( self):
		return abs(self.x)+abs(self.y*1.00001)
	def __lt__ ( self, p ):
		return self.distance()<p.distance()
	def __gt__ ( self, p ):
		return self.distance()>p.distance()
	def __le__ ( self, p ):
		return self==p or self.distance()<p.distance()
	def __ge__ ( self, p ):
		return self==p or self.distance()>p.distance()
	def __str__( self ):
		return "(" + str(self.x) + "," + str(self.y) + ")"
	def copy( self ):
		return pt3d(self.x,self.y,self.z)
	def getTransit(self):
		return self.z

def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1

traversed = []
inters = []
def day3a():
	inters.sort(key=pt3d.distance)  
	f = open("inters.txt", "w")
	for p in inters:
		 f.write( str(p)+", dist "+ str(p.distance()) +"\n" )
	f.close() 
def day3b():
	inters.sort(key=pt3d.getTransit)  
	f = open("inters.txt", "w")
	for p in inters:
		 f.write( str(p)+", Transit "+ str(p.getTransit()) +"\n" )
	f.close() 

f = open("input.txt", "r")
line = 0
for x in f:
	line+=1
	transit = 0
	traversed.sort(key=pt3d.distance)
	lastPt = pt3d( 0, 0, 0 )    
	cmds = x.split(',')
	print("NEW LINE")
	for c in cmds:
		if( len(c) < 2 ):
			continue
		print(c)
		dir = c[0]
		cnt = int(c[1:len(c)])
		list = ""
		for i in range(cnt):
			if(dir == 'R') :
				lastPt.x += 1
			elif(dir == 'L') :
				lastPt.x -= 1
			elif(dir == 'U') :
				lastPt.y += 1
			elif(dir == 'D') :
				lastPt.y -= 1
			lastPt.z += 1
			list = list + str(lastPt)
			has = 0
			if(line>1):
				has = BinarySearch(traversed,lastPt)
				if( has >= 0):
					it = lastPt.copy()
					it.z += traversed[has].z
					inters.append(it)
					print( str(lastPt) )
			else:
				traversed.append(lastPt.copy())

day3b()
