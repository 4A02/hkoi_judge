num=int(input())    #input the number of line
n=1      #n=number should be printed
for i in range(1,num+1):
    for j in range(1,num+1):
        print(n,end=' ')
        n+=4
    n-=4       #reduce n by 4 so it can become the last integer from the line above
    print()
