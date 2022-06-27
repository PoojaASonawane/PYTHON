###############count()###############
#s1="This is demo. This is my string handling program"
# x=s1.count("is")
# print(x)
# x=s1.count('is',4)
# print(x)
##############find()##############
# x=s1.find('is')
# print(x)
# x=s1.find('is',x+1)
# print(x)
##################################
# x=-1
# while True:
#     x=s1.find('is',x+1)
#     if x==-1:
#         break
#     print(x)
##############split()########################
# s1="a,b,hello,d,e,f,g"
# arr=s1.split('*')
# print(arr)
# s2="This is demo"
# arr1=s2.split(" ")
# print(arr1)
##############startswith() and endswith()###########################
# s1="Hello World"
# x=s1.startswith('Hello')
# print(x)
# y=s1.endswith('World')
# print(y)
# #################index()###############################
# s1="This is demo.This is first string"
# # print(len(s1))
# # x=s1.index('IS')
# # print(x)
# x=s1.find('Is')
# print(x)
##################center() ljust()  rjust()#############################
# s1="Hello World"
# print(s1.center(50,'*'))
# print(s1.ljust(50,'*'))
# print(s1.rjust(50,'*'))
##################lstrip() rstrip() strip()########################
# s1=" Hello World "
# print(len(s1))
# s1=s1.lstrip()
# print(len(s1))
# s1=s1.rstrip()
# print(len(s1))
# s1=s1.strip()
# print(len(s1))
###############join()###########################
mylist=['Hello','World','This','is','demo']


def myjoin(mylist):
   s1=" "
   for x in mylist:
       s1 += " " + x

   return(s1.strip())
####################################################
#mylist=['Hello','World','This','is','demo']
# s1=''
# for x in mylist:
#     s1+=""+x
# print(s1.strip())
##################################################
#mylist=['Hello','World','This','is','demo']
#s1=" ".join(mylist)
#s2=myjoin(mylist)
#print(s1)
#print(s2)
##################replace()############################
# s1="This is demo. This is string program."
# print(s1)
# s1=s1.replace('is','IS')    #replace all instances
# print(s1)
# s1=s1.replace('is','IS',2)   #replace 2 instances
# print(s1)
######################################################
#s1="This is DEMO"
# print(s1.capitalize())
# print(s1.lower())
# print(s1.upper())
#print(s1.swapcase())
#print(s1.title())



