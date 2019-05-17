"""
Author:         Tim Smith
Description:    Solution to Class04 Ex1
"""

class_tuple = ("ITM220", "ITM251", "ITM360")# create a tuple

classname = input("Enter a class name: ")

if classname in class_tuple:
    print("Yes, I have taken this course")
else:
    print("No, I have not taken this course")