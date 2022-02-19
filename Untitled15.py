#!/usr/bin/env python
# coding: utf-8

# In[1]:


for x in range(2000,3201):
    if x% 7 == 0 and x%5 != 0:
        print(x, end = ',')
       


# In[2]:


first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
name = first_name+' ' +last_name
print(f"Actual_name: {name}")
print(f"Reverse_order: {name[::-1]}")


# In[3]:


import math

d = 12
r = 6
Vol_of_sphere = (4/3) * (math.pi) * (math.pow(6,3))
print(Vol_of_sphere)


# In[ ]:




