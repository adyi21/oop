#!/usr/bin/env python3

"""
71f27c9cdffad064338e8d8a33d14839
oopython
lab2
v2
adyi21
2022-01-27 15:34:52
v4.0.0 (2019-03-05)

Generated 2022-01-27 16:34:52 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""


from dbwebb import Dbwebb
from classes import Person, Address, Teacher, Student

# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - oopython
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python documentation](https://docs.python.org/3/library/index.html).
# Here you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Class relationships
#
# Practice on creating classes and relationships between them in python.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (2 points)
#
# Create a new file, put your code for the classes in it, call it
# **classes.py**.
#
# Create a new class named **Person**.  Give the class the instance
# attributes "name" and "ssn". Make "ssn" a private attribute. The values for
# the attributes should be sent to the constructor as arguments.
# Create a get method for "ssn".
#
# In the code below create a new variable called **per** and set it to a new
# instance of Person. Give it the name `Hugo` and ssn `541355-8072`.
#
#
# Answer with per\'s getter for ssn.
#
# Write your code below and put the answer into the variable ANSWER.
#


per = Person("Hugo", "541355-8072")



ANSWER = per.get_ssn()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (2 points)
#
# Create a new class named **Address**.  Give the class the instance
# attributes "city", "state" and "country". The values for the attributes
# should be sent to the constructor as arguments.
#
# Create the magic method **_\_str_\_**, in Address, it should return
# `"Address: <city> <state> <country>"` (replace the \<city\> with the value
# of the attribute city...).
#
# Create a new instance of the class Address. Initiate it with the city `Tar
# Valon`, the state `Throvenland` and the country `Ceald` and store it in a
# variable called **per_address**.
#
# Now, go back and add the instance attribute **address** to your Person
# class. It's value should be sent as argument to constructor, give it a
# default value of and empty string, `""`.
# Create a set method for the attribute "address".
#
# Create the magic method **_\_str_\_** for Person, it should return `"Name:
# <name> SSN: <ssn> Address: <city> <state> <country>"` if the person has an
# address or, `"Name: <name> SSN: <ssn>"` if its an empty string.
#
# Use Address' string representation to get address the data.
#
# Use the set method in Person to add the newly create Address object to your
# **per** object.
#
# Answer with per's string representation.
#
# Write your code below and put the answer into the variable ANSWER.
#

per_address = Address("Tar Valon", "Throvenland", "Ceald")

per.set_address(per_address)



ANSWER = str(per)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (2 points)
#
# Create a new class name **Teacher** make it inherit from class "Person".
# Add the instance attribute "courses" and initiate it to an empty list.
#
# Create the method **add_course**, it should take one argument and add it to
# the course list attribute.
#
# Overload the `__str__` method from the base class. It should return the
# same as the original method and add the courses to the end of the string,
# `"Name: <name> SSN: <ssn> Address: <city> <state> <country> Courses:
# <course>, <course>, ..."`. The list of courses should be comma seperated
# without one at the end. Use `super()` to access base method.
#
#
# Create a new instance of the class Teacher. Initiate it with the name
# `Hugo` and ssn `930807-7536`.
# Use the add_course method to add the following courses, `linux`, `linux`
# and `javascript1`.
#
#
# Answer with the Teacher object's string representation.
#
# Write your code below and put the answer into the variable ANSWER.
#

teacher = Teacher("Hugo", "930807-7536")
teacher.add_course("linux")
teacher.add_course("linux")
teacher.add_course("javascript1")




ANSWER = str(teacher)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (2 points)
#
# Create a new class name **Student** make it inherit from class "Person".
# Add the instance attribute "courses_grades" and initiate it to an empty
# list.
#
# Create the method **add_course_grade**, it should take two arguments, one
# course and a grade. Create a tuple with the two arguments and add to the
# attribute "courses_grades".
#
# Create the method **average_grade**. Calculate and return the students
# average grade. Ignore grades with "-" in the calculation.
#
# Create a new instance of the class Student. Initiate it with the name
# `Buster` and ssn `768244-4857`.
# Use the add_course_grade method to add the following courses, `python` with
# grade `3`, `linux` with grade `-` and `linux` with grade `3`.
#
#
# Answer with the Student object's "average_grade" method.
#
# Write your code below and put the answer into the variable ANSWER.
#

student = Student("Buster", "768244-4857")
student.add_course_grade("python", 3)
student.add_course_grade("linux", "-")
student.add_course_grade("linux", 3)




ANSWER = student.average_grade()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# In Teacher, create the *classmethod* **from_json** with one argument,
# `filename`.
# The *filename* is a json-file that contains data to create and return a new
# instance of the class Teacher.
# Use "teacher.json" to create a new instance of Teacher.
#
# Tip, import json and use `load` method.
#
# Answer with the new instance's string representation.
#
# Write your code below and put the answer into the variable ANSWER.
#


teacher_2 = Teacher.from_json('teacher.json')




ANSWER = str(teacher_2)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# In Teacher, create the method **to_json** that returns a JSON formatted
# dictionary.
# The dictionary should have the same structure as the file used above.
#
# Answer with a json string that has an indention of 4 spaces.
#
# Write your code below and put the answer into the variable ANSWER.
#

teacher_2 = Teacher.from_json('teacher.json')

xman = teacher_2.to_json()




ANSWER = xman
# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, True)


dbwebb.exit_with_summary()
