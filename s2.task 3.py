#!/usr/bin/env python
# coding: utf-8

# In[1]:


i=0
while(i==0):
    a=input("enter the first number: ")
    dotcount=0
    numcount=0
    i2=0
    for character in a:
        if(ord(character)==46):
            dotcount+=1
            if(dotcount==2):
                print("wrong input try again")
                i2=1
        elif(ord(character)>=48 and ord(character)<=57):
            numcount+=1
        else:
            print("wrong input try again")
            i2=1
    if(i2==1):
        i=0
    elif(i2==0 and numcount>0):
        i=1
a=float(a)
i=0
while(i==0):
    b=input("enter the second number: ")
    dotcount=0
    numcount=0
    i2=0
    for character in b:
        if(ord(character)==46):
            dotcount+=1
            if(dotcount==2):
                print("wrong input try again")
                i2=1
        elif(ord(character)>=48 and ord(character)<=57):
            numcount+=1
        else:
            print("wrong input try again")
            i2=1
    if(i2==1):
        i=0
    elif(i2==0 and numcount>0):
        i=1
b=float(b)
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




