a = int (input ( " adad aval khod ra vared konid : " ))
b = int (input ( " adad dovom khod ra vared konid : " ))
x = 1
y = 1
n = 0
m = 0
# ***************************
while ( x <= a and x <= b ) :
    if ( a % x == 0 and b % x == 0 ) :
        s = x 
    x += 1
print ( f" BMM =  {s} " )
#****************************
while ( True ) :
    if ( x >= a or x >= b ) :
        if ( x % a == 0 and x % b == 0 ) :
            break
        x += 1
print ( f" KMM =  {x} " )
# ***************************
x = 1
while ( x <= a ) :
    if ( a % x == 0 ) :
        n += 1
    x += 1  
x = 1  
while ( x <= b ) :
    if ( b% x == 0) :
        m += 1
    x += 1
big = max (n , m)
if ( big == n ) :
    print ( f" Winner is {a} " ,"with" , big)
elif ( big == m ) :
    print ( f" Winner is {b} " ,"with" , big)
else : 
    print (" do adad shoma barabaran oskol !!! ")
# ***************************
# while ( True ) :
#     if ( int(a) % x <= 0 ) :
#         print ( x )
#     if ( int(b) % y <= 0 ) :
#         print ( y )
#     elif ( ( x <= int(a) and int(a) > int(b) ) or ( y <= int(b) and int(b) > int(a) ) ) :
#         break
#     y =+ 1
#     x =+ 1
# ***************************