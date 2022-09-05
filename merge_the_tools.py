def merge_the_tools(string, k):
    l = []
    size = len(string)

    for i in range(int(size/k)):
        l.append( "".join( set( string[ i * (k) : (i+1) * (k) ] ) ) )

    [ print( i) for i in l ]

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)