from collections import defaultdict

n,m = [ int(x) for x in input().split(" ") ]
d = defaultdict(list)
ind=0

for i in range(n):
    d[input()].append( str(ind) )
    ind+=1

for i in range(m):
    val = input()
    if( len( d[val] ) == 0 ):
        print("-1")
    else:
        print( ' '.join( d[val] ) )