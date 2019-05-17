"""
Author:         Tim Smith
Description:    Solution to Class04 Ex2
"""

class_tuple = ("ITM220", "ITM251", "ITM360")# create a tuple
class_list = list(class_tuple)              # cast (aka convert) the class_tuple tuple to a list and store in class_list
class_list.append("ITM695")                 # add ITM695 to class_list
class_tuple = tuple(class_list)             # cast the class_list list to a tuple and store in class_tuple

print("The classes I've taken include the following: ")
for i in class_tuple:
    print(i)
