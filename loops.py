#!/usr/bin/env python
# coding: utf-8

# task 5
# The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .
# 
# Example
# 
# The list of non-negative integers that are less than n=3  is [123] . Print the square of each number on a separate line.

# In[4]:


if __name__ == '__main__':
    n = int(input())
    for s in range(0, n):
        print(s ** 2)

