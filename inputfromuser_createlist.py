list=[]
while True:
    n=input("Enter number")
    if len(n)!=0:
        list.append(n)
    else:
         break

print(list)
temp=[]
for num in list:
   if num not in temp:
       x = (list.count(num))
       print(num, x)
       temp.append(num)


        






