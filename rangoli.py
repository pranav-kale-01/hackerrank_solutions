def get_rangoli_pattern( size, ind ):
    width = (size-1)*4 + 1
        
    # finding the half of width 
    

    # calculating the step for placing the characters 
    step = 1 / ( int( width/ 4.0 ) )

    l = ['-']*width

    # placing the values according to size 
    for j in range(0, ind):
        temp = int( width/2 ) * (1- j*step)
        temp2 = int( width/2 ) * (1+ j*step)

        l[ int( round( temp ) ) ]  = chr( 97 + (size - (ind-j)) )
        l[ int( round( temp2 ) ) ] = chr( 97 + (size  - (ind-j)) )

    for j in l: 
        print(j, end="")
    print()

def print_rangoli(size):
    for i in range(1,size+1):
        get_rangoli_pattern( size, i )            


    for i in range( size-1, 0, -1):
        get_rangoli_pattern(size, i)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)