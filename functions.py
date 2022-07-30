#!/usr/bin/env python
# coding: utf-8

# task 7
# The included code stub will read an integer,n, from STDIN.
# 
# Without using any string methods, try to print the following:
# 
# 1,2,3,....
# Note that "...." represents the consecutive values in between.
# 
# Example
# n=5
# Print the string 12345.

# In[8]:


if __name__ == '__main__':
    n = int(input())
    for i in range (n):
        print(i+1,end="")
        

