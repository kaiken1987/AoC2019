
class obj :
	def __init__(self, parent=""):
		self.sats = []
		self.dist = -1
		self.weight = 0
		self.parent = parent

orbits = {"COM": obj()}

def depth( name ) :
	if( name == "") :
		return 0
	elif( name not in orbits) :
		return 0
	else :
		return depth(orbits[name].parent) +1
	
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
	else :
		orbits[sat].parent = center
	orbits[center].sats.append(sat)
	
print("Number of Objects: " + str(len(orbits)))
direct = 0
indirect = 0
for name, x in orbits.items() :
	direct += len(x.sats)
	x.depth = depth(x.parent)
	indirect += x.depth
print("Direct Orbits: " + str(direct))
print("Indirect Orbits: " + str(indirect))
