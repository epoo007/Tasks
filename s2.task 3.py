#!/usr/bin/env python
# coding: utf-8

# In[7]:


i=0
while(i==0):
    a=input("Enter the first number:")
    if(a.isdigit()==True):
        i=1
        a=int(a)
    else:
        print("wrong input try again")
i=0
while(i==0):
    b=input("Enter the second number:")
    if(b.isdigit()==True):
        i=1
        b=int(b)
    else:
        print("wrong input try again")
i=0
while(i==0):
    c=input("enter the operation as + , - ,/ ,*:")
    if(c=="+"):
        print(a,"+",b,"=",a+b)
        i=1
    elif(c=="-"):
        print(a,"-",b,"=",a-b)
        i=1
    elif(c=="/"):
        print(a,"/",b,"=",a/b)
        i=1
    elif(c=="*"):
        print(a,"*",b,"=",a*b)
        i=1
    else:
        print("wrong input")




