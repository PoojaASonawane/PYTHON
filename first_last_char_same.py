i=0
t1=('abc','xy','aba','1221')
for x in t1:
    if len(x)>2 and x[0]==x[-1]:
        print(x)
        i=i+1
print(i)