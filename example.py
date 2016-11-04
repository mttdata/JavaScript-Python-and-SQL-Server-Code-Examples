
T-SQL Coding Examples
=============================================================================================================================
This is an example of writing a script in T-SQL on SQL Server Management Studio in order 
to extract data between a specific date range.
=============================================================================================================================


USE [WorkDatabase]
GO

DECLARE @StartDate DATE
DECLARE @EndDate DATE

SET @StartDate  = '09/01/2010';
SET @EndDate = '08/30/2016';

SELECT TOP 100 A.Name AS [Estimate Name],  
A.GrandTotalRecoveredDepreciation AS [Claim Net ABC],
B.Number AS [Claim Number], CONVERT(VARCHAR(15), (D.LossDate), 107) AS  
[Loss Date],
CONVERT(VARCHAR(15), C.ClaimEstimateCompletedDate, 107) AS [Date], CASE
WHEN A.GrandTotalRecoveredDepreciation <= 1000 THEN 'Low Estimate Status'
WHEN A.GrandTotalRecoveredDepreciation BETWEEN 1000 AND 2000 THEN  
'Medium Estimate Status'
ELSE 'Large Status Normal'
END [Listed Estimate Status]
FROM Claims AS B WITH(NOLOCK)
INNER JOIN Estimates AS A WITH(NOLOCK)
ON A.ClaimID = B.ClaimID
INNER JOIN ClaimSummaryParticipantsView 
C.ClaimEstimateCompletedDate 
ON B.ClaimID = C.ClaimID
INNER JOIN Claims AS D WITH(NOLOCK) 
ON C.ClaimID = D.ClaimID
WHERE C.ClaimEstimateCompletedDate >= @StartDate and  
C.ClaimEstimateCompletedDate <=  @EndDate
ORDER BY [Claim Net ABC] DESC


Creating temporary tables with inner joins in order to extract data.  
=============================================================================================================================

DROP TABLE #AB2
SELECT A.ClaimID,
[WorkDatabase].[dbo].ClaimsStatus,
COUNT(EstimateItemID) AS COUNT_OF_ESTIMATE_ITEM
INTO #AB2
FROM WorkDatabase.dbo.leaves AS A WITH(NOLOCK)
INNER JOIN
#RC AS B
ON A.ClaimID = B.ClaimID
WHERE Description = 'Closed'
GROUP BY A.ClaimID
HAVING COUNT(EstimateItemID) >= 1

Creating both a primary and foreign key in SQL Server using the T-SQL programming language
============================================================================================================================

CREATE TABLE Employees
(
EmployeeNo INTEGER IDENTITY NOT NULL PRIMARY KEY,
EmployeeName VARCHAR(30) NOT NULL,
EmployeeHireDate DATE NOT NULL,
Title VARCHAR (25)NOT NULL,
SSN VARCHAR (11) NOT NULL,
Salary MONEY NOT NULL,
PriorSalary MONEY,
HireDate SMALLDATETIME NOT NULL,
CurrentlyEmployed BIT
)


CREATE TABLE PensionInformation
(
OrderID INTEGER IDENTITY NOT NULL PRIMARY KEY,
PensionNo INTEGER NOT NULL
BenefitsDate DATE NOT NULL,
EmployeeID INTEGER NOT NULL
FOREIGN KEY REFERENCES Employees(EmployeeNo)
ON UPDATE NO ACTION 
ON DELETE CASCADE 
)

SET IDENTITY_INSERT PensionInformation ON
GO 
INSERT INTO PensionInformation (PensionNo, BenefitsDate, EmployeeID)
VALUES (001, 03/11/2016, 15134)
SET IDENTITY_INSERT PensionInformation OFF

Using Nested Queries to Retrieve Data
====================================================

SELECT * FROM leaves AS A 
LEFT JOIN leaves2 AS B 
ON A.TreeID = B.TreeID 
WHERE A.TreeHeight > 16 
AND A.TreeHeight 
IN (SELECT A.TreeHeight FROM Leaves)
AND 
A.TreeID = (SELECT MAX(TReeID) From leaves) 

Creating a Temporary Table to Retrieve Data 
==================================================

SELECT A.TreeID, MAX(A.TreeHeight) AS TreeHeight 
INTO #TreeData
FROM leaves AS A 
GROUP BY A.TreeID, A.TreeName 

SELECT * FROM leaves2 AS B
JOIN #TreeData AS C
ON B.TreeID = C.TreeID 

DROP TABLE #TreeData

Using subqueries and temporary tables to retrieve and
transfer data into a new database 
=======================================================

SELECT A.TreeID, 
(SELECT MAX(TreeHeight)
FROM leaves2 AS B 
WHERE A.TreeID = B.TreeID)
AS NewTableName 
INTO #ABC 
FROM leaves AS A

