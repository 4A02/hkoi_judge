x,y=input().split()    #let x and y separate by space 
a=int(x)        #change string x and y into integers
b=int(y)

if b>a:             #let a be the greater number in order to apply Euclid's algorithm to find HCF
    temp=b
    b=a
    a=temp

remain=-1
while remain!=0:      #Euclid's algorithm
    remain=a%b
    a=b
    b=remain
print(a)        #result HCF
print(round(int(x)*int(y)/a))   #result LCM
