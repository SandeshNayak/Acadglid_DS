
# coding: utf-8

# In[ ]:


#Write a program which will find all such numbers which are divisible by 7 but are not a multiple
#of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
#comma-separated sequence on a single line.


# In[13]:


number=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5!=0):
        number.append(str(x))
print (','.join(number))  


# In[ ]:


#Write a Python program to accept the user's first and last name and then getting them printed in
#the the reverse order with a space between first name and last name.


# In[39]:


firstName=input("Enter first Name: ")
LastName=input("Enter Last Name:")
print(firstname[::-1] + " " + lastname[::-1])


# In[ ]:



#Write a Python program to find the volume of a sphere with diameter 12 cm.


# In[34]:



PI = 3.14
diameter = 12
radius = diameter / 2

Volume = (4 / 3) * PI * radius * radius * radius

print("\n The Volume of a Sphere = %.2f" %Volume)


# In[ ]:


#Write a program which accepts a sequence of comma-separated numbers from console and generate a list.


# In[59]:



list=[]
data=input("Enter a sequence of number seperated by comma: ")
list.append(data)
print('Generating a list......')
list


# In[ ]:


#Write a Python program to reverse a word after accepting the input from the user.


# In[63]:



data=input("Enter the number to print in reverse order")
print(data[::-1])


# In[97]:


h=['WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens']
h


# In[102]:


String1=str(h)


# In[103]:


String1


# In[104]:


type(String1)


# In[111]:


String1[:25]