SELECT *, 
CASE WHEN NewTableName IS NULL THEN 'NoData'
ELSE 'Data Entered' 
END AS NewInformationTable 
FROM #ABC 
DROP #ABC 

SELECT * INTO [Sample6].[dbo].[leaves7]
FROM #ABC 


Creating a searchable stored procedure to obtain data
==================================================

CREATE PROCEDURE sp_treename 
@TreeName VARCHAR(30)
AS
BEGIN 
SELECT TreeID, 
TreeHeight
FROM 
leaves 
WHERE TreeName LIKE @TreeName = '%'
END 

EXEC sp_treename 'Maple' 


Creating a Function 
==========================

CREATE FUNCTION Test1 
(@A INTEGER, 
@B INTEGER) 
RETURNS INTEGER 
AS 
BEGIN 
RETURN @A + @B 
END 


Creating a function in order to use inner joins
===================================================

CREATE FUNCTION fn_test()
RETURNS TABLE 
AS
RETURN (SELECT * FROM leaves)

SELECT * FROM fn_test() AS A
INNER JOIN leaves2 AS B
ON A.TreeID = B.TreeID 

sp_helptext fn_test 

Creating a multi-statement table valued function
===================================================

CREATE FUNCTION fn_trees()
RETURNS @Table TABLE (NewTreeHeight FLOAT, DateEntered DATETIME2)
WITH SCHEMABINDING
AS 
BEGIN 
INSERT INTO @Table
SELECT TreeHeight, CONVERT(VARCHAR(30), DateEntered, 107)
FROM leaves
RETURN 
END 

===========================================================

Using Nested Queries to Retrieve Data
====================================================

SELECT * FROM leaves AS A 
LEFT JOIN leaves2 AS B 
ON A.TreeID = B.TreeID 
WHERE A.TreeHeight > 16 
AND A.TreeHeight 
IN (SELECT A.TreeHeight FROM Leaves)
AND 
A.TreeID = (SELECT MAX(TReeID) From leaves) 

Creating a Temporary Table to Retrieve Data 
==================================================

SELECT A.TreeID, MAX(A.TreeHeight) AS TreeHeight 
INTO #TreeData
FROM leaves AS A 
GROUP BY A.TreeID, A.TreeName 

SELECT * FROM leaves2 AS B
JOIN #TreeData AS C
ON B.TreeID = C.TreeID 

DROP TABLE #TreeData

Using SubQueries and Temporary Tables to Retrieve Data and
to transfer the results into a new database 
=======================================================

SELECT A.TreeID, 
(SELECT MAX(TreeHeight)
FROM leaves2 AS B 
WHERE A.TreeID = B.TreeID)
AS NewTableName 
INTO #ABC 
FROM leaves AS A

SELECT *, 
CASE WHEN NewTableName IS NULL THEN 'NoData'
ELSE 'Data Entered' 
END AS NewInformationTable 
FROM #ABC 
DROP #ABC 

SELECT * INTO [Sample6].[dbo].[leaves7]
FROM #ABC 


Creating a searchable stored procedure to obtain data
==================================================

CREATE PROCEDURE sp_treename 
@TreeName VARCHAR(30)
AS
BEGIN 
SELECT TreeID, 
TreeHeight
FROM 
leaves 
WHERE TreeName LIKE @TreeName = '%'
END 



Creating a Function 
==========================

CREATE FUNCTION Test1 
(@A INTEGER, 
@B INTEGER) 
RETURNS INTEGER 
AS 
BEGIN 
RETURN @A + @B 
END 


Creating A Function
=======================

CREATE FUNCTION fn_test()
RETURNS TABLE 
AS
RETURN (SELECT * FROM leaves)

SELECT * FROM fn_test() AS A
INNER JOIN leaves2 AS B
ON A.TreeID = B.TreeID 

sp_helptext fn_test 

Creating an clustered index
==================

CREATE INDEX IX_leaves_TreeName
ON leaves(TreeName ASC)

--note: cannot create more than one clustered
--index on a table. 

Creating a view 
=====================

CREATE VIEW vWleaves
AS
SELECT 
TreeHeight, TreeName, DateEntered
FROM leaves

SELECT * FROM vWleaves 

UPDATE vWleaves
SET TreeName = 'Spruce' 
WHERE TreeHeight = 12.341
---note the parent table is also updated when the
--child table is altered in a view. this does not 
--usually happen when multiple tables are used. INSTEAD
OF triggers are used. 

Creating a clustered index on an existing view 

CREATE UNIQUE CLUSTERED INDEX UIX_VWleaves1
ON VWleaves1(TreeID) 

