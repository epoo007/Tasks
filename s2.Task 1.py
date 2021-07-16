#!/usr/bin/env python
# coding: utf-8

# In[1]:


i1=0
while(i1==0):
    a=[]
    n=input("Enter number of elements:")
    if(n.isdigit()==True):
        i2=0
        i1+=1
        print("Enter the elements")
        while(i2<int(n)):
            b=input()
            if(b.isdigit()==True):
                a.append(int(b))
                i2+=1
            else:
                print("wrong input ")
        print(a)
    else:
        print("Wrong input try again")
i2=0
while(i2==0):
    print("1.To remove a specific number ")
    print("2.To show the list ")
    print("3.To exit ")
    x=input("enter the operation number: ")
    if(x=="1"):
        i3=0
        while(i3==0):
            print("to return back type x")
            b=input("enter the number you want to delete: ")
            if(b.isdigit()==True and a.count(int(b))>0):
                i3=1
                while(a.count(int(b))>0):
                    a.remove(int(b))
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
        
        
