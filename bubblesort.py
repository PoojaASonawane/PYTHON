mylist=[8,7,6,5,4,3,2,1]
for i in range(len(mylist)-1):
    for j in range(len(mylist)-1):
        if mylist[j]>mylist[j+1]:
            t=mylist[j]
            mylist[j]=mylist[j+1]
            mylist[j+1]=t
print(mylist)