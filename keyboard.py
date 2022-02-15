words="1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
s1=input("Enter String")
arr=s1.split(" ")
s2=" "
for x in arr:
    for y in x:
        p=words.index(y)
        p=p-1
        s2+=words[p]
    s2+=" "
print(s2)



