mylist=[]
choice="yes"
count=0
while choice=="yes":
    n = int(input("Enter numbers"))
    mylist.append(n)
    choice=input("Do you want to continue?(yes|no)")
    count+=1
    if choice=="no":
        break
print(mylist)
temp=[]
for num in mylist:
    if num not in temp:
        x = (mylist.count(num))
        print(num, x)
        temp.append(num)



