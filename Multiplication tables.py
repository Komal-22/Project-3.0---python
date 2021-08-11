#!/usr/bin/env python
# coding: utf-8

# # Tables from 1 to 12

# In[1]:


# tried this first 

for value in range(1,13):
    for table in range(1,11):
        print (" {number2} * {number1} = {num3}".format(number1 = table,number2 = value, num3 = table * value ))
    value = value + 1
    print("********")


# In[3]:


#then this below is the optimized code after attending lecture also of the number entered as input

a = int(input())
i = 1
while (i <= 12):
    print(i * a)
    i = i + 1


# In[ ]:




