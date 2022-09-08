num=int(input())
i=1     #i is the number of row
k=1     #k is maximum number can be print in each row
j=1     #j is the number to be print
while k<=num:
    while j<=num**2 and i<=k:    #num**2 is the maximum number to be print
        print(j,end=" ")     #print a row of number without changing row
        j+=1
        i+=1    #count how many numbers have been print in a row
    i=1    #reset i to 1
    print()    #ready to start a new row
    k+=1    #increase the maximum number can be print in each row by 1

#finish the first half of triangle (where k is equal to inputed number+1)

k-=2    #the next line to be print is less than inputed number by 2

while k>0:
    while j<=num**2 and i<=k:
        print(j,end=" ")
        j+=1
        i+=1
    i=1
    print()
    k-=1
