a = int(input (" adad khod ra vared konid (1,10) plz : " ))
n = 1
while ( n <= a ) :
    print ( n * "*" )
    n += 1
n = 1
if ( a % 2 == 0) :
    print ("")
    while ( n <= (a//2) ) :
        print ( n * "**" )
        n += 1
else :
    while ( n <= a ) :
        print ( n * "*" )
        n += 2
        