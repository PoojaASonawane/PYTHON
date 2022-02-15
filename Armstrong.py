a=input("Enter any number")
a=int(a)    #153
b=a//100    #1
c=a%100     #53
d=c//10     #5
e=c%10      #3
f=b**3 + d**3 + e**3
print(f)
if f==a:
    print("Armstrong")
else:
    print("Not Armstrong")

