from itertools import product
l = list( product( input().split(" "), input().split(" ")  ) ) 
[ print( "(", i , ", ", j, ")", sep="", end=" " ) for i,j in l ]