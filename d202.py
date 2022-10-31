import math
n=int(input())
s=round(math.sqrt(n))
factors=set()         #let factors be a set in order to sort them in increasing order conveniently

for i in range(1,s+2):           #use the method of factorization
    if n%i==0:
        factors.add(i)
        factors.add(round(n/i))
factors=tuple(sorted(factors))      #convert factors into tuple to print them one by one

for j in range(0,len(factors)):
    print(factors[j])
