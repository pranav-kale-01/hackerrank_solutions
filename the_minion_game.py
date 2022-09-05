def minion_game(string):
    string = string.upper()
    stuart_score, kevin_score = 0,0

    # your code goes here
    size = len( string )
    ind =0
    for i in s:
        #checking for vowels
        if( i=="A" or i=="E" or i=="I" or i=="O" or i=="U" ):
            kevin_score += (size - ind) 
        else: 
            stuart_score += (size - ind) 

        ind +=1

    if( kevin_score > stuart_score ):
        print( "Kevin", kevin_score, sep=" ") 
    elif( kevin_score == stuart_score ):
        print("Draw")
    else:
        print("Stuart", stuart_score, sep=" " )

if __name__ == '__main__':
    s = input()
    minion_game(s)