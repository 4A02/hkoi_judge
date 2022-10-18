a=input()
b=input()
y1,m1,d1=a.split()    #split the inputs by space
y2,m2,d2=b.split()
y1=int(y1)            #change the data type of the input to integer
m1=int(m1)
d1=int(d1)
y2=int(y2)
m2=int(m2)
d2=int(d2)

if y1>y2:
    print('After')         #compare
elif y1<y2:
    print('Before')
else:
    if m1>m2:
        print('After')
    elif m1<m2:
        print('Before')
    else:
        if d1>d2:
            print('After')
        elif d1<d2:
            print('Before')
        else:
            print('Same')