Creating a trigger
========================

CREATE TRIGGER tr_trigger1 
ON leaves15 
FOR INSERT --could also be update or delete
AS 
BEGIN 
SELECT LeafID FROM leaves15 
WHERE LeafID > 10 
END 

SET IDENTITY_INSERT leaves15 ON 
INSERT INTO leaves15 (LeafID, LeafName) VALUES (19, 2341)
SET IDENTITY_INSERT leaves15 OFF

Creating a trigger for update statement
============================================

CREATE TRIGGER tr_trigger2 
ON leaves15 
FOR UPDATE 
AS 
BEGIN 
	SELECT * FROM deleted
	SELECT * FROM inserted
END 

UPDATE leaves15 
SET LeafName = 3434
WHERE LeafID = 15 

Creating an INSTEAD OF Trigger for a delete statement
==================================================
CREATE VIEW vw1 
AS 
SELECT * FROM leaves AS A
INNER JOIN leaves15 AS B
ON A.TreeID = B.LeafID 

CREATE TRIGGER tr1 
ON vw1 
INSTEAD OF DELETE 
AS 
BEGIN 
   DELETE leaves
   FROM leaves
   JOIN deleted
   ON leaves.TreeID = deleted.TreeID 
END 

DELETE FROM vw1 WHERE LeafID = 6

Creating derieved tables 
=============================

SELECT * FROM 
(SELECT TreeID, TreeName, TreeHeight FROM leaves)
AS NewTreeInformation
WHERE TreeID IN (2, 4, 7) 
AND TreeHeight >= 15 

Creating a CTE(Common Table Expression) 
============================================

WITH TreeInfo(TreeID, TreeName, TreeHeight)
AS 
(SELECT TreeID, TreeName, COUNT(*) AS TotalTreeHeight
FROM leaves
GROUP BY TreeID, TreeName)
SELECT * FROM TreeInfo 
WHERE TreeName NOT IN ('Maple') 
AND TreeID > 3 

Using more than 1 CTE 
=============================
WITH TreeInfo(TreeID, TreeName)
AS 
(SELECT TreeID, TreeName
FROM leaves
GROUP BY TreeID, TreeName), 
SecondTreeInfo(LeafID, LeafName)
AS(SELECT * FROM leaves10)
SELECT * FROM TreeInfo
WHERE TreeName NOT IN ('Spruce')
AS TreeID >=2 AND TreeName = 'Maple'
UNION 
SELECT * FROM SecondTreeInfo 
WHERE LeafID > 25

Updating a CTE Table
===========================
WITH LeafInfo1(LeafID, LeafName)
AS 
(SELECT LeafID, LeafName
FROM leaves10)
UPDATE LeafInfo1 SET 
LeafName = 'Spruce' WHERE
LeafID = 25 





============================================================================================================================
Python Coding Examples
=============================================================================================================================
Creating a Web Scraper in Python 

#!/usr/bin/python
import requests
import re
from bs4 import BeautifulSoup
a = input("\r\rPlease enter the ISBN number:  ")
url = 'https://store.kobobooks.com/search?Query='
r = requests.get((url) + (a))
soup = BeautifulSoup(r.text)
print("\n\nThe author is", (re.sub(r"(<meta content=)|(property=)|([/>])|(.?author.*)|(^.)|(\..""$)", '', 
str((soup.find_all("meta", property="author"))))))
print("\nThe title of the book is", re.sub(r"(<meta content=)|(/s.*)|(....$)|(-)|(property=)|(/s.*$)|(o......../>?)|(..?$)|(Kobo)|(\s......$)", '', 
str((soup.find("meta", property="og:title")))))
print("\nThe book was published on ", re.sub(r"(<meta content=)|(property=)|(datePublished)|(/>)|(\s..''$)", '', 
str((soup.find("meta", property="datePublished")))))
print("\nThis is a description of the book:\n\n", re.sub(r"(<meta content=)|(property=)|(description)|(/)|(/>)|(/i&gt;)|(i&gt;)|(&lt;)|(b&gt;)|(br&gt;)", '', 
str((soup.find("meta", property='description')))))
print("\nThe book has a rating of ",re.sub(r"(<meta content=)|(property=)|(og:rating)|(/>)|(\s.*$)", '', 
str((soup.find("meta", property="og:rating")))))
print("\nThe price of the book is $",re.sub(r"(<meta content=)|(property=)|(og:price)|(/>)|(\s.*$)", '', 
str((soup.find("meta", property="og:price")))))


=============================================================================================================================
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




======================================================================================================================================================

An extremely large dataset, one that spans 202 rows, and 358 columns, from the World Health Organization, is data mined
in order to examine the relationship between countries and urban population growth.

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
