Probability is often defined as the frequency of something occuring provided a certain sample size

We are presented the following statistical problem: what is the probability that I will encounter a red light when I
reach an intersection exactly 100 times. What is the probability that I won't get a red light?

Once we construct a simple mathematical model, we find that if we encounter an intersection exactly 100 times, the probability of encoutering a red light is 16.67 percent; the chances of not encoutering a red light is 83.33 percent.

In addition, four other programs are listed: the first demonstrates the methodology behind superclasses; the second showcases the power of polymorphism; the third examines the reasoning behind static and class methods in Pythonic object-orientated-programming; and the fourth examines multiple resolution order.


#!/usr/bin/python3

class Light(object):
    'This class determines the probability of getting a red light'
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def stop(self):
        'This method is used to calculate the probability'
        return round(self.x/self.y)**10, 2)
         
class NotLight(Light):
    '''We create a superclass in order to use the base class method. This will allow us to
     find the probability of not getting a red light; it also allows us to reuse code.'''
    def __init__(self, x, y,):
        super().__init__(x, y)
        
    def __repr__(self):
        return '''
        The chances of encoutering a red light is {0} percent
        The chances of not encoutering a red light is {1} 
        percent'''.format(a.stop(), b.stop())
        
    def __str__(self):
        return repr(self)
        
          
a = Light(1, 6)
b = NotLight(5, 6)
        
if __name__ == "__main__":
    main()

============================================================================================================================
# A simple demonstration of the underlying logic of superclasses that I used in my probability program.  
# Superclasses are quite effective in their ability to reuse both code and instance methods.

class A(object):
    def __init__(self, x):
        self.x = x
        
class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y 

class C(B):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
        
class D(C):
    def __init__(self, x, y, z, a):
        super().__init__(x, y, z)
        self.a = a 
        
        
a = A(10)
b = B(20, 30)
c = C(40, 50 , 60)
d = D(70, 80, 90, 100)

================================================================================================================================

# Polymorphisim allows different classes to possess the same named methods and properties.
# This simple example, using terms gleaned from statistical probability theory, demonstrates the 
# power of polymorphism

class Distribution:
    def __init__(self, dist):
        if not dist.endswith(self.ext):
            raise Exception("The File Format is Incorrect")
        self.dist = dist
        
class Exponential(Distribution):
    ext = "exponential"
    def stats(self):
        print("We are using the {} distribution".format(self.dist))
        
class Logonormal(Distribution):
    ext = "logonormal"
    def stats(self):
        print("We are using the {} distribution".format(self.dist))
        
class Pareto(Distribution):
    ext = "pareto"
    def stats(self):
        print(" the {} distribution".format(self.dist))
        
a = Exponential("x.exponential")
b = Logonormal("x.logonormal")
c = Pareto("x.pareto")

# we call the instance method

a.stats(), b.stats(), c.stats()

==================================================================================================================================

# Using instance, class, and static methods in Python


# An instance method, shown below, needs an instance object 
# in order to be called.  The instance is the first argument
# that is passed

class AClass(object):
    def an_instance_method(self, x, y, z=None):
        return self.a_class_method(x, y)

# However, a class method, shown below, does not need
# an instance.  It is the class, rather than the instnace, 
# which is the first argument that is passed

    @classmethod
    def a_class_method(cls, x, y, z=None):
        return cls.a_static_method(x, y, z=None)
        
# A static method, shown below, is quite similar to a class method
# The main difference is that neither an instance or a class is passed as the first argument.
# Keep in mind that static methods are rarely used, and often discouraged, in Python
        
    @staticmethod
    def a_static_method(x, y, z=None):
        return x, y, z

# We create an instance of the class
instance = AClass()

print("Your instance method is listed as", instance.an_instance_method(1,2))

# A class method does not initially use an instance object; instead
# it uses the class object as the intial paramenter

print("Your class method is listed as", AClass.a_class_method(3, 4))

# A static method does not have self as parameter; rather, it can be
# called directly from the class.

print("Your static method is listed as", AClass.a_static_method(5, 6))


# In addition, static or class methods can also be passed
# in the following manner:

class M:
    def f(x):
        return x**2
        
f = staticmethod(9) or f = classmethod(9)


==================================================================================================================================

# An example of multiple resolution order

# In larger class systems, the method resolution order is D - B - A - C
# The D-B-A-C method signifies a depth first method resolution search order

class A:
    print("This is A")
    
class B(A):
    print("This is B(A)")
    
class C(A):
    print("This is C(A)")
    
class D(B, C):
    pass

d = D()

# Python shows us the order in which attributes are checked

#  >>> print(D.mro())

# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]




