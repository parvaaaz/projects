print ("\n \n Hello :) \n Let\'s play hoop!!!!! \n You Have 5 seconds for each turn! - Type * instead of hoop! \n " )
a = input ( " Please insert hoop cycle length : " ) 
n = 1
while (True) :
    if ( (n % int(a)) == 0 ) :
        print ( "hoop" ) 
    else :
        print (n)
    b = input ()
    try : 
        if ( int (b) != (n+1)) : 
            break
    except :
        while (False) :
            print (1)
    if ( (  (n+1) % int(a)) == 0 and b != ("*") ) :
        break
    if ( (  (n+1) % int(a)) != 0 and b == ("*") ) :
        break
    n += 2
print (" You have Failed!!! ")
