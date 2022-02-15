list1=[10,20,30]
list2=list1.copy()
list2[0]=123
print(id(list1))
print(id(list2))
print(list1)
print(list2)
