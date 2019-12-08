
class pt2d:
    def __init__( self, x, y ):
        self.x = x
        self.y = y
    def __cmp__ ( self, p ):
        bool = self.x==p.x and self.y==p.y
        print( "cmp is " + str(bool) )
    def toString( self ):
        return "(" + str(self.x) + "," + str(self.y) + ")"

traversed = []
inters = []

f = open("input.txt", "r")
sum = 0;
for x in f:
    lastPt = pt2d( 0, 0 )    
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
            list = list + lastPt.toString()
            has = 0
            for p in traversed :
                if( p == lastPt):
                    has = 1
                    break;            
            print( "Count for " + lastPt.toString() +" : ", traversed.count(lastPt))
            if( has < 1):
                traversed.append(lastPt)
                print( lastPt.toString() )
            else:
                inters.append(lastPt)
        print( list )
                
f = open("inters.txt", "w")
for p in inters:
    f.write( p.toString() )
