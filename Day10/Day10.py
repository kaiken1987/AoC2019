import math

field = [
	"##.###.#.......#.#....#....#..........#.",
	"....#..#..#.....#.##.............#......",
	"...#.#..###..#..#.....#........#......#.",
	"#......#.....#.##.#.##.##...#...#......#",
	".............#....#.....#.#......#.#....",
	"..##.....#..#..#.#.#....##.......#.....#",
	".#........#...#...#.#.....#.....#.#..#.#",
	"...#...........#....#..#.#..#...##.#.#..",
	"#.##.#.#...#..#...........#..........#..",
	"........#.#..#..##.#.##......##.........",
	"................#.##.#....##.......#....",
	"#............#.........###...#...#.....#",
	"#....#..#....##.#....#...#.....#......#.",
	".........#...#.#....#.#.....#...#...#...",
	".............###.....#.#...##...........",
	"...#...#.......#....#.#...#....#...#....",
	".....#..#...#.#.........##....#...#.....",
	"....##.........#......#...#...#....#..#.",
	"#...#..#..#.#...##.#..#.............#.##",
	".....#...##..#....#.#.##..##.....#....#.",
	"..#....#..#........#.#.......#.X#..###..",
	"...#....#..#.#.#........##..#..#..##....",
	".......#.##.....#.#.....#...#...........",
	"........#.......#.#...........#..###..##",
	"...#.....#..#.#.......##.###.###...#....",
	"...............#..#....#.#....#....#.#..",
	"#......#...#.....#.#........##.##.#.....",
	"###.......#............#....#..#.#......",
	"..###.#.#....##..#.......#.............#",
	"##.#.#...#.#..........##.#..#...##......",
	"..#......#..........#.#..#....##........",
	"......##.##.#....#....#..........#...#..",
	"#.#..#..#.#...........#..#.......#..#.#.",
	"#.....#.#.........#............#.#..##.#",
	".....##....#.##....#.....#..##....#..#..",
	".#.......#......#.......#....#....#..#..",
	"...#........#.#.##..#.#..#..#........#..",
	"#........#.#......#..###....##..#......#",
	"...#....#...#.....#.....#.##.#..#...#...",
	"#.#.....##....#...........#.....#...#..."
	]
asteroids = []
wid = len(field[0])
hei = len(field)
class frac:
	epsilon = 0.0001
	def __init__(self,num,denom):
		self.num = -num
		self.denom = denom
		self.ang = math.atan2(denom,-num) 
		self.dist = math.hypot(num,denom)
		if(self.ang<0): 
			self.ang += math.pi*2
	def __eq__(self, value):
		if( (self.num>0)!=(value.num>0) or (self.denom>0)!=(value.denom>0) ) :
			return False
		if( (self.num==0) and (value.num==0) ) :
			return True
		if( (self.denom==0) and (value.denom==0) ) :
			return True
		if( (self.num==0) and (value.num==0) ) :
			return False
		if( (self.denom==0) or (value.denom==0) ) :
			return False
		return abs(self.num/self.denom - value.num/value.denom)<frac.epsilon
	def __lt__(self, value):
		return self.dist<value.dist
	def __le__(self, value):
		return self.dist()<=value.dist()
	def __gt__(self, value):
		return not (self<=value)
	def __ge__(self, value):
		return not (self<value)
	def __str__(self):
		return "{}/{} {}".format(self.num,self.denom,self.ang)

class point:
	def __init__(self, x,y):
		self.x = x
		self.y = y
		
def scan(origin):
	tested = []
	for pt in asteroids :
		dx = pt.x-origin.x
		dy = pt.y-origin.y
		if(dx == 0 and dy == 0): continue
		dist = frac(dx, dy)
		cnt = tested.count(dist)
		if(cnt==0) :
			tested.append(dist)
	return len(tested)

def scan2(origin, idx):
	tested = []
	for pt in asteroids :
		if(pt == origin): continue
		dx = pt.x-origin.x
		dy = pt.y-origin.y
		if(dx == 0 and dy == 0): continue
		dist = frac(dy, dx)
		try:
			idx = tested.index(dist)
		except:
			idx = -1
		if(idx==-1) :
			tested.append(dist)
		elif(dist<tested[idx]):
			tested[idx] = dist
	tested.sort(key=lambda ast: ast.ang)
	for f in tested : print( str(f) )
	if(len(tested)<idx):
		return frac(0,0)
	return tested[idx]

best = point(31,20)
bestCnt = 319
#look = scan2( best, 199 )

for y in range(hei):
	for x in range(wid) :
		if(field[y][x]=='.') : continue
		asteroids.append(point(x,y))
def findBest():
	idx = 0
	for pt in asteroids :
		cnt = scan( pt )
		idx += 1
		if( cnt > bestCnt) :
			best = pt
			bestCnt = cnt 
		print( "%d/%d" % (idx,len(asteroids)) )
field[best.y] = field[best.y][0:best.x]+'*'+field[best.y][best.x+1:-1]
print(field[best.y])
print( "Best Point %d,%d with %d"% (best.x, best.y, bestCnt) )

#print( "test atan2: ", str(math.atan2(0,5)))

look = scan2( best, 199 )
print( "200th Point %d,%d"% (look.num+best.x, look.denom+best.y) )
