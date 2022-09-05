from itertools import permutations
string, k = input().split(" ")
l = list(string)
l.sort()
[ print( "".join(i) ) for i in set( permutations( l, int( k ) ) ) ] 