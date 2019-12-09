

ints = [1,9,10,3,2,3,11,0,99,30,40,50]

def intcodes():
	pos = 0
	while pos < len(ints) :
		if(ints[pos] == 1):
			ints[ints[pos+3]] = ints[ints[pos+1]] + ints[ints[pos+2]]
			pos += 4
		elif (ints[pos] == 2):
			ints[ints[pos+3]] = ints[ints[pos+1]] * ints[ints[pos+2]]
			pos += 4
		elif (ints[pos] == 99):
			return True
			break
		else:
			print("Unknow value encountered")
			return False
			break
	return False
intcodes()
outstr = ""
for x in ints: 
	outstr += str(x)+','
print(outstr)

ints.clear()
inital = []
f = open("input.txt", "r")
for x in f:
	inital.append( int(x) )
for noun in range(100):
	for verb in range(100):
		ints = inital.copy()
		ints[1]=noun
		ints[2]=verb
		if( intcodes() ):
			if( ints[0] == 19690720 ):
				print( 'Found output Answer: ' + str(noun*100+verb) )
				exit(0)
			
