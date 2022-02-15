ch=input("Enter chracter")
x=ord(ch)
if x>65 and x<=90:
    print("capital")
elif x>=97 and x<=122:
    print("Small")
elif x>=48 and x<=57:
    print("Digital")
else:
    print("I don't know this character")
    print("End")