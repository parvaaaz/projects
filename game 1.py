import random
a = (random.randrange(1,10))
n = 0
while ( n < 5 ) :
    b = input ( "Adad Khod Ra Vared Konid : " )
    if ( a != b and n == 4 ) : 
        print ( " You Failed " )
    elif ( int (a) < int (b) ) :
        print (" Lower ")
    elif ( int (a) > int (b) ) :
        print (" Higher ")
    elif ( int (a) == int (b) ) :
        print ( " You Succed Horay " )
        break
    n += 1
