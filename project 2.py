import random
a = random.randrange(1,1000000)
print (a)
a=str(a)
n = 0 
while (n<len(a)) :
    b=str(a[n])
    print(a[n], ':' ,int(a[n])*b)
    n+=1