a=int(input("Enter a number")) #11
b=a//10  #1
c=a%10   #1
f=b+c*10
if f==a:
    print("Palindrome")
else:
    print("Not Palindrome")