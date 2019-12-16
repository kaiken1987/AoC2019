
class obj :
	def __init__(self, parent=""):
		self.sats = []
		self.dist = -1
		self.weight = 0
		self.parent = parent

orbits = {"COM": obj()}

def trace( name, depth ):
	if name not in orbits:
		print( name + "not found")
		return 1
	cur = orbits[name]
	cur.weight = 1
	cur.dist = depth
	for x in cur.sats :
		cur.weight += trace(x, depth+1)
	return cur.weight
	
f = open("input.txt", "r")
for x in f:
	objs = x.split(')')
	if(len(objs) != 2):
		break
	center = objs[0]
	sat = objs[1].split('\n')[0]
	if not (center in orbits) :
		orbits[center] = obj()
	if not (sat in orbits) :
		orbits[sat] = obj(center)
	orbits[center].sats.append(sat)
	
print("Number of Objects: " + str(len(orbits)))

orbitCnt = trace("COM", 0)
print("Orbits: " + str(orbitCnt))
