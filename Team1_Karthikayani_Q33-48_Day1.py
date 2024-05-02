#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Q.35.find the way to reverse string for given input
#(eg: input : This hackathon is about cardiac outcomes: outcomes cardiac about is hackathon This)

user_input = input("Enter string for reversal:")
reversed_string = user_input[::-1]
print("Reversed string is: " + reversed_string)


# In[5]:


#Q.38.find the length of Tuple for any given input (Hint: Input a string from user )

user_input = input("Enter string :")
user_tuple = tuple(user_input)
print("Output tuple:", user_tuple)
print("Length of entered tuple:", len(user_tuple))


# In[2]:


#Q.48.Using loops, create a multiplication table for the number 7

multiplier = 7
row = int(input("Enter number of rows for 7 multiplication table:"))

for i in range(1, row+1):
    product = multiplier * i
    print(f"{multiplier} * {i} = {product}")    


# In[ ]:




