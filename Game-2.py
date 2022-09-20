import time
print (""""" Hello :) 
 Let\'s play hoop!!!!! 
  You Have 5 seconds for each turn! - Type * instead of hoop! \n """ )
a = input ( " Please insert hoop cycle length : " ) 
n = 1
def Timers () :
        c = 6 
        while ( c != 0 ) :
            print ( c )
            time.sleep(1)
            c -= 1               
while (True) :
    Timers ()
    b = input ()    
    if ( (n % int(a)) == 0 ) :
        print ( "hoop" ) 
    else :
        print (n)  
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
