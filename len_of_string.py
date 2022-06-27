# 1. Write a Python program to calculate the length of a string.

# s1="My name is Pooja"
# print(len(s1))
############################

# def findlen(s1):
#     counter = 0
#     for char in s1:
#         counter+=1
#     return counter
# s1="My name is Pooja"
# print(findlen(s1))

#########################################

# def findlen(s1):
#      counter = 0
#      while s1[counter:]:
#          counter+=1
#      return counter
# s1="My name is Pooja"
# print(findlen(s1))
###############################################

def findLen(s1):
    if not s1:
        return 0
    else:

        s1=" ".join(str)
        x=s1.count(" ") +1

        return (x)


str = "geeks"
print(findLen(str))

