#12. Write a Python program to count the occurrences of each word in a given sentence.

# def count(str,word):
#     x=(str.split())
#     return x.count(word)
# str="My name is pooja . My hobby is coding"
# word="pooja"
# print(count(str,word))

#####################################################
s1=input("Enter the string")
a=s1.split(' ')
s2=[]
print(a)
for x in a:
    if x not in s2:
        d1=a.count(x)
        print(x,":",d1)
        s2.append(x)

