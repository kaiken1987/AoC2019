
rangeMin = 387638
rangeMax = 919123

validCnt = 0

def validTest(password) :
	string = str(password)
	#digits never decrease
	for i in range(len(string)-1) :
		if string[i]>string[i+1] :
			return False
	#contains at least one set of doubles
	hasDbl = False
	i = 0
	while i <len(string)-1 :
		if string[i]==string[i+1] :
			#check for invalid 3x or 5x
			cnt = string.count(string[i])
			if( cnt == 2 ):
				return True
			i+=cnt
		else:
			i+=1
	return False
tests = [112233, 123444, 111122, 333445, 444555, 667777, 233334, 233345, 223334, 112345]
print( "Tests cases")
for x in tests:
	res = validTest(x)
	print( str(x) + " is " + str(res) )

for i in range(rangeMin, rangeMax) :
	if validTest( i ) :
		validCnt+=1
	
print( "Possible Passwords: "+str(validCnt))
