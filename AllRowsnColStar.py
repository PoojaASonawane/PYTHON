""""
for i in range(1,5):
    for j in range(1,5):
        print("*",end='')
    print(" ")
    """
"""
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end='')
    print("")
    """
"""
k=1
for i in range(1,6):
    for j in range(1,i+1):
        print(k,end='')
        k=k+1
    print(" ")
"""
a=1
b=5
for i in range(1,6):
    for j in range(1,6):
        if a==i and b==j:
            print("*", end='')
            a=a+1
            b=b-1
        elif i==j:
            print("*", end='')
        else:
            print(" " ,end='')
    print()