=================================================================================
Marks Program
========================

This program will ask for a student's name and their final mark.

Once the professor has entered in the information, the values will stored into a dictionary.

After this, the keys and values will be ordered into a table and the data will be visualized using pandas.

Both the ordering and the visualization of the data will be done automatically.


#!/usr/bin/python3 

import pandas as pd

d = {}
for i in range(11):
    user = input("Enter the student's name followed by their final mark: ") 
    data = user.split()
    d[data[0]] = int(data[1])
    
    

marks = pd.DataFrame(list(d.items()), columns=['Student_Name','Final_Mark'])
print(marks)
print("The class average is", marks.mean())
print(marks.stack())
print(marks.plot(kind='bar', color = 'g')) # 'color' function changes the color of the bar
print(marks.plot(kind='barh', stacked=True, alpha=0.5))


===================================================================
Inventory Program 
======================================================

This program creates an inventory that allows the user to enter as much information into the inventory as they need. Once the information is entered, it is automatically displayed back to the user in a ordered list.

In addition, The program asks the user to enter in their username, If their username contains numbers, the program asks the user to only enter in a username that contains letters.

Please note that the program makes heavy use of regular expressions and object orientated programming concepts.


#!/usr/bin/python

# By using regular expressions the program
# will only accept either upper or lower-case letters
# as a username. 

import re

while True:
    user_name = input("\r\rPlease enter your username:\r")
    if not re.match("^[A-Za-z]*$", user_name):
        print("Error! Please only use letters in your name!")
    else:
        print("Hello  " + user_name)
        break


class Computer(object):
    'Creates an inventory computer class'
# The __init__ method initializes the attributes
# The __slots__method reduces the memory footprint, useful 
# when creating many instances of a single class    
    __slots__=['manufact', 'model', 'price', 'year']
    def __init__(self, manufact, model, price, year):
        self.manufact = manufact
        self.model = model
        self.price = price
        self.year = year
        
# We create an instance of the computer class

data = Computer(manufact, model, price, year)  
 
# We create a list to store the information
comp_list = []

# We create a for loop to enter the information
for i in range(1, 3):
    manufact = input('\nEnter the manufacturer: ')
    model = int(input('Enter the model number: '))
    price = float(input('Enter the retail price: '))
    year = int(input('Enter the model year: '))
    comp_list.append(i)
                            
for i in comp_list:
    print('\rHere is the data that you entered:\n')
    print('The Manufacturer is:', data.manufact)
    print('The model is:', data.model) 
    print('The price is: $', data.price)
    print('The year is:', data.year)
    print(i)
    

===================================================================
Regular Expressions
==================================

Program 1: We are asked to find dates from a list that spans many lines and print them as an ordered list. We import regular expressions and use re.MULTILINE in order to solve the problem.

Program 2: Someone has mispelled a word a few times in a file. We are asked to use a regular expression to replace many instances of this wrongly place word. We will use re.sub to replace the word "the" with "HOT".

The rest of the code includes answers to a few interesting problems that were given to me to solve. Thank you for sending me these problems!


# usr/bin/python3

# We are asked to find dates from a list that spans many lines
# and print them as an ordered list
# we import regular expressions and use re.MULTILINE

import re

a = re.compile('^\w+\: (\w+/\w+/\w+)', re.MULTILINE)
b = a.findall('date: 11/03/2011 \ndate: 11/02/2015  \
date: 12/03/2007 \ndate: 09/03/2014')

print("These are the dates that were found in the list: ")
for i in b:
    print(i)
    
    
# Someone has mispelled a word a few times in a file
# We are asked to use a regular expression to replace many
# instances of this wrongly place word
# We will use re.sub to replace word "the" with "HOT"

import re
a = re.compile(r'the+')
b = a.sub('HOT', 'It is the because summer makes it the.')
print(b)



===========================================================================================================================

# --------------
#  QUESTION ONE 
# --------------

# Write a function that prints the numbers from 1 to 100. But for multiples of three print “Foo” instead 
# of the number and for the multiples of five print “Bar”. For numbers which are multiples of both three and
# five print “FooBar”. Example output:  1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 FooBar ... 


for i in range(1, 101):
    if i % 3 == 0:
        print('Foo', end=',')
    elif i % 5 == 0:
        print('Bar', end=',')
    elif i % 15 == 0:
        print('FooBar', end=',')
    else:
        print(i, end=',')

# --------------
# QUESTION TWO 
# --------------
# Write a function that counts the number of even numbers that appear in a range of
# integers 0..n, where n is supplied as the sole argument to your function. 

def main():
    n = int(input("Please enter a even number: "))
    n = n / 2
    print("The number of even integers in your number is", n)
