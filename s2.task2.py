#!/usr/bin/env python
# coding: utf-8

# In[1]:


i1=0
while(i1==0):
    i2=0
    print("1.Show the ascii of letter")
    print("2.Show the letter of ascii")
    print("3.To exit")
    a=input("Enter operation number: ")
    if(a=="1"):
        while(i2==0):
            b=str(input("Enter the letter: "))
            if(len(b)==1):
                print("The ascii code of",b,"is",ord(b))
                i2+=1
                i3=0
                while(i3==0):
                    z=input("Do you want to do another operation ?? y/n ")
                    if(z=="y"):
                        i2=0
                        i3=1
                    elif(z=="n"):
                        i2=1
                        i3=1
                    else:
                        i3=0
            else:
                print("You entered more than 1 letter")
    elif(a=="2"):
        i2=0
        while(i2==0):
            b=input("Enter the ascii code:")
            if(b.isdigit()==True):
                print("The letter of ",int(b),"is",chr(int(b)))
                i3=0
                while(i3==0):
                    z=input("Do you want to do another operation ?? y/n ")
                    if(z=="y"):
                        i2=0
                        i3=1
                    elif(z=="n"):
                        i2=1
                        i3=1
                    else:
                        i3=0
            else:
                print("wrong input try again")
                i2=0
        
    elif(a=="3"):
        i1=1
    else:
        print("Error the operation you entred does not exsist try another number")



