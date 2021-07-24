#!/usr/bin/env python
# coding: utf-8

# In[1]:


i1=0
while(i1==0):
    a=[]
    n=input("Enter number of elements:")
    if(n.isdigit()==True):
        i1=1
print("Enter the elements")
i2=0
while(i2<int(n)):
    b=input()
    dotcount=0
    numcount=0
    alphacount=0
    for character in b:
        if(ord(character)==46):
            dotcount+=1
        elif(ord(character)>=48 and ord(character)<=57):
            numcount+=1
        else:
            alphacount+=1
    if(alphacount>0):
        b=str(b)
    elif(dotcount==0 and numcount>=1):
        i=0
        while(i==0):
            print("i.input as int")
            print("f.input as float")
            print("s.input as str")
            c=input()
            if(c=='i'):
                b=int(b)
                i=1
            elif(c=='s'):
                b=str(b)
                i=1
            elif(c=='f'):
                b=float(b)
                i=1
            else:
                print("wrong input try again")
    elif(dotcount==1 and numcount>1):
        i=0
        while(i==0):
            print("f.input as float")
            print("s.input as str")
            c=input()
            if(c=='f'):
                b=float(b)
                i=1
            elif(c=='s'):
                b=str(b)
                i=1
            else:
                print("wrong input try again")
    else:
        b=str(b)
    i2+=1
    a.append(b)
print(a)
i2=0
while(i2==0):
    print("1.To remove a specific data ")
    print("2.To show the list ")
    print("3.To exit ")
    x=input("enter the operation number: ")
    if(x=="1"):
        i3=0
        while(i3==0):
            print("to return back type x")
            b=input("enter the data you want to delete: ")
            dotcount=0
            numcount=0
            alphacount=0
            for character in b:
                if(ord(character)==46):
                    dotcount+=1
                elif(ord(character)>=48 and ord(character)<=57):
                    numcount+=1
                else:
                    alphacount+=1
            if(alphacount>0):
                b=str(b)
            elif(dotcount==0 and numcount>=1):
                i=0
                while(i==0):
                    print("i.input as int")
                    print("f.input as float")
                    print("s.input as str")
                    print("x.to return back")
                    c=input()
                    if(c=='i'):
                        b=int(b)
                        if(a.count(b)>0):
                            i=1
                        else:
                            print("wrong input or the number doesn't exsist try again")
                    elif(c=='s'):
                        b=str(b)
                        if(a.count(b)>0):
                            i=1
                        else:
                            print("wrong input or the number doesn't exsist try again")
                    elif(c=='f'):
                        b=float(b)
                        if(a.count(b)>0):
                            i=1
                        else:
                            print("wrong input or the number doesn't exsist try again")
                    elif(c=='x'):
                        i=1
                    else:
                        print("wrong input try again")
            elif(dotcount==1 and numcount>1):
                i=0
                while(i==0):
                    print("f.input as float")
                    print("s.input as str")
                    print("x.to return back")
                    c=input()
                    if(c=='f'):
                        b=float(b)
                        if(a.count(b)>0):
                            i=1
                        else:
                            print("wrong input or the number doesn't exsist try again")
                    elif(c=='s'):
                        b=str(b)
                        if(a.count(b)>0):
                            i=1
                        else:
                            print("wrong input or the number doesn't exsist try again")
                    elif(c=='x'):
                        if(a.count(b)>0):
                            i=1
                        else:
                            print("wrong input or the number doesn't exsist try again")
                    else:
                        print("wrong input try again")
            else:
                b=str(b)
            if(a.count(b)>0):
                i3=1
                while(a.count(b)>0):
                    a.remove(b)
            elif(b=="x"):
                i3=1
            else:
                print("wrong input or the number doesn't exsist try again")
    elif(x=="2"):
        print("the list is: ",a)
    elif(x=="3"):
        i2=1
    else:
         print("wrong input try again")
        
        