if __name__ == "__main__": main()

# --------------
# QUESTION THREE 
# --------------
# Given the following pseudo code, determine the range of possible values for “a” in your language of choice: 
# x = random_int(1,6) 
# y = random_int(1,6) 
# z = random_int(1,6) 
# a = x + y + z 


import random 

x = random.randint(1,6)
y = random.randint(1,6)
z = random.randint(1,6)
a = x + y + z

print(a)

# --------------
#  QUESTION FOUR 
# --------------
# Given: 
# words = ['one', 'one', 'two', 'three', 'three', 'two'] 
# Remove the duplicates. 

a = ['one', 'one', 'two', 'three', 'three', 'two']       
b = ', '.join(sorted(set(a), key=a.index))
print(b)

# --------------
#  QUESTION FIVE 
# --------------
#Print the following output using only one loop: 
# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5 

x = 1
for i in range(5):
  print (x,x,x,x)
  x += 1
  
# --------------
#  QUESTION SIX 
# --------------
# Write a method that finds the largest sum of consecutive entries in an array given a group size. 
# It should take an array and the interval size as inputs and should return both the largest sum and
# the index of the first entry in the group. 
# For example, in the following Array [1,1,1,1,1,1,1,2] given a group size of 2 the 
# result would be a maximum sum of 3 and a position of 6. 

Array = [1,1,1,1,1,1,1,2]

group = 2

group_sum = 0

for i in range(len(Array)-1):
    temp_sum = sum(Array[i: (i+group)])
    if temp_sum > group_sum:
        group_sum = temp_sum
        position = i
    temp_sum = 0
    
print (group_sum, position)


=======================================
4
===============================

An extremely large dataset, one that spans 202 rows, and 358 columns, from the World Health Organization, is data mined in order to examine the relationship between countries and urban population growth.

Data is mined and sorted in order to create the follwing values:

1: The top 20 countries with increasing growing populations 2: The top 20 countries with declining urban populations

This sorted data is then visualized and displayed in .png files listed in the repository.


#!/usr/bin/python3 

import pandas as pd
import numpy as np 
import matplotlib as mp 

# This is a dataset from the World Health Organization 

data = pd.read_csv('WHO.csv') # This function imports the .csv file into pandas

data.shape # Tells you how many rows, followed by columns the file is. 
# In this case the file is listed as (202, 358). 
# It is therefore 202 rows, and 358 columns long. A very large file. 

data.info # tells you how much memory was used - in this case 566.5 KB

growth = data[['Urban_population_growth', 'Country']] # We are asked to
# create a table that compares 'Urban_population_growth' to 'Country'

# However, the data is unsorted and there are missing values in the dataset

urban_growth = urban_growth.dropna() # We take the rows containing missing data and drop them

urban_growth = growth.sort('Urban_population_growth')  # We sort the values according to Urban Population Growth

# Now we list the data  
urban_growth.head(20) # The top 20 countries, with growing Urban Population Growth are listed as follows: 

Urban_population_growth               Country

133                     4.20           Nigeria
132                     4.22             Niger
199                     4.37             Yemen
170                     4.40             Sudan
122                     4.47        Mozambique
181                     4.49              Togo
29                      4.58          Cambodia
39                      4.60  Congo, Dem. Rep.
64                      4.71            Gambia
110                     4.75              Mali
34                      4.88              Chad
20                      4.95            Bhutan
107                     5.02            Malawi
27                      5.09      Burkina Faso
126                     5.10             Nepal
161                     5.41      Sierra Leone
0                       5.44       Afghanistan
56                      5.56           Eritrea
28                      6.64           Burundi
150                     7.85            Rwanda

urban_growth.tail(20) # The top 20 countries, with declining Urban Population Growth are listed as follows: 

Urban_population_growth              Country

65                     -1.16         Georgia
117                    -0.99         Moldova
102                    -0.74       Lithuania
97                     -0.62          Latvia
7                      -0.62         Armenia
149                    -0.60          Russia
148                    -0.57         Romania
189                    -0.53         Ukraine
57                     -0.30         Estonia
73                     -0.22          Guyana
26                     -0.21        Bulgaria
66                     -0.03         Germany
163                     0.05        Slovakia
45                      0.09            Cuba
144                     0.09          Poland
15                      0.11         Belarus
47                      0.13  Czech Republic
87                      0.19           Japan
164                     0.25        Slovenia
169                     0.26       Sri Lanka
 
# We then plot the values 

urban_growth.plot(x='Country', y='Urban_population_growth', kind='barh)

# We set the x values as 'Country'
# We set the y values as 'Urban_population_growth'
