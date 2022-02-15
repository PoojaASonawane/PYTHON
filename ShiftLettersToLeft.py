
temp=[]
s=input("Enter String")
print(s)
arr1=list(s)
print(arr1)


temp1=[]
for x in arr1:
    if (ord(x)>=97 and ord(x)<=122):
        # n=(arr1.append(x))
        print(x)
        temp.append(x)
    else:
        temp1.append(x)

s1="".join(temp)
s2="".join(temp1)
print(s1+s2)
#######################################################
s1=input("Enter String")
a=list(s1)
s1=""
s2=""
for ele in a:
    x=ord(ele)
    if((x>=65) and x<=90) or (x>=97 and x<=122):
        s1=s1+ele
    else:
        s2=s2+ele
print(s1+s2)
#############################################





