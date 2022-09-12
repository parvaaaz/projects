import random
x1 =(random.randrange(1, 10))
x2 =(random.randrange(1, 10))
y1 =(random.randrange(1, 10))
y2 =(random.randrange(1, 10))
print (x1,y1,x2,y2)
while (x1!=x2 or y1!=y2) :
    if (x1<x2):
        x1 =(random.randrange(x1+1, 10))
    elif (x1>x2):
        x1 =(random.randrange(1, x1-1))
    if (y1<y2):
        y1 =(random.randrange(y1+1, 10))
    elif (y1>y2):
        y1 =(random.randrange(1, y1-1))
    print (x1,y1,x2,y2)
print ('noice')

