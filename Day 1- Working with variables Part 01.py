#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")


# ### String Manipulation and Code Intelligence

# In[2]:


print("Hello world!\nHello world!\nHello world!")


# In[3]:


print("Hello"+" "+"Chinedu")


# ###### Debugging Exercise

# In[4]:


print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


# #### Python Input Function

# In[5]:


# input() will get user input in console
# Then print() will print the word "Hello" and the user input
print("Hello " + input("What is your name?") + "!")


# ##### Input Exercise: Write a program that prints the number of characters in a user's name.

# In[6]:


# input() will get user input in console
# len prints the number of characters in the string.
print(len(input("What is your name? ")))


# ### Final Project

# In[7]:


#  Automatically generates a band name
print("Welcome to the Band Name Generator")
city=input("What's the name of the city did you grew up in?\n")
pet_name=input("What's your pet's name?\n")
print("Your band name could be "+city+" "+pet_name)

