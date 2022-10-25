n=int(input())
words=input().split()        #convert input numbers into a list by space

for i in range(0,n):           #convert the numbers in the list into integers
    words[i]=int(words[i])

for j in range(1,n):        #insertion sort
    temp=0
    min=j-1
    for k in range(j,n):
        if words[min]>words[k]:
            temp=k
            k=min
            min=temp
    temp=words[j-1]
    words[j-1]=words[min]
    words[min]=temp
    
print(words[-1])      #print the maximum & second maximum
print(words[-2])
