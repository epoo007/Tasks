#!/usr/bin/env python
# coding: utf-8

# In[1]:
i=0
while(i==0):
    try:
        a=float(input("enter the first number: "))
        i=1
    except:
        print("try again")
        i=0
i=0
while(i==0):
    try:
        b=float(input("enter the second number: "))
        i=1
    except:
        print("try again")
        i=0
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




