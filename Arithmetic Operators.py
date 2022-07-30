#!/usr/bin/env python
# coding: utf-8

# task 3
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
# 
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Example
# a=3
# b=5
# 
# Print the following:

# In[1]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    add=a+b
    diff=a-b
    prod=a*b
    
print(add)
print(diff)
print(prod)

