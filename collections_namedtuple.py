from collections import namedtuple
n, Student = int( input() ), namedtuple( 'Student', input() )
print( sum( [float( Student( *input().split() ).MARKS ) for i in range(n)] )/n )