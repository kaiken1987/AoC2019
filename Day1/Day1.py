import math

def getFuelReqPartOne( mass ):
	fuel = math.floor(mass/3)-2
	if fuel < 0:
		return 0
	else:
		extraFuel = getFuelReq( fuel )
		fuel = fuel + extraFuel
		return fuel
def getFuelReq( mass ):
	fuel = (mass//3)-2
	if fuel < 0:
		return 0
	else:
		extraFuel = getFuelReq( fuel )
		fuel = fuel + extraFuel
		return fuel
	
print( 'Mass 4 requires ' + str(getFuelReq( 4 )) )
print( 'Mass 12 requires ' + str(getFuelReq( 12 )) )
print( 'Mass 14 requires ' + str(getFuelReq( 14 )) )
print( 'Mass 1969 requires ' + str(getFuelReq( 1969 )) )
print( 'Mass 100756 requires ' + str(getFuelReq( 100756 )) )

f = open("input.txt", "r")
sum = 0;
for x in f:
	sum = sum + getFuelReq( int(x) )
print( 'Total fuel req ' + str( sum ) )
