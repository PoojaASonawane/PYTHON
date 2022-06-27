# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
####################################################################################################

# s1="google.com"
# dic={}
# for char in s1:
#     dic[char]=dic.get(char,0)+1
# print(str(dic))
###############################################
# s1="google.com"
# dic={}
# for char in s1:
#     if char in dic:
#         dic[char]+=1
#     else:
#         dic[char]=1
# print(dic)
#####################################################
# s1="google.com"
# x={i : s1.count(i) for i in set(s1)}
# print(str(x))
##################################################

# s1=input("Enter the string")
# d1={}
# for x in s1:
#     d1[x]=s1.count(x)
#     #d1[x]=a
# print(d1)

#######################################################

