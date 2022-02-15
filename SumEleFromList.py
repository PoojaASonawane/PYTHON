list=[]

while True:
    n=input("Enter number")
    if len(n)!=0:
        list.append(n)
    else:
         break
total = 0
for num in list:
    total=total+int(num)
print(total)


